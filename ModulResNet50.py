import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from keras.layers import Dense,Flatten
import pathlib
import cv2

data_dir="DataSet_Create_Train/"
data_dir = pathlib.Path(data_dir)
global img_height
global img_width
img_height,img_width=180,180
global batch_size
batch_size=32

def EksekusiTran():
       global train_ds
       train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size) 

def EksekusiVal():
        global val_ds
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)
      

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)


val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)


def LoadDataSet():
            global class_names
            class_names = train_ds.class_names
            global resnet_model
            resnet_model = Sequential()

            pretrained_model= tf.keras.applications.ResNet50(include_top=False,
                              input_shape=(180,180,3),
                              pooling='avg',classes=5,
                              weights='imagenet')
            for layer in pretrained_model.layers:
                    layer.trainable=False

            resnet_model.add(pretrained_model)
            resnet_model.add(Flatten())
            resnet_model.add(Dense(512, activation='relu'))
            resnet_model.add(Dense(5, activation='softmax'))

            stringlist = []
            resnet_model.summary(print_fn=lambda x: stringlist.append(x))
            short_model_summary = "\n".join(stringlist)
            

            out = open('report.txt','w')
            out.write(str(class_names) + "\n" + short_model_summary) 
            out.close

            global history 

            history=np.load('database/history.npy',allow_pickle='TRUE').item()
            resnet_model.load_weights('database/my_model_weights.h5')

            # print(history)


def model_epochs(e,b):

            global resnet_model
            global history
            global batch_size
            batch_size = int(b)
            
            EksekusiTran()
            EksekusiVal()
        

            resnet_model.compile(optimizer='adam',loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
            history = resnet_model.fit(
                    train_ds, 
                    validation_data=val_ds, 
                    epochs=int(e))
            
            resnet_model.save_weights("database/my_model_weights.h5")
            np.save('database/history.npy',history.history)

           

            
def setGrafik():
            Laporan=np.load('database/history.npy',allow_pickle='TRUE').item()
            
            fig1 = plt.gcf()
            plt.plot(Laporan['accuracy'])
            plt.plot(Laporan['val_accuracy'])
            plt.axis(ymin=0.4,ymax=1)
            plt.grid()
            plt.title('Model Accuracy')
            plt.ylabel('Accuracy')
            plt.xlabel('Epochs')
            plt.legend(['train', 'validation'])
            plt.savefig('database/accuracy.png')
           

            plt.plot(Laporan['loss'])
            plt.plot(Laporan['val_loss'])
            plt.grid()
            plt.title('Model Loss')
            plt.ylabel('loss')
            plt.xlabel('epochs')
            plt.legend(['train', 'validation'])
            plt.savefig('database/model_loss.png')
            


def modul_deepfake(file):
    image=cv2.imread(file)

    image_resized= cv2.resize(image, (img_height,img_width))
    image=np.expand_dims(image_resized,axis=0)

    pred=resnet_model.predict(image)

    output_class=class_names[np.argmax(pred)]

    return output_class

