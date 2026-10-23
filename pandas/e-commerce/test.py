import os
import numpy as np
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
print(os.listdir(folder))
df = pd.read_csv("Ecommerce Purchases")
print(df.head())
print(df.shape)
df.info()

print(df["Purchase Price"].mean())

print(df["Purchase Price"].max())
print(df["Purchase Price"].min())

print((df["Language"] == "en").sum())

print((df["Job"] == "Lawyer").sum())

print(df["AM or PM"].value_counts())

print(df["Job"].value_counts().head(5))

print(df[df["Lot"] == "90 WT"]["Purchase Price"])

print(df[df["Credit Card"] == 4926535242672853]["Email"])

print(((df["CC Provider"] == "American Express") & (df["Purchase Price"] > 95)).sum())

print(df["CC Exp Date"].apply(lambda x: x[3:] == "25").sum())

print(df["Email"].apply(lambda x: x.split("@")[1]).value_counts().head(5))