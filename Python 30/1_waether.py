import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\Cars_Dataset\waether.csv")  

print(df.head())   
print(df.info())   


print(df.isnull().sum())
df.fillna(method='ffill', inplace=True) 

print("Hot Days:", df[df['Temperature'] == df['Temperature'].max()])
print("Cold Days:", df[df['Temperature'] == df['Temperature'].min()])
print("Avrage Humidity:", df['Humidity'].mean())


plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='r')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Graph")
plt.xticks(rotation=45)
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Temperature'], y=df['Humidity'])
plt.title("Tempreature or Humidity Relations")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=df['Rainfall'], y=df['Wind_Speed'], color='blue')
plt.title("Rain or Wind Speed Relations")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Wind Speed (km/h)")
plt.show()
