import abc
from dataclasses import dataclass
from typing import Any

import cv2


class CameraFrameHandler:
    @abc.abstractmethod
    def on_frame(self, frame) -> Any:
        raise NotImplementedError()


@dataclass()
class CamVideoCaptureConfig:
    DEFAULT_WINDOW_NAME = "CamVideoCapture"
    DEFAULT_QUIT_KEY_CODE = 27  # Esc key

    frame_handler: CameraFrameHandler
    cam_index: int = 0
    window_name: str = DEFAULT_WINDOW_NAME
    quit_key_code: int = DEFAULT_QUIT_KEY_CODE


class CamVideoCapture:
    def __init__(self, config: CamVideoCaptureConfig):
        self.is_started = False
        self.videoCapture = None
        self.config = config

    def start(self):
        if self.is_started:
            print("Camera capture already started. Ignoring...")
            return

        print("Starting camera video capture...")
        self.videoCapture = cv2.VideoCapture(self.config.cam_index)
        self.is_started = True

        cv2.namedWindow(self.config.window_name, cv2.WINDOW_NORMAL)

        # Make window focused
        cv2.setWindowProperty(self.config.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty(self.config.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

        while self.videoCapture.isOpened():
            ret, img = self.videoCapture.read()

            if not ret or img is None:
                print("Can't receive frame. Skipping frame loop...")
                continue

            processed_frame = self.config.frame_handler.on_frame(img)
            cv2.imshow(self.config.window_name, processed_frame if processed_frame is not None else img)

            if cv2.waitKey(1) & 0xFF == self.config.quit_key_code:
                print("Quit key was pressed. Exiting...")
                self.stop()
                break

    def stop(self):
        if not self.is_started:
            print("Camera capture is not started. Ignoring...")
            return

        print("Stopping camera video capture...")
        self.videoCapture.release()
        self.videoCapture = None
        self.is_started = False

        cv2.destroyWindow(self.config.window_name)
