import pandas as pd

# import os
# from dotenv import load_dotenv, dotenv_values 
# print(os.getenv("DATA_SET_PATH"))
dataFrame=pd.read_csv("data//iris-flower-data.csv")

print("Dataframes...\n",dataFrame)

print(dataFrame.describe())