#Importing Pandas library and defining a dataframe df to store the training set data:
import pandas as pd
df = pd.read_csv("C:\\Users\\johns\\Desktop\\Study\\DS Training\\train.csv")

#Filtering the training dataset with sex only female and age less than 40:
df_female40 = df[(df['Sex']== 'female') & (df['Age'] < 40)]
#Finding max, min and mean of their ages:
df_female40['Age'].max()
df_female40['Age'].min()
df_female40['Age'].mean()

#Filtering the training dataset with sex only male and age less than 40:
df_male40 = df[(df['Sex']== 'male') & (df['Age'] < 40)]
#Finding max, min and mean of their ages:
df_male40['Age'].max()
df_male40['Age'].min()
df_male40['Age'].mean()

#Filtering the training datset according to sex:
df_female = df[(df['Sex']=='female')]
df_male = df[(df['Sex']=='male')]

#Finding the count of people according to sex and embarkment port:
df_female['Embarked'].value_counts()
df_male['Embarked'].value_counts()

#Finding the count of people according to sex and pclass:
df_female['Pclass'].value_counts()
df_male['Pclass'].value_counts()