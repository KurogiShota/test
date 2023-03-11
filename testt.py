#test
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("test.csv")
df = df.fillna(0)

print(df.loc[0])
df = pd.DataFrame([0,1,2,3,5])
print("ok")

a= np.zeros((3,3))

print(a)



