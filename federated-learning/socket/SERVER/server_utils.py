
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np

def create_and_save():
    # creates the neural network for MNIST dataset

	# Creating a Sequential Model and adding the layers
	model = Sequential()
	model.add(Conv2D(28, kernel_size=(3,3), input_shape=input_shape))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Flatten()) # Flattening the 2D arrays for fully connected layers
	model.add(Dense(128, activation=tf.nn.relu))
	model.add(Dropout(0.2))
	model.add(Dense(10,activation=tf.nn.softmax))
	#serialize model to JSON
	model_json = model.to_json()
	with open("model.json", "w") as json_file:
	   json_file.write(model_json)
	   
	   
def load_and_send():
    # load json and create model
    json_file = open('model.json', 'rb')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    return loaded_model

def load_weights_and_evaluate(loaded_model):
    # load weights into new model
    #loaded_model.load_weights("weights.h5")
    #print("Loaded model from disk")
    print("weights saved to disk")
    loaded_model.save_weights("weights.h5")
    
    loaded_model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    #Evalutation of the model
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train= x_train[-200:]
    y_train=y_train[-200:]
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
    # Making sure that the values are float so that we can get decimal points after division
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # Normalizing the RGB codes by dividing it to the max RGB value.
    x_train /= 255
    x_test /= 255
    
    loaded_model.evaluate(x_test, y_test)
    # Making a single prediction
    image_index = np.random.randint(200)
    
    pred = loaded_model.predict(x_test[image_index].reshape(1, 28, 28, 1))
    print("predicted: ",pred.argmax())
    print("target: ", y_test[image_index])
    

def load_model_and_train(num=0,fold = 5000):
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    # x_train=x_train[num*fold:(num+1)*fold]
    # y_train = y_train[num*fold:(num+1)*fold]
    # x_test = x_test[num*fold:(num+1)*fold]
    # y_test = y_test[num*fold:(num+1)*fold]
    # Reshaping the array to 4-dims so that it can work with the Keras API
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
    # Making sure that the values are float so that we can get decimal points after division
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # Normalizing the RGB codes by dividing it to the max RGB value.
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)

    
    # load json and create model
    json_file = open('model.json', 'rb')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    loaded_model.fit(x=x_train,y=y_train, epochs=10)
    loaded_model.evaluate(x_test, y_test)
    
    
    # serialize weights to HDF5
    loaded_model.save_weights("weights.h5")
    print("Saved model to disk")
    return loaded_model
# serialize model to JSON
# model_json = model.to_json()
# with open("data/model.json", "w") as json_file:
#     json_file.write(model_json)    

