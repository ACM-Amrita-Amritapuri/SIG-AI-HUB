Project Overview

The main goal of the project is to develop a system that can automatically analyze and classify the sentiment expressed in movie reviews(positive and negative here). This is useful for applications such as sentiment analysis in product reviews, customer feedback analysis, and more.

WORK FLOW:-

1.IMPORTING LIBRARIES:
    Necessary libraries are imported for data manipulation, machine learning, and evaluation.
2.LOADING DATASET:
    The IMDB dataset is loaded into a pandas DataFrame. The head() method displays the first few rows of the dataset.
3.ENCODING SENTIMENT LABELS:
    The LabelEncoder is used to convert the sentiment labels (positive/negative) into numerical form (1/0).
4.CHECKING DISTRIBUTION OF ENCODED SENTIMENTS:
    This line displays the count of each sentiment class in the dataset to check for class balance.          
5.CREATING A PIPELINE: 
    A pipeline is created to streamline the process of vectorizing text data and training a classifier. The pipeline consists of two steps:-
        *CountVectorizer: Converts text data into a matrix of token counts.
        *RandomForestClassifier: A random forest classifier with 5 trees and using entropy as the criterion for splitting.
6.SPLITING THE DATA:
    The dataset is split into training and testing sets. 80% of the data is used for training, and 20% is used for testing.        
7.TRAINING THE MODEL:
    The pipeline is trained using the training data (X_train and y_train). The fit method applies the CountVectorizer to the text data and then trains the RandomForestClassifier on the resulting numerical data.
8.MAKING PREDICTIONS:
    The trained model is used to predict the sentiment labels for the test data (X_test).    
9.EVALUATING THE MODEL:
    The accuracy of the model is calculated by comparing the predicted labels (y_pred) with the true labels (y_test). The accuracy score is printed.
10.IMPORTING TKINTER AND MODULES
11.CREATING THE MAIN APPLICATION WINDOW
12.CREATING WIDGETS (GUI ELEMENTS)
13.DEFINING THE PREDICTION FUNCTION:
    *process_input() function retrieves the text entered by the user (entry.get()).
    *Checks if there's any input. If not, it displays a warning message using messagebox.showwarning().
        If there is input:
            Uses a machine learning model (clf) to predict the sentiment (positive or negative) of the review text.
            Updates result_label with the prediction result (Prediction: Positive or Prediction: Negative) and changes the text color (fg) based on the sentiment (green for positive, red for negative).
14.CREATING THE PREDICT BUTTON
15.RUNNING THE APPLICATION    

Detailed Explanation of Key Components

#Pipeline:

    A pipeline helps in combining multiple steps into a single object, making the workflow more organized and easier to manage. It ensures that the steps are applied in the correct order.

#CountVectorizer:

    Converts the text data into a numerical form by counting the occurrences of each word. This representation is known as the Bag of Words (BoW) model.

#RandomForestClassifier:

An ensemble learning method that builds multiple decision trees and merges them to get a more accurate and stable prediction. It uses entropy to measure the quality of splits.

#LabelEncoder:

Converts categorical labels into numerical form. In this case, it converts sentiments (positive/negative) into 0 and 1.

#train_test_split:

Splits the dataset into training and testing sets to evaluate the performance of the model on unseen data.
