#import dependencies and packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)


def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df