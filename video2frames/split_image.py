import cv2
import numpy as np

for frame_no in range(20, 600):
    input_img = cv2.imread('./op/frame%d.jpg' % frame_no)
    height, width = input_img.shape[:2]

    # Let's get the starting pixel coordiantes (top left of cropped top)
    start_row, start_col = int(0), int(0)
    start_row_right, start_col_right = int(0), int(width * .5)
    # Let's get the ending pixel coordinates (bottom right of cropped top)
    end_row, end_col = int(height), int(width * .5)
    end_row_right, end_col_right = int(height), int(width)
    cropped_left = input_img[start_row:end_row, start_col:end_col]
    cropped_right = input_img[start_row_right:end_row_right, start_col_right:end_col_right]

    cv2.imwrite("./left/left_frame%d.jpg" % frame_no, cropped_left)
    cv2.imwrite("./right/right_frame%d.jpg" % frame_no, cropped_right)
