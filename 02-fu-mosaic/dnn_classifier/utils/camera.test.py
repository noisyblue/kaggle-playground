import cv2

from camera import CamVideoCapture, CamVideoCaptureConfig, CameraFrameHandler


class FrameProcessor(CameraFrameHandler):
    def on_frame(self, frame):
        new_frame = frame.copy()

        cv2.putText(new_frame, 'Hello!', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)
        return new_frame


if __name__ == '__main__':
    config = CamVideoCaptureConfig(frame_handler=FrameProcessor())
    player = CamVideoCapture(config)
    player.start()
