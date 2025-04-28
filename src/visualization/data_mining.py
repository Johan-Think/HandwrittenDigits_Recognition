import matplotlib.pyplot as plt
   import seaborn as sns
   import numpy as np

   def visualize_samples(X_data, y_data, save_path='outputs/figures/samples.png'):
       plt.figure(figsize=(10, 10))
       for i in range(25):
           plt.subplot(5, 5, i+1)
           plt.imshow(X_data[i].reshape(28, 28), cmap='gray')
           plt.title(f"Label: {y_data[i]}")
           plt.axis('off')
       plt.tight_layout()
       plt.savefig(save_path)
       plt.close()

   def visualize_class_distribution(y_train, y_test, save_path='outputs/figures/class_distribution.png'):
       plt.figure(figsize=(12, 5))
       plt.subplot(1, 2, 1)
       sns.countplot(x=y_train)
       plt.title('Phân bố lớp - Tập train')
       plt.subplot(1, 2, 2)
       sns.countplot(x=y_test)
       plt.title('Phân bố lớp - Tập test')
       plt.tight_layout()
       plt.savefig(save_path)
       plt.close()

   def visualize_predictions(X_test, y_true, y_pred_classes, save_path='outputs/figures/predictions.png'):
       plt.figure(figsize=(12, 12))
       for i in range(16):
           plt.subplot(4, 4, i+1)
           plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
           pred_label = y_pred_classes[i]
           true_label = y_true[i]
           color = 'green' if pred_label == true_label else 'red'
           plt.title(f"Pred: {pred_label}, True: {true_label}", color=color)
           plt.axis('off')
       plt.tight_layout()
       plt.savefig(save_path)
       plt.close()

# # Training dataset overview
# fig = plt . figure ( figsize =(12 , 9) )
# axes = sns . countplot ( x=" label ", data = train_dataset_path )
# axes . set_ylabel (’Count ’)
# axes . set_title (’Label of images in train dataset ’)
# plt . show ()
# # Testing dataset overview
# fig = plt . figure ( figsize =(12 , 9) )
# axes = sns . countplot ( x=" label ", data = test_dataset_path )
# axes . set_ylabel (’Count ’)
# axes . set_title (’Label of images in test dataset ’)
# plt . show ()