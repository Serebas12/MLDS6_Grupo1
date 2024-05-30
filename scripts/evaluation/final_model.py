from argparse import ArgumentParser
import mlflow
import tensorflow as tf
import numpy as np
import json
import os

mlflow.set_tracking_uri("http://localhost:5000")
model_name = 'final_model'
model_version = 1
model = mlflow.pyfunc.load_model(f"models:/{model_name}/{model_version}")
c = [41, 43, 46, 51, 58, 73, 74, 75, 77, 78, 80, 81, 82, 83, 88, 89, 94, 95]
ordered_to_id = {i: j for i, j in enumerate(c)}
id_to_ordered = {j: i for i, j in ordered_to_id.items()}
#path_cat = os.path.join(os.path.dirname(__file__), "cat_to_name.json")
path_cat = "/content/src/cat_to_name.json"
with open(path_cat) as r:
  dict_flower = json.load(r)
dict_flower = {int(key): value for key, value in dict_flower.items()}


def preprocess_image(path_image):
  img = tf.keras.preprocessing.image.load_img(
      path_image, target_size = (224, 224, 3)
  )
  img = np.array([img])
  return img

def classify_image(path_image):
  img = preprocess_image(path_image)
  prediction = model.predict(img).argmax(axis=1)
  return prediction

def convert_id(value, via):
  if via == 'to_id':
    return ordered_to_id[value]
  if via == 'to_ordered':
    return id_to_ordered[value]

def correct_classify(prediction):
  correct_prediction = convert_id(prediction, "to_id")
  pred_fl = dict_flower.get(correct_prediction, "Flor no identificada")
  return pred_fl

def main():
  parser = ArgumentParser(
      description = "CLI para modelo de clasificación de flores"
  )
  parser.add_argument(
      "--text", type=str, required=True, help="Ruta de la imagen a clasificar"
  )
  args = parser.parse_args()
  prediction = classify_image(args.text)[0]
  correct_pred = correct_classify(prediction)
  print(f"El tipo de flor en la imagen es: {correct_pred}")

if __name__ == "__main__":
  main()
