import cv2
import numpy as np
import sklearn.preprocessing
from mediapipe.python.solutions import hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from tensorflow import keras

from utils.camera import CameraFrameHandler, CamVideoCaptureConfig, CamVideoCapture


class FUFingerFilter(CameraFrameHandler):
    __MAX_NUM_HANDS = 2
    __GESTURES = {0: 'fy'}

    def __init__(self):
        self.hand_detector = hands.Hands(
            max_num_hands=FUFingerFilter.__MAX_NUM_HANDS,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        self.classifier = keras.models.load_model('classifier.h5')

    def on_frame(self, frame):
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hand_detector.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                landmarks = np.zeros((21, 3))
                for idx, lm in enumerate(res.landmark):
                    landmarks[idx] = [lm.x, lm.y, lm.z]

                draw_landmarks(frame, res, hands.HAND_CONNECTIONS)
                normalized_features = sklearn.preprocessing.minmax_scale(landmarks).ravel()
                fu_confidence = self.classifier.predict(np.array([normalized_features]))

                if fu_confidence >= 0.7:
                    x1, y1 = tuple((landmarks.min(axis=0)[:2] * [frame.shape[1], frame.shape[0]] * 0.9).astype(int))
                    x2, y2 = tuple((landmarks.max(axis=0)[:2] * [frame.shape[1], frame.shape[0]] * 1.1).astype(int))
                    # Prevent index reference error
                    x1 = max(x1, 0)
                    y1 = max(y1, 0)
                    x2 = min(x2, frame.shape[1])
                    y2 = min(y2, frame.shape[0])

                    if x2 - x1 > 0 and y2 - y1 > 0:
                        mosaic = frame[y1:y2, x1:x2].copy()
                        mosaic = cv2.resize(mosaic, dsize=None, fx=0.05, fy=0.05, interpolation=cv2.INTER_NEAREST)
                        mosaic = cv2.resize(mosaic, dsize=(x2 - x1, y2 - y1), interpolation=cv2.INTER_NEAREST)

                        frame[y1:y2, x1:x2] = mosaic

        return frame


if __name__ == '__main__':
    filter = FUFingerFilter()

    config = CamVideoCaptureConfig(frame_handler=filter)
    player = CamVideoCapture(config)
    player.start()
