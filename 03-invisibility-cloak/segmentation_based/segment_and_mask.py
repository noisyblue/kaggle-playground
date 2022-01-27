#!/usr/bin/env python3
import sys

import cv2
import numpy as np

from pixellib.torchbackend.instance import instanceSegmentation

from camera import CamVideoCaptureConfig, CameraFrameHandler, CamVideoCapture


class FrameProcessor(CameraFrameHandler):
    frame_idx = 0
    background = None
    ins_seg = None
    src_file_name = None
    out_segmentation = None
    out_result = None

    def __init__(self, src_file_name=None):
        self.ins_seg = instanceSegmentation()
        self.ins_seg.load_model("pointrend_resnet50.pkl")  # try another detection_speed : fast or rapid
        self.src_file_name = src_file_name

        if self.is_processing_mode():
            self.out_segmentation = cv2.VideoWriter('out_segmentation.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30,
                                               (1280, 720))
            self.out_result = cv2.VideoWriter('out_result.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (1280, 720))

    def on_frame(self, frame):
        segment_display_frame = frame.copy()

        self.frame_idx += 1

        # Capture background during first 60 frames
        if self.frame_idx < 60:
            self.background = frame
            return frame
        elif self.frame_idx == 60:
            print("Starting segmentation...")

        results = self.ins_seg.segmentFrame(segment_display_frame, show_bboxes=True)

        mask = None
        anti_mask = None
        for idx, class_name in enumerate(results[0]['class_names']):
            mask_item = results[0]['masks'][:, :, idx]

            if class_name == 'person':
                mask_person = mask_item
                mask_person = np.where(mask_person == False, 0, 255).astype(np.uint8)

                mask = mask_person if mask is None else mask + mask_person
            else:
                anti_mask = mask_item if anti_mask is None else anti_mask + mask_item

        result = None
        if mask is not None:
            mask = cv2.dilate(mask, kernel=np.ones((10, 10), np.uint8), iterations=3)

            if anti_mask is not None:
                intersection = mask & anti_mask
                mask = mask ^ intersection

            mask_bg = cv2.bitwise_not(mask)
            res1 = cv2.bitwise_and(self.background, self.background, mask=mask)
            res2 = cv2.bitwise_and(frame, frame, mask=mask_bg)
            result = cv2.addWeighted(src1=res1, alpha=1, src2=res2, beta=1, gamma=0)

        cv2.imshow('result', result if result is not None else frame)

        if self.is_processing_mode():
            self.out_segmentation.write(segment_display_frame)
            self.out_result.write(result)

        return segment_display_frame

    def on_stop(self):
        if self.is_processing_mode():
            self.out_segmentation.release()
            self.out_result.release()

    def is_processing_mode(self):
        return self.src_file_name is not None


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print("Starting as processing mode...")
        config = CamVideoCaptureConfig(frame_handler=FrameProcessor(), file_name=sys.argv[1])
    else:
        print("Starting as preview mode...")
        config = CamVideoCaptureConfig(frame_handler=FrameProcessor())
    player = CamVideoCapture(config)
    player.start()
