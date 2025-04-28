def build_cnn_model():
       # Placeholder
       pass

   def train_cnn(model, X_train, y_train, X_val, y_val, datagen):
       # Placeholder
       pass
# model = keras . Sequential ()
# model . add ( keras . Input ( shape = (28 , 28 , 1) ))
# model . add ( keras . layers . Conv2D ( filters = 32 , kernel_size = (3 , 3) , activation = ’relu ’
# ))
# model . add ( keras . layers . MaxPool2D ( pool_size = (2 , 2) ))
# model . add ( keras . layers . Dropout ( rate = 0.3) )
# model . add ( keras . layers . Conv2D ( filters = 64 , kernel_size = (3 , 3) , activation =’relu ’)
# )
# model . add ( keras . layers . MaxPool2D ( pool_size = (2 , 2) ))
# model . add ( keras . layers . Dropout ( rate = 0.3) )
# model . add ( keras . layers . Conv2D ( filters = 128 , kernel_size = (3 , 3) , activation =’relu ’
# ))
# model . add ( keras . layers . MaxPool2D ( pool_size = (2 , 2) ))
# model . add ( keras . layers . Dropout ( rate = 0.3) )
# model . add ( keras . layers . Flatten () )
# model . add ( keras . layers . Dense ( units = 128 , activation = ’relu ’))
# model . add ( keras . layers . Dense ( units = 25 , activation = ’softmax ’))
# # Configures the model for training .
# model . compile ( loss = ’ sparse_categorical_crossentropy ’, optimizer = ’adam ’, metrics =
# [’acc ’])
# # Reduce learning rate when a metric has stopped improving .
# reduce_lr = keras . callbacks . ReduceLROnPlateau ( monitor =’val_acc ’, patience = 2,
# verbose = 1, mode =’max ’, min_lr = 0.00001)

# # Prints a string summary of the network
# model . summary ()


# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report
# import pickle
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

# def train_svm(X_train, y_train, save_path='models/svm.pkl'):
#     svm = SVC(kernel='rbf', C=1)
#     svm.fit(X_train[:10000], y_train[:10000])
#     with open(save_path, 'wb') as f:
#         pickle.dump(svm, f)
#     return svm

# def train_cnn(X_train, y_train, save_path='models/cnn.h5'):
#     model = Sequential([
#         Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
#         MaxPooling2D((2,2)),
#         Conv2D(64, (3,3), activation='relu'),
#         MaxPooling2D((2,2)),
#         Flatten(),
#         Dense(128, activation='relu'),
#         Dense(10, activation='softmax')
#     ])
#     model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#     model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
#     model.save(save_path)
#     return model

# def evaluate_model(model, X_test, y_test, output_path='outputs/metrics.txt'):
#     y_pred = model.predict(X_test) if 'predict' in dir(model) else model.predict(X_test).argmax(axis=1)
#     accuracy = accuracy_score(y_test, y_pred)
#     report = classification_report(y_test, y_pred)
#     with open(output_path, 'w') as f:
#         f.write(f"Accuracy: {accuracy}\n{report}")
#     return accuracy, report