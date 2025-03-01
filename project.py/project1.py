import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def select_file():
    root = Tk()
    root.withdraw()  # Hide Tkinter window
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx;*.xls")])
    return file_path
    
def load_data(file_path)
    df = pd.read_excel(file_path)
    print("\n🔹 Top 5 Lines of Data: \n", df.head())
    return df

def clean_data(df):
    df = df.dropna()  
    print("\n✅ Clean Data: \n", df.head())
    return df

def analyze_data(df):
    print("\n Tempratuer Acording to Colem: \n", df.describe())
    
    if 'Revenue' in df.columns:
        total_revenue = df['Revenue'].sum()
        print(f"\n Total Sales: {total_revenue}")

def visualize_data(df):
    if 'Category' in df.columns and 'Revenue' in df.columns:
        df.groupby('Category')['Revenue'].sum().plot(kind='bar', color='skyblue')
        plt.title(' Sales Acording to Category ')
        plt.xlabel('Category')
        plt.ylabel('Revenue')
        plt.show()
    else:
        print("⚠ In Data 'Category' or 'Revenue' Not in Colem")

if __name__ == "__main__":
    file_path = select_file()
    if file_path:
        df = load_data(file_path)
        df = clean_data(df)
        analyze_data(df)
        visualize_data(df)
    else:
        print("File Not Found")
