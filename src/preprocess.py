import pandas as pd


def clean_data(df):

    df['MSRP'] = df['MSRP'].replace('[\\$,]', '', regex=True).astype(float)
    df['Invoice'] = df['Invoice'].replace('[\\$,]', '', regex=True).astype(float)

    df = df.dropna()

    return df
