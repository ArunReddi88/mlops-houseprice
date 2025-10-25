import pandas as pd

def prepare():
    input_path = 'data/raw/housing.csv'
    df = pd.read_csv(input_path)
    # Your data preparation code here

if __name__ == '__main__':
    prepare()

