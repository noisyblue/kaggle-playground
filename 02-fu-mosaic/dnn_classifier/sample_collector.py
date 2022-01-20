import sys

import cv2
import numpy as np
import sklearn.preprocessing
from mediapipe.python.solutions import hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks

from utils.camera import CamVideoCapture, CamVideoCaptureConfig, CameraFrameHandler

CAM_WINDOW_NAME = "Sample collector"


class FingerSampleCollector(CameraFrameHandler):
    __GESTURES = {0: 'fy'}
    __SAMPLING_KEY_CODE = 115  # s key
    __DISCARD_KEY_CODE = 100  # d key

    def __init__(self, label: int, sample_file_name: str):
        self.hand_detector = hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

        self.label = label
        self.is_sampling = False
        self.sampled_finger_count = 0
        self.finger_samples = []
        self.sample_file_path = sample_file_name

    def on_frame(self, frame):
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hand_detector.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks:
            for res in result.multi_hand_landmarks:
                landmarks = np.zeros((21, 3))
                for idx, lm in enumerate(res.landmark):
                    landmarks[idx] = [lm.x, lm.y, lm.z]

                draw_landmarks(frame, res, hands.HAND_CONNECTIONS)

                if self.is_sampling:
                    normalized_features = sklearn.preprocessing.minmax_scale(landmarks).ravel()
                    if len(normalized_features) > 0:
                        label_appended_features = np.hstack((normalized_features, np.array([self.label])))
                        self.finger_samples.append(label_appended_features)
                        self.sampled_finger_count += 1

        pressed_key_code = cv2.waitKey(1) & 0xFF
        if pressed_key_code == FingerSampleCollector.__SAMPLING_KEY_CODE:
            self.toggle_sampling_mode()
        elif pressed_key_code == FingerSampleCollector.__DISCARD_KEY_CODE:
            self.stop_sampling()

        self.put_caption(frame,
                         f"Sampled {self.sampled_finger_count} fingers... s: save, d: discard" if self.is_sampling else "s: Start sampling, esc: Exit")

        return frame

    @staticmethod
    def put_caption(frame, text):
        cv2.putText(frame, text, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3, cv2.LINE_AA)

    def toggle_sampling_mode(self):
        if not self.is_sampling:
            self.start_sampling()
        else:
            self.stop_sampling_and_save()

    def start_sampling(self):
        self.sampled_finger_count = 0
        self.is_sampling = True

    def stop_sampling_and_save(self):
        result = np.asarray(self.finger_samples)
        with open(self.sample_file_path, "ab") as f:
            np.savetxt(f, result, delimiter=",")

        self.stop_sampling()

    def stop_sampling(self):
        self.is_sampling = False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} label output-file-path")
        exit(-1)

    sample_collector = FingerSampleCollector(int(sys.argv[1]), sys.argv[2])
    config = CamVideoCaptureConfig(frame_handler=sample_collector, window_name=CAM_WINDOW_NAME)
    player = CamVideoCapture(config)
    player.start()
