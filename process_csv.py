import pandas as pd

def process_csv(path):
    full_path = "r'" + path + "'"
    data = pd.read_csv(full_path)
    print(data)

if __name__ == "__main__":
    path = "C:\Users\torrjond\Desktop\chords.csv"
    process_csv(path)
