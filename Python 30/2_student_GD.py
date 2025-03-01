import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\Cars_Dataset\student.csv")  


print(df.head()) 
print(df.info())   


print(df.isnull().sum())
df.fillna(df['Grade'].mean(), inplace=True)  


print("Higest Marks Student:", df[df['Grade'] == df['Grade'].max()])
print("Lowest Marks Student:", df[df['Grade'] == df['Grade'].min()])
print("Avrage Grade:", df['Grade'].mean())


plt.figure(figsize=(8,5))
sns.histplot(df['Grade'], bins=10, kde=True, color='blue')
plt.title("Student Grades Analysis")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(x=df['Subject'], y=df['Grade'])
plt.title("Perfomens")
plt.xlabel("Subjects")
plt.ylabel("Grades")
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df['Student_Name'], df['Grade'], marker='o', linestyle='-', color='green')
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Grades")
plt.title("Student Grade Trand")
plt.show()
