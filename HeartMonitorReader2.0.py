import cv2
import matplotlib.pyplot as plt
import torch
from ultralytics import YOLO

# Load the YOLO model
model_path = 'runs/detect/train20/weights/last.pt'


# Load the image you want to make predictions on
image_path = 'Processing_Images/images (4).jpg'



def image_to_vals(model_path, image_path):
    model = YOLO(model_path)
    img = cv2.imread(image_path)
    results = model(img)[0]
    results_list = results.boxes.data.tolist()
    value_dic = {}
    value_dic = {}
    for line in results_list:
        # Parse the values from the line
        x1, y1, x2, y2, score, class_id = map(float, line)
        print(class_id)
        # Convert float coordinates to integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        avg_y = (y1 + y2) / 2
        avg_x = (x1 + x2) / 2

        if score > 0.2:
            value_dic[avg_y] = [int(class_id) - 1, float(avg_x)]
        value_dic = dict(sorted(value_dic.items()))
    sorted_list_of_lists = sorted(value_dic.items(), key=lambda x: x[0])
    nested_list = [[key, value] for key, value in sorted_list_of_lists]
    print(nested_list)
    results_list = []
    result = []
    list_of_tuples = nested_list
    for ind, t in enumerate(list_of_tuples):
        if ind + 1 < len(list_of_tuples):
            if abs(t[0] - list_of_tuples[ind + 1][0]) <= 10:
                result.append(list_of_tuples[ind][1])
            else:
                result.append(list_of_tuples[ind][1])
                results_list.append(result)
                result = []
        else:
            result.append(list_of_tuples[ind][1])
            results_list.append(result)

    print(results_list)
    data = results_list
    # Sort each inner list based on the second values
    for inner_list in data:
        inner_list.sort(key=lambda x: x[1])
    print(data)
    final_list = []
    string = ''
    for lis_lists in data:
        for lis in lis_lists:
            string += str(lis[0])
        final_list.append(string)
        string = ''
    SYS = final_list[0]
    DIA = final_list[1]
    PULSE = final_list[2]

    print(final_list)
    print("THE SYS VALUE IS:", SYS)
    print("THE DIA VALUE IS:", DIA)
    print("THE PULSE VALUE IS:", PULSE)

image_to_vals(model_path, image_path)