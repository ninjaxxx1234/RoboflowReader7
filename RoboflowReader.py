from roboflow import Roboflow
rf = Roboflow(api_key="B2CGYEexTigY1JFIodvp")
project = rf.workspace().project("purushothamanomron")
model = project.version(1).model
image_path = "Processing_Images/images (3).jpg"
# infer on a local image


def ImageToVals(image_path):
  json_data = model.predict(image_path, confidence=20, overlap=30).json()
  model.predict(image_path, confidence=20, overlap=30).save("last.jpg")
  result_dict = {}
  print(json_data)
# Iterate through predictions and populate the result_dict
  for id, prediction in enumerate(json_data['predictions']):
    print(prediction)
    y_value = prediction['y'] + 0.0001*id
    class_id = prediction['class_id']
    x_coordinate = prediction['x']
    confidence = prediction['confidence']
    if confidence >= 0.5:
        result_dict[y_value] = [class_id, float(x_coordinate)]
  print(result_dict)
  sorted_list_of_lists = sorted(result_dict.items(), key=lambda x: x[0])
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





ImageToVals(image_path)
