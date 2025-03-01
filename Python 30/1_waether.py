import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ CSV फ़ाइल से डेटा लोड करें
df = pd.read_csv("C:\Cars_Dataset\waether.csv")  # पहले सुनिश्चित करें कि CSV फ़ाइल उपलब्ध हो

# 2️⃣ डेटा का अवलोकन करें
print(df.head())   # पहली 5 पंक्तियाँ देखें
print(df.info())   # डेटा की पूरी जानकारी

# 3️⃣ Missing Values को चेक करें और ठीक करें
print(df.isnull().sum())
df.fillna(method='ffill', inplace=True)  # Null वैल्यू को पिछले वैल्यू से भरें

# 4️⃣ बेसिक एनालिसिस करें
print("सबसे गर्म दिन:", df[df['Temperature'] == df['Temperature'].max()])
print("सबसे ठंडा दिन:", df[df['Temperature'] == df['Temperature'].min()])
print("औसत आर्द्रता (Humidity):", df['Humidity'].mean())

# 5️⃣ मौसम डेटा का विज़ुअलाइज़ेशन

# (A) तापमान परिवर्तन का ग्राफ 📈
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='r')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("तापमान परिवर्तन ग्राफ 🌡️")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# (B) आर्द्रता और तापमान के बीच संबंध 💦
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Temperature'], y=df['Humidity'])
plt.title("तापमान और आर्द्रता का संबंध")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.show()

# (C) वर्षा और हवा की गति 📊
plt.figure(figsize=(8,5))
sns.barplot(x=df['Rainfall'], y=df['Wind_Speed'], color='blue')
plt.title("वर्षा और हवा की गति का संबंध")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Wind Speed (km/h)")
plt.show()
