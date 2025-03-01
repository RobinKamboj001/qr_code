import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ CSV फ़ाइल से डेटा लोड करें
df = pd.read_csv("C:\Cars_Dataset\student.csv")  # पहले सुनिश्चित करें कि CSV फ़ाइल उपलब्ध हो

# 2️⃣ डेटा का अवलोकन करें
print(df.head())   # पहली 5 पंक्तियाँ देखें
print(df.info())   # डेटा की पूरी जानकारी

# 3️⃣ Missing Values को चेक करें और ठीक करें
print(df.isnull().sum())
df.fillna(df['Grade'].mean(), inplace=True)  # Missing values को Mean से भरें

# 4️⃣ बेसिक एनालिसिस करें
print("सबसे अधिक अंक प्राप्त करने वाला छात्र:", df[df['Grade'] == df['Grade'].max()])
print("सबसे कम अंक प्राप्त करने वाला छात्र:", df[df['Grade'] == df['Grade'].min()])
print("कक्षा का औसत ग्रेड:", df['Grade'].mean())

# 5️⃣ स्टूडेंट ग्रेड का विज़ुअलाइज़ेशन

# (A) सभी छात्रों के ग्रेड का वितरण 📊
plt.figure(figsize=(8,5))
sns.histplot(df['Grade'], bins=10, kde=True, color='blue')
plt.title("स्टूडेंट ग्रेड का वितरण")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()

# (B) विषयवार प्रदर्शन ग्राफ़ 📖
plt.figure(figsize=(10,5))
sns.boxplot(x=df['Subject'], y=df['Grade'])
plt.title("विषयवार प्रदर्शन")
plt.xlabel("Subjects")
plt.ylabel("Grades")
plt.show()

# (C) स्टूडेंट्स के ग्रेड का ट्रेंड 📈
plt.figure(figsize=(10,5))
plt.plot(df['Student_Name'], df['Grade'], marker='o', linestyle='-', color='green')
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Grades")
plt.title("स्टूडेंट्स के ग्रेड का ट्रेंड")
plt.show()
