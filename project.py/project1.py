import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# ----- Step 1: एक्सेल फाइल चुनें -----
def select_file():
    root = Tk()
    root.withdraw()  # Hide Tkinter window
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx;*.xls")])
    return file_path

# ----- Step 2: डेटा लोड करें -----
def load_data(file_path):
    df = pd.read_excel(file_path)
    print("\n🔹 डेटा का पहला 5 पंक्तियाँ: \n", df.head())
    return df

# ----- Step 3: डेटा क्लीनिंग -----
def clean_data(df):
    df = df.dropna()  # खाली डेटा हटाएँ
    print("\n✅ क्लीन डेटा: \n", df.head())
    return df

# ----- Step 4: डेटा एनालिसिस -----
def analyze_data(df):
    print("\n📊 कॉलम के हिसाब से समरी: \n", df.describe())
    
    # कुल बिक्री निकालें
    if 'Revenue' in df.columns:
        total_revenue = df['Revenue'].sum()
        print(f"\n💰 कुल बिक्री: {total_revenue}")

# ----- Step 5: डेटा विज़ुअलाइज़ेशन -----
def visualize_data(df):
    if 'Category' in df.columns and 'Revenue' in df.columns:
        df.groupby('Category')['Revenue'].sum().plot(kind='bar', color='skyblue')
        plt.title('📊 कैटेगरी के हिसाब से बिक्री')
        plt.xlabel('Category')
        plt.ylabel('Revenue')
        plt.show()
    else:
        print("⚠ डेटा में 'Category' या 'Revenue' कॉलम नहीं है!")

# ----- Main Function -----
if __name__ == "__main__":
    file_path = select_file()
    if file_path:
        df = load_data(file_path)
        df = clean_data(df)
        analyze_data(df)
        visualize_data(df)
    else:
        print("❌ कोई फाइल चयनित नहीं की गई!")
