
# 🤖 Logistic Regression Multiclass Number Predictor 

This is a project that uses logistic regression to predict the value of a given number based on its image. The model can predict numbers from 0 to 9 with high accuracy.

## 📦 Libraries Used

This project uses the following libraries:
- 🧬 Scikit-learn for loading and preprocessing the image dataset, and for training the logistic regression model.
- 🔢 NumPy for handling numerical operations and array manipulations.
- 📊 Matplotlib for visualizing the dataset and the model's performance.
- 🌊 Seaborn for creating the heatmap to explore the dataset's features and correlations.
- 🐼 Pandas for organizing and displaying the dataset's statistics and information.

## 🚀 Model Training

The logistic regression model was trained on a custom dataset created using image data from the scikit-learn library. The dataset consists of 60,000 training images and 10,000 testing images, with each image being a 28x28 grayscale image of a single digit.

The image pixels were flattened into a 1D array and used as the input to the logistic regression model. The model was trained using the one-vs-rest approach to handle the multiclass classification problem.

The model achieved an accuracy of over 95% on the test set, demonstrating its effectiveness in predicting the value of handwritten digits.

## 🔍 Exploratory Data Analysis

To better understand the dataset and the relationships between the features, we created a heatmap using the 🌊 Seaborn library. The heatmap shows the correlations between the different pixels in the images, which can help us identify any patterns or relationships that may exist.

From the heatmap, we can see that there are some correlations between the pixels in the images. For example, pixels in the center of the image tend to be more highly correlated with each other than with pixels at the edges of the image.

## 📈 Model Performance

The model achieved an accuracy of over 95% on the test set, demonstrating its effectiveness in predicting the value of handwritten digits. Overall, the model is effective in predicting the values of handwritten digits.
