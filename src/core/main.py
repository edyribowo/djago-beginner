import numpy as np
from keras.preprocessing import image
import tensorflow as tf


def hello_world():
    model = tf.keras.models.load_model('CatVsDogs.h5')
    model.summary()
    nameImage = 'image.jpeg'
    img = image.load_img('../src/images/' + nameImage, target_size=(300, 400))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    result = ''
    if classes[0][0]<0.5:
        result = 'Dog'
    else:
        result = 'Cat'

    print(result)
hello_world()
