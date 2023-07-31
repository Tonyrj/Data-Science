# Data Science Project Management and Requirement Gathering
# Apparel Image Classification: Real vs. Fake

![Apparel Classification](https://github.com/Tonyrj/Data-Science/blob/Meenakshi-Remadevi-patch-1/class-lable-prediction.png)

This project focuses on building a Convolutional Neural Network (CNN) to classify images of apparels as either "Real" or "Fake." The dataset contains grayscale images of different apparels, and the goal is to accurately distinguish between authentic and counterfeit products.

## Data Preprocessing

The dataset is originally stored in a single folder, but it needs to be split into two separate folders: "Real" and "Fake" based on the matching ID provided in the CSV file. The data preprocessing step involves reading the CSV file and moving the images to their corresponding output folders. The function `separate_files` is utilized for this task.

```python
# Usage example
folder_path = 'path/to/images/folder'
csv_path = 'path/to/brand_info.csv'
real_folder = 'path/to/Real/folder'
fake_folder = 'path/to/Fake/folder'

separate_files(folder_path, csv_path, real_folder, fake_folder)
```

## Dataset Visualization

The processed dataset is then visualized to explore and understand the distribution of "Real" and "Fake" images. The images are displayed in two separate subplots, with the corresponding labels.

## CNN Model Architecture

The CNN model architecture is designed using Keras with TensorFlow as the backend. The model consists of convolutional layers followed by max-pooling layers to extract relevant features from the images. The final output layer uses softmax activation to classify the images into the two categories: "Real" and "Fake."

```python
# Define the CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(120, 120, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(2, activation='softmax'))
```

## Model Training and Evaluation

The CNN model is trained on the preprocessed dataset using the training generator. An early stopping callback is employed to prevent overfitting. The model's performance is evaluated using various metrics, such as accuracy, precision, recall, and area under the curve (AUC).

```python
# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=metrics_)

# Train the model
model.fit(train_images, epochs=5, validation_data=test_images, verbose=1, callbacks=early_stop)

# Evaluate the model on the test data
result = model.evaluate(test_images, steps=len(test_images), verbose=False, return_dict=True)

# Print evaluation results
print("The model trained has a result for:\nArea Under the Curve of {:.3f}\n\
\nAn Accuracy of {:.2f}%\nPrecison {:.2f}% and \nRecall of {:.2f}%".format(
    result['auc'],
    result['accuracy'] * 100,
    result['precision'] * 100,
    result['recall'] * 100
))
```

## Results and Visualizations

The model's performance is presented through various visualizations, including accuracy and loss plots during training and the confusion matrix after evaluation. The confusion matrix provides insight into the model's true positive, false positive, true negative, and false negative predictions.

## Next Steps

To further enhance the apparel classification model, we need to consider the following:

- Fine-tune hyperparameters and experiment with different model architectures.
- Increase the dataset size to improve model generalization.
- Explore data augmentation techniques to increase the dataset's diversity.
- Investigate other CNN models and transfer learning approaches for better performance.

---



