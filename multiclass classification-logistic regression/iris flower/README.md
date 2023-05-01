
# 🌺 Iris Species Predictor

This is a machine learning project that uses the scikit-learn dataset to predict the species of iris flowers. The model can predict three different species of iris: setosa, versicolor, and virginica.

## 📦 Libraries Used

This project uses the following libraries:
- 🧬 Scikit-learn for loading and preprocessing the iris dataset, and for training the logistic regression model.
- 🔢 NumPy for handling numerical operations and array manipulations.
- 📊 Matplotlib for visualizing the dataset and the model's performance.
- 🌊 Seaborn for creating the heatmap to explore the dataset's features and correlations.

## 🚀 Model Training

The logistic regression model was trained on the iris dataset, which consists of 150 samples of iris flowers, each with four features: sepal length, sepal width, petal length, and petal width. The dataset was split into training and testing sets with a ratio of 9:1.

The model was trained using the one-vs-rest approach to handle the multiclass classification problem. The training accuracy of the model was over 97%, demonstrating its effectiveness in predicting the species of iris flowers.

## 🔍 Exploratory Data Analysis

To better understand the dataset and the relationships between the features, we created a heatmap using the 🌊 Seaborn library. The heatmap shows the correlations between the different features in the dataset, which can help us identify any patterns or relationships that may exist.

From the heatmap, we can see that there are strong correlations between the petal length and petal width features, which can be useful in predicting the species of iris flowers.

## 📈 Model Performance

The model achieved an accuracy of over 97% on the test set, demonstrating its effectiveness in predicting the species of iris flowers. Overall, the model is effective in predicting the species of iris flowers based on their features, and can be used in various applications such as botany and agriculture.
