import pandas as pd

sal = pd.read_csv("Salaries.csv")

print(sal.head())

sal.info()

print(sal["BasePay"].mean())

print(sal["OvertimePay"].max())

print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"])

print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])

print(sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()])

print(sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()])

print(sal.groupby("Year")["BasePay"].mean())

print(sal["JobTitle"].nunique())

print(sal["JobTitle"].value_counts().head(5))

print((sal[sal["Year"] == 2013]["JobTitle"].value_counts() == 1).sum())

print(sal["JobTitle"].apply(lambda x: "chief" in x.lower().split()).sum())

sal["title_len"] = sal["JobTitle"].apply(len)
print(sal[["title_len", "TotalPayBenefits"]].corr())