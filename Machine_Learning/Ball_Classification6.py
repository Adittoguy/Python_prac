# Steps For Machine Learning Application

# Step 1 : Data Gathering or Data Collection
# Step 2 : Data Analysis
# Step 3 : Data Cleaning
# Step 4 : Model Selection
# Step 5 : Model Training
# Step 6 : Model Testing / Evaluation
# Step 7 : Model Improvment(Model Tuning)
# Step 8 : Prediction / Deployment

from sklearn import tree

# Rough = 1
# Smooth = 0

# Circket = 2
# Tennis = 1

def main():
    print("Ball Classifcation case study")
    
    # Original Encoded dataset
    #  Independent Variable
    X = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0], [35, 1], [95, 0]]
    
    #  Dependent Variable
    Y = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]
    
    # Independent Variable for training
    Xtrain = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0]]
    
    # Independent Variable for testing
    Xtest =  [[35, 1], [95, 0]]
    
    # Dependent Variable for training
    Ytrain = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2]
    
    # Dependent Variable for testing
    Ytest =  [1, 2]
    
    modelobj = tree.DecisionTreeClassifier()
    
    trainedmodel = modelobj.fit(Xtrain, Ytrain)
    
    Result = trainedmodel.predict([[35, 1]])
    
    print(type(Result))
    
    if Result == 1:
        print("Object looks like tennis ball")
    elif Result == 2:
        print("Object looks like Cricket ball")
    
    print("Model predicts the object as : ", Result)
    
if __name__ == "__main__":
    main()
