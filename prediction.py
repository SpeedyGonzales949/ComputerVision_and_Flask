import tensorflow
from keras.utils import load_img, img_to_array
from keras.models import load_model
import numpy as np
import PIL


def predict_image_classification(file_path,model):

    reconstructed_model = load_model(f'static/Model/{model}.h5')
    if model=="ResNet":
        my_image = load_img(file_path, target_size=(128, 128))
    else:
        my_image = load_img(file_path, target_size=(224, 224))
    my_image = img_to_array(my_image)
    my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2])) / 255
    prediction = reconstructed_model.predict(my_image)
    pred = [np.argmax(element) for element in prediction]
    classes = ['georgia', 'crichi', 'mihnea']
    return classes[pred[0]]
