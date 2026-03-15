import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

border = '-'*70

def MarvellousClassifier(Datapath):
    
    # Step 1 : Load the dataset from CSV file
    
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)
    
    df = pd.read_csv(Datapath)
    
    print(border)
    print("Some entries from CSV file")
    print(df.head())
    print(border)
    
    # Step 2 : Clean the Dataset by removing empty rowes
    
    print(border)
    print("Step 2 : Clean the Dataset by removing empty rows")
    print(border)
    
    df.dropna(inplace=True)
    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])
    print(border)
    
    # Step 3 : Separate independent and dependent varibales
    
    print(border)
    print("Step 3 : Separate independent and dependent varibales")
    print(border)
    
    X = df.drop(columns=['Class'])
    Y = df['Class']
    
    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)
    
    print(border)
    print("Input columns : ", X.columns.tolist())
    print("Output cloumns : Class")
    
    # Step 4 : Split the dataset for training and testing
    
    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
    
    print(border)
    print("Information of training and testing data")
    print("X_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ", Y_test.shape)
    print(border)
    
    # Step 5 : Feature Scaling 
    
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)
    
    scalar = StandardScaler()
    
    # Independent variable scaling
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    
    print("Feature scaling is done")
    
    # Step 6 : Explore multiple values of K
    # Hyperparameter tuning(K)
    
    print(border)
    print("Step 6 : Explore multiple values of K")
    print(border)
    
    accuracy_scores = []
    K_values = range(1, 21)
    
    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test, Y_pred)
        
        accuracy_scores.append(accuracy)
        
    print(border)
    print("Accuracy report of K values form 1 - 20: ")
    for value in accuracy_scores:
        print(value)
        
    print(border)

def main():
    print(border)
    print("Wine Classifier using KNN")
    print(border)
    
    MarvellousClassifier("WinePredictor.csv")
    
if __name__ == "__main__":
    main()