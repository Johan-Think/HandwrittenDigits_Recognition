# import numpy as np 
# from tensorflow.keras.datasets import mnist


# def load_data():
#     (x_train, y_train), (x_test, y_test) = mnist.load_data()
#     x_train = x_train / 255.0
#     x_test = x_test / 255.0
#     x_train_svm = x_train.reshape(-1, 28*28)
#     x_train_cnn = x_train.reshape(-1, 28, 28, 1)
#     x_test_cnn = x_test.reshape(-1, 28, 28, 1)
#     return x_train_svm, x_train_cnn, y_train, x_test_cnn, y_test


# # Convert data to array - like
# train_data = np . array ( train_dataset_path )
# test_data = np . array ( test_dataset_path )
# # Get all data from pixel1 , pixel2 ,... , pixel784
# x_train = train_data [: , 1:]
# x_test = test_data [: , 1:]
# # Get all the label from each image , we will use it to compare the prediction with
# the initial label
# y_train = train_data [: , 0]
# y_test = test_data [: , 0]
# # Reshape x_train , x_test from (1 x 784) array to (28 x 28) array
# x_train = x_train . reshape ( x_train . shape [0] , *(28 , 28 , 1) )
# x_test = x_test . reshape ( x_test . shape [0] , *(28 , 28 , 1) )


# # Scale value of x_train , x_test from [0 , 255] -> [0 , 1]
# x_train = x_train / 255.0
# x_test = x_test / 255.0
# # 21 sample image , grayscale
# plt . figure ( figsize =(18 , 9) )
# for i in range (21) :
# plt . subplot (3 , 7 , i + 1)
# plt . imshow ( x_train [i] , cmap = ’gray ’)
# plt . show ()
