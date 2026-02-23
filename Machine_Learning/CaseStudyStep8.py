import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
                                accuracy_score, 
                                confusion_matrix,
                                classification_report,
                                ConfusionMatrixDisplay
                            )

Border = "-"*75

#------------------------------------------------------------------------------------#
#   Step 1 : Load the Dataset
#------------------------------------------------------------------------------------#

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets Loaded successfully...")
print("Initial entries from dataset : ")
print(df.head())

#------------------------------------------------------------------------------------#
#   Step 2 : Data Analysis (EDA) 
#------------------------------------------------------------------------------------#

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ", df.shape)
print("Column Names : ", list(df.columns))

print("Missing Values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species Count)")
print(df["species"].value_counts())

print("Statistical Report of Dataset")
print(df.describe())

#------------------------------------------------------------------------------------#
#   Step 3 : Decide Independent and Dependent Variables
#------------------------------------------------------------------------------------#

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X :   Independent Variables / Features
# Y :   Dependent Variables / Labels

feature_cols = [
                    "sepal length (cm)",
                    "sepal width (cm)",
                    "petal length (cm)",
                    "petal width (cm)"
                ]

X = df[feature_cols]
Y = df["species"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)

#------------------------------------------------------------------------------------#
#   Step 4 : Visualisation of Dataset
#------------------------------------------------------------------------------------#

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize=(7, 5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)
    
plt.title("Iris : Petal length vs Petal width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
# plt.show()

#------------------------------------------------------------------------------------#
#   Step 5 : Split the Dataset for training and testing
#------------------------------------------------------------------------------------#

print(Border)
print("Step 5 : Split the Dataset for training and testing")
print(Border)

# Test size = 20%
# Train size = 80%

X_train, X_test, Y_train, Y_test = train_test_split(
                                                        X,
                                                        Y,
                                                        test_size = 0.2,
                                                        random_state = 42
                                                    )

print("Data spliting Activity done : ")

print("X - Independent: ", X.shape) # (150, 4)
print("Y - Dependent: ", Y.shape)   # (150, )

print("X_train : ", X_train.shape)  # (120, 4)
print("X_test : ", X_test.shape)    # (30, 4)

print("Y_train : ", Y_train.shape)  # (120, )
print("Y_test : ", Y_test.shape)    # (30, )

#------------------------------------------------------------------------------------#
#   Step 6 : Build the Model
#------------------------------------------------------------------------------------#

print(Border)
print("Step 6 : Build the Model")
print(Border)

print("We are using DecisionTreeClassifier")

model = DecisionTreeClassifier  (
                                    criterion="gini",
                                    max_depth=3,
                                    random_state= 42
                                )

print("Model successfully created : ", model)

#------------------------------------------------------------------------------------#
#   Step 7 : Train the Model
#------------------------------------------------------------------------------------#

print(Border)
print("Step 7 : Train the Model")
print(Border)

model.fit(X_train, Y_train)

print("Model training completed")

#------------------------------------------------------------------------------------#
#   Step 8 : Evaluate the Model
#------------------------------------------------------------------------------------#

print(Border)
print("Step 8 : Evaluate the Model")
print(Border)

Y_pred = model.predict(X_test)

print("Model Evaluation(testing) complete")

print(Y_pred.shape)

print("Expected answers : ")
print(list(Y_test))

print("Predicted answers : ")
print(Y_pred)