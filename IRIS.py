import pandas as pd
df = pd.read_csv("C:\\Users\\johns\\Desktop\\Study\\DS Training\\IRIS.csv", names = ["Sepal length (in cm)", "Sepal width (in cm)", "Petal length (in cm)", "Petal width (in cm)", "Class", "Sum"])
df = df[["Class", "Sepal length (in cm)", "Sepal width (in cm)", "Petal length (in cm)", "Petal width (in cm)", "Sum"]]
df["Sum"] = df["Sepal length (in cm)"]+ df["Sepal width (in cm)"] + df["Petal length (in cm)"] + df["Petal width (in cm)"]
df.shape
Iris_Setosa = df[(df['Class'] == 'Iris-setosa')]
Iris_Versicolour = df[(df['Class'] == 'Iris-versicolor')]
Iris_Virginica = df[(df['Class'] == 'Iris-virginica')]