import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#--------------------------------------------------------------------------------------
#   Function Name   :   PreserveModel
#   Description     :   It used to preserve model on secondary 
#   Parameters      :   model, filename
#   Return          :   None
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

def PreserveModel(model, filename):
    joblib.dump(model, filename)
    
    print("Model Preserved successfully with name : ", filename)

#--------------------------------------------------------------------------------------
#   Function Name   :   TrainTitanicModel
#   Description     :   It does splitting X, Y, Training data , testing data
#   Parameters      :   df
#   Return          :   None
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

# Split features and labels
def TrainTitanicModel(df):
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]
    
    print("\nFeatures : ")
    print(X.head())
    
    print("\nLabels : ")
    print(Y.head())
    
    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    
    print("X_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ", Y_test.shape)
    
    model = LogisticRegression(max_iter=1000)
    
    model.fit(X_train, Y_train)
    
    print("Model trained successfully")
    
    print("\nIntercept of model : ")
    print(model.intercept_)
    
    print("\nCoeficient of model")
    for feature, coefficient in zip(X.columns, model.coef_[0]):
        print(feature, " : ", coefficient)
        
    PreserveModel(model,"marvelloustitanic.pkl")

#--------------------------------------------------------------------------------------
#   Function Name   :   CleanTitanicData
#   Description     :   It does preprocessing
#                       It remove unnecessary columns
#                       It handle missing values
#                       It converts text data to numeric formate
#                       It does encoding to categorical columns
#   Parameters      :   df
#                       df -> Pandas dataframe
#   Return          :   df
#                       df -> Clean Pandas dataframe
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original data")
    print(df.head())
    
    # Remove unnecessary columns
    drop_columns = ["Passengerid", "zero", "Name", "Cabin"]
    
    existing_columns = [col for col in drop_columns if col in df.columns]
    
    print("\nColumns tobe dropped : ")
    print(existing_columns)
    
    # Drop the unwanted columns
    df = df.drop(columns= existing_columns)
    
    DisplayInfo("Step 3 : Data after column removal")
    print(df.head())
    
    # Handle Age column
    
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))
        
        # coerce -> Invalid value gets converted to NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
        
        age_median = df["Age"].median()
        print("\nMedian of Age column is : ", age_median)
        
        # Replace missing value with median
        df["Age"] = df["Age"].fillna(age_median)
        
        print("Age column after preprocessing\n")
        print(df["Age"].head(10))
        
    # Handle Fare column
    if "Fare" in df.columns:
        print("Fare column before filling missing values")
        print(df["Fare"].head(10))
        
        # coerce -> Invalid value gets converted to NaN
        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
        
        fare_median = df["Fare"].median()
        print("\n Median of fare column is : ", fare_median)
        
        # Replace missing value with median
        df["Fare"] = df["Fare"].fillna(age_median)
        
        print("Fare column after preprocessing\n")
        print(df["Fare"].head(10))
        
    # Handle Embark column
    
    if "Embarked" in df.columns:
        print("Embarked column before filling missing values")
        print(df["Embarked"].head(10))
        
        # convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()
        
        # Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan','None',''], np.nan)
        
        # Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        
        print('\nMode of embarked column : ', embarked_mode)
        
        df["Embarked"] = df["Embarked"].fillna(embarked_mode)
        
        print("Embarked column after preprocessing\n")
        print(df["Embarked"].head(10))
        
    # Handle Sex column
    if "Sex" in df.columns:
        print("Sex column before filling missing values")
        print(df["Sex"].head(10))
        
        # coerce -> Invalid value gets converted to NaN
        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")
        
        print("Sex column after preprocessing\n")
        print(df["Sex"].head(10))
        
    DisplayInfo("Data After preprocessing")
    print(df.head())
    
    print("\nMissing values after preprocessing")
    print(df.isnull().sum())
    
    # Encode Embarked column
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)
    print("\nData After encoding")
    
    print(df.head())
    print("Shape of Dataset : ", df.shape)
    
    # convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)
            
    print("\nData After encoding")
    
    print(df.head())
    print("Shape of Dataset : ", df.shape)
    
    return df

#--------------------------------------------------------------------------------------
#   Function Name   :   ShowData
#   Description     :   It shows basic information about dataset(df)
#   Parameters      :   df
#                       df      ->  pandas dataframe objcet
#                       message
#                       message ->  Heading text to display 
#   Return          :   None
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo(message)
    
    print("First 5 rows of Dataset : ")
    print(df.head())
    
    print("\nShape of dataset : ")
    print(df.shape)
    
    print("\nColumn name : ")
    print(df.columns.tolist())
    
    print("\nMissing Values in each column : ")
    print(df.isnull().sum())

#--------------------------------------------------------------------------------------
#   Function Name   :   DisplayInfo
#   Description     :   It displays the formated title
#   Parameters      :   title(str)
#   Return          :   None
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

#--------------------------------------------------------------------------------------
#   Function Name   :   TitanicLogistic
#   Description     :   -This is main pipeline controller
#                       -It loads the dataset, shows raw data
#                       -It preprocess the dataset and train the model
#   Parameters      :   Datapath of dataset file
#   Return          :   None
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

def TitanicLogistic(Datapath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(Datapath)
    
    ShowData(df, "Initial Dataset")
    
    df = CleanTitanicData(df)
    
    TrainTitanicModel(df)
    
#--------------------------------------------------------------------------------------
#   Function Name   :   main
#   Description     :   Starting point of application
#   Parameters      :   None
#   Return          :   None
#   Date            :   14/03/2026
#   Author          :   Aditya Bhaskar Sanap
#--------------------------------------------------------------------------------------

def main():
    TitanicLogistic("MarvellousTitanicDataset.csv")
    
if __name__ == "__main__":
    main()