import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_accuracy(history, save_path='outputs/figures/accuracy.png'):
       plt.figure(figsize=(12, 5))
       plt.subplot(1, 2, 1)
       plt.plot(history.history['accuracy'], label='Train Accuracy')
       plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
       plt.title('Accuracy over epochs')
       plt.ylabel('Accuracy')
       plt.xlabel('Epoch')
       plt.legend()
       plt.subplot(1, 2, 2)
       plt.plot(history.history['loss'], label='Train Loss')
       plt.plot(history.history['val_loss'], label='Validation Loss')
       plt.title('Loss over epochs')
       plt.ylabel('Loss')
       plt.xlabel('Epoch')
       plt.legend()
       plt.tight_layout()
       plt.savefig(save_path)
       plt.close()

def plot_confusion_matrix(y_true, y_pred_classes, save_path='outputs/figures/confusion_matrix.png'):
       cm = confusion_matrix(y_true, y_pred_classes)
       plt.figure(figsize=(10, 8))
       sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                   xticklabels=range(10), yticklabels=range(10))
       plt.title('Confusion Matrix')
       plt.xlabel('Predicted Label')
       plt.ylabel('True Label')
       plt.savefig(save_path)
       plt.close()