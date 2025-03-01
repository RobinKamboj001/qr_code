# आवश्यक लाइब्रेरी इंपोर्ट करें
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CSV फाइल से डेटा लोड करें
df = pd.read_csv("C:\Cars_Dataset\Brand,Model,Year,Mileage,Price,Fuel.txt")  # पहले सुनिश्चित करें कि cars.csv फ़ाइल उपलब्ध हो

# 2. डेटा का अवलोकन करें
print(df.head())   # पहली 5 पंक्तियाँ देखें
print(df.info())   # डेटा की पूरी जानकारी

# 3. Missing Values को चेक करें
print(df.isnull().sum())

# 4. डेटा क्लीनिंग (Missing Values को भरना)
df = df.fillna(df.mean())  # Numerical data के लिए mean से भरना

# 5. कुछ बेसिक विश्लेषण करें
print("कुल कारों की संख्या:", df.shape[0])
print("यूनिक ब्रांड्स:", df['Brand'].nunique())

# 6. डेटा का विज़ुअलाइज़ेशन

# (A) सबसे ज्यादा बिकने वाले ब्रांड्स
plt.figure(figsize=(10,5))
sns.countplot(y=df['Brand'], order=df['Brand'].value_counts().index)
plt.title("सबसे ज्यादा बिकने वाले कार ब्रांड्स")
plt.show()

# (B) माइलेज और प्राइस के बीच संबंध
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Mileage'], y=df['Price'])
plt.title("Mileage vs Price")
plt.xlabel("Mileage (KMPL)")
plt.ylabel("Price (Lakhs)")
plt.show()
