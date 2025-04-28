
# **Nhận dạng chữ số MNIST với Mô hình CNN**

## **Mô tả**
Trong notebook này, chúng ta sẽ xây dựng một mô hình học sâu để nhận dạng các chữ số viết tay từ tập dữ liệu MNIST bằng cách sử dụng Mạng Nơ-ron Chập (CNN). Mô hình sẽ được huấn luyện và đánh giá trên tập dữ liệu MNIST, bao gồm các bước tiền xử lý dữ liệu, xây dựng mô hình, huấn luyện, và đánh giá kết quả.

## **Các bước thực hiện**

### 1. **Thiết lập môi trường**
Đầu tiên, các thư viện cần thiết cho mô hình như `numpy`, `pandas`, `matplotlib`, `seaborn`, và `tensorflow` được nhập vào. Thư viện `keras` từ `tensorflow` được sử dụng để xây dựng mô hình CNN.

### 2. **Kiểm tra phiên bản TensorFlow và GPU**
Chúng ta sẽ kiểm tra phiên bản của TensorFlow và xem GPU có sẵn để tăng tốc quá trình huấn luyện hay không.

### 3. **Tải và khám phá dữ liệu**
- Dữ liệu MNIST được tải từ Keras/TensorFlow.
- Tập dữ liệu bao gồm hình ảnh của các chữ số viết tay từ 0 đến 9.
- Chúng ta sẽ hiển thị một số mẫu hình ảnh và phân bố lớp trong tập huấn luyện và tập kiểm tra.

### 4. **Tiền xử lý dữ liệu**
- Dữ liệu hình ảnh được chuẩn hóa và biến đổi thành dạng phù hợp cho mô hình CNN.
- Mỗi nhãn (label) được chuyển sang dạng one-hot encoding.
- Tập dữ liệu huấn luyện được chia thành tập huấn luyện và tập xác thực (validation set).

### 5. **Xây dựng mô hình CNN**
- Mô hình CNN được xây dựng với các lớp Conv2D, MaxPooling2D, Dropout, và BatchNormalization để cải thiện hiệu suất và tránh overfitting.
- Mô hình có 3 khối Conv2D kết hợp với MaxPooling2D và Dropout để giảm thiểu overfitting.

### 6. **Huấn luyện mô hình**
- Mô hình được huấn luyện trên tập dữ liệu huấn luyện với sự hỗ trợ của Data Augmentation để cải thiện khả năng tổng quát.
- Các callback như EarlyStopping và ReduceLROnPlateau được sử dụng để cải thiện quá trình huấn luyện.

### 7. **Đánh giá mô hình**
- Sau khi huấn luyện, mô hình được đánh giá trên tập kiểm tra (test set) và kết quả sẽ được hiển thị bao gồm độ chính xác (accuracy) và loss.
- Ma trận nhầm lẫn (confusion matrix) và báo cáo phân loại (classification report) được in ra để đánh giá chất lượng mô hình.

### 8. **Dự đoán mẫu**
- Các hình ảnh trong tập kiểm tra được dự đoán và so sánh với nhãn thực tế. Các dự đoán đúng sẽ được hiển thị với màu xanh và các dự đoán sai với màu đỏ.

### 9. **Kết luận**
- Mô hình đã được huấn luyện và lưu lại dưới dạng tệp `mnist_cnn_model.h5` để có thể tái sử dụng sau này.

## **Yêu cầu**
Để chạy notebook này, bạn cần cài đặt các thư viện sau:

- TensorFlow
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

### **Cài đặt TensorFlow**
```bash
pip install tensorflow
```

### **Cài đặt các thư viện khác**
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## **Chạy thử**
1. Tải tập dữ liệu MNIST từ Keras/TensorFlow.
2. Tiền xử lý và chuẩn hóa dữ liệu.
3. Xây dựng và huấn luyện mô hình CNN.
4. Đánh giá kết quả với các chỉ số như accuracy và loss.
5. Kiểm tra dự đoán mẫu.

## **Kết quả**
Sau khi huấn luyện, mô hình có thể phân loại chính xác các chữ số từ 0 đến 9 với độ chính xác cao.
