df = pd.DataFrame({"Study_Mode":["Online","Classroom","Online"]})
encoded = pd.get_dummies(df,columns=["Study_Mode"],dtype=int)
print(encoded)