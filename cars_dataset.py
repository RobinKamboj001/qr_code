
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\Cars_Dataset\Brand,Model,Year,Mileage,Price,Fuel.txt")  # cars.csv 

print(df.head())   
print(df.info())   

print(df.isnull().sum())

df = df.fillna(df.mean())  

print("Total Cars:", df.shape[0])
print("Unik Brands:", df['Brand'].nunique())


plt.figure(figsize=(10,5))
sns.countplot(y=df['Brand'], order=df['Brand'].value_counts().index)
plt.title("Best Saling Brand")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Mileage'], y=df['Price'])
plt.title("Mileage vs Price")
plt.xlabel("Mileage (KMPL)")
plt.ylabel("Price (Lakhs)")
plt.show()
