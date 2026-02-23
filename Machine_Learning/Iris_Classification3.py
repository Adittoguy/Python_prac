from sklearn.datasets import load_iris

def main():
    print("Iris Classifcation case study")
    
    Dataset = load_iris()
   
    # Metadata of dataset 
    print("Independent Variables are : ")
    print(Dataset.feature_names)
    
    print("Length of Independent variables is : ", len(Dataset.feature_names))
    
    print("Dependent Variables are : ")
    print(Dataset.target_names)
    
    print("Length of Dependent variables is : ", len(Dataset.target_names))
        
if __name__ == "__main__":
    main()
