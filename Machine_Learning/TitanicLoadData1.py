import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

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