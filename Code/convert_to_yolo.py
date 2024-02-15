import cv2
import json
def save_yolo_format(image_file, json_file, txt_file):
    with open(json_file) as f:
        chars = json.loads(f.read())

    bgr = cv2.imread(image_file)

    result = ""
    for char in chars:
        x_center = (char["x"] + char["width"] // 2) / bgr.shape[1]
        y_center = (char["y"] + char["height"] // 2) / bgr.shape[0]

        width = char["width"] / bgr.shape[1]
        height = char["height"] / bgr.shape[0]

        label = char["char_id"]

        result += str(label) + " " + str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height) + "\n"

    with open(txt_file, "w+") as f:
        f.write(result)

save_yolo_format("dataset_root/images/1.jpg",
                 "dataset_root/labels/1.json",
                 "dataset_root/labels/1.txt")
