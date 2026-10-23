import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

titanic = sns.load_dataset("titanic")

print(titanic.head())
print(titanic.isnull().sum())

plt.figure(figsize=(10, 6))
sns.histplot(titanic["age"].dropna(), bins=30, kde=True)
plt.title("Distribution of Passengers' Ages")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(titanic["age"].dropna(), bins=30, kde=True, ax=axes[0])
axes[0].set_title("Distribution of Age")
sns.histplot(titanic["fare"], bins=30, kde=True, ax=axes[1])
axes[1].set_title("Distribution of Fare")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic, x="age", y="fare")
plt.title("Age vs Fare")
plt.show()

plt.figure(figsize=(10, 6))
sns.stripplot(data=titanic, x="survived", y="age", jitter=True, alpha=0.6)
plt.title("Survived vs Age")
plt.show()

print("Male survival rate:  ", titanic[titanic["sex"] == "male"]["survived"].mean())
print("Female survival rate:", titanic[titanic["sex"] == "female"]["survived"].mean())

plt.figure(figsize=(10, 6))
sns.barplot(data=titanic, x="sex", y="survived", errorbar=None)
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=titanic, x="pclass", y="survived", errorbar=None)
plt.title("Survival Rate by Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

bins = [0, 12, 18, 35, 60, 80]
labels = ["Child", "Teen", "Adult", "Middle-Aged", "Senior"]
titanic["age_group"] = pd.cut(titanic["age"], bins=bins, labels=labels)
print(titanic["age_group"].head())

plt.figure(figsize=(10, 6))
sns.barplot(data=titanic, x="age_group", y="survived", errorbar=None)
plt.title("Survival Rate by Age Group")
plt.ylabel("Survival Rate")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=titanic, x="embarked", y="survived", hue="sex", errorbar=None)
plt.title("Survival Rate by Embarkation Point and Sex")
plt.ylabel("Survival Rate")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x="pclass", hue="sex")
plt.title("Passengers by Class and Sex")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x="class", hue="who")
plt.title("Passengers by Class and Who")
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(data=titanic, x="class", hue="sex")
plt.title("Males and Females Across Classes")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=titanic, x="embark_town", y="survived", errorbar=None)
plt.title("Survival Rate by Embarkation Port")
plt.ylabel("Survival Rate")
plt.show()

numeric_cols = titanic.select_dtypes(include=[np.number])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic, x="sex", y="fare", hue="survived")
plt.title("Fare by Gender and Survival Status")
plt.show()

plt.figure(figsize=(8, 6))
sns.pointplot(data=titanic, x="pclass", y="survived", hue="sex", errorbar=None)
plt.title("Survival Rate by Class and Gender")
plt.ylabel("Survival Rate")
plt.show()