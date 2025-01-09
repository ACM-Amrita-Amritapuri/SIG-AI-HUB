## Music Genre Classification and Prediction

This project demonstrates a machine learning model for classifying music genres using the GTZAN dataset. 
It includes data processing, feature extraction, model training, and a Tkinter-based GUI for predicting the genre of a given music file.

### Introduction

This project uses the GTZAN dataset to train a machine learning model that can classify music genres. The trained model can then be used to predict the genre of a given music file through a simple GUI application built with Tkinter.

### Features

- Data preprocessing and feature extraction
- Model training using RandomForestClassifier and KNeighborsClassifier
- Hyperparameter tuning with GridSearchCV
- Feature importance visualization
- Genre prediction through a Tkinter-based GUI

### Workflow
## Data Preparation
**Loading the Data:**
  Read the datasets features_3_sec.csv and features_30_sec.csv using pandas and concatenate them.
**Data Cleaning and Preprocessing:**
Convert the 'label' column to a categorical type and create a 'class_label' column with numerical codes for each genre.
Make a copy of the DataFrame for future use.

## Feature and Target Extraction
**Feature Extraction:**
Remove the 'filename' column and create a subset DataFrame containing only the feature columns.
**Target Extraction:**
Separate the feature columns (X) and target column (y) for model training.

## Data Splitting
  Split the data into training and testing sets using train_test_split from scikit-learn.

## Data Scaling
   Apply StandardScaler to scale the feature data. Fit the scaler on the training data and apply the same scaling to the testing data.

## Model Training and Evaluation
**Random Forest Classifier:**
  -Train a RandomForestClassifier on the scaled training data.
  -Plot and display the feature importances.
**K-Nearest Neighbors (KNN) Classifier:**
  -Use GridSearchCV to perform hyperparameter tuning for the KNN classifier.
  -Train the KNN classifier with a range of neighbor values (1 to 58).
  -Evaluate the model using accuracy score and classification report.

## Genre Prediction Function
**predict_genre_by_filename:**
  -Define a function to predict the genre of a given music file.
  -Extract features of the given file from the copied DataFrame.
  -Scale the features using the previously fitted scaler.
  -Use the trained model to predict the genre and map the prediction to the genre name using lookup_genre_name.

## GUI Application
**Tkinter Setup:**
  -Create a Tkinter GUI for selecting a music file and predicting its genre.
  -Add entry fields, buttons for browsing files, and displaying predictions.
**Open File Function:**
  -Define a function to open a file dialog for selecting a music file.
**Predict Function:**
  -Define a function to call predict_genre_by_filename and display the predicted genre in the GUI.

## Run the Application
Start the Tkinter GUI application to interactively select music files and predict their genres.
Detailed Steps
