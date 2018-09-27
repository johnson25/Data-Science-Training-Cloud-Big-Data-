#Importing Pandas library and defining a dataframe df to store the training set data:
import pandas as pd
df = pd.read_csv("C:\\Users\\johns\\Desktop\\Study\\DS Training\\train.csv")

#Filtering the training dataset with sex only female and age less than 40:
df_female40 = df[(df['Sex']== 'female') & (df['Age'] < 40)]
#Finding max, min and mean of their ages:
print("Max Female Age: ", df_female40['Age'].max())
print("Min Female Age: ", df_female40['Age'].min())
print("Mean Female Age: ", df_female40['Age'].mean())

#Filtering the training dataset with sex only male and age less than 40:
df_male40 = df[(df['Sex']== 'male') & (df['Age'] < 40)]
#Finding max, min and mean of their ages:
print("\nMax Male Age: ", df_male40['Age'].max())
print("Min Male Age: ", df_male40['Age'].min())
print("Mean Male Age: ", df_male40['Age'].mean())

#Filtering the training datset according to sex:
df_female = df[(df['Sex']=='female')]
df_male = df[(df['Sex']=='male')]

#Finding the count of people according to sex and embarkment port:
print("\nCount of females embarked at ports:\n",df_female['Embarked'].value_counts())
print("\nCount of males embarked at ports:\n",df_male['Embarked'].value_counts())

#Finding the count of people according to sex and pclass:
print("\nCount of females according to the Pclass:\n",df_female['Pclass'].value_counts())
print("\nCount of males according to the Pclass:\n",df_male['Pclass'].value_counts())