import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

plt.rcParams["figure.figsize"] = (10, 5)
saved_style_state = matplotlib.rcParams.copy()

if os.path.isfile("Tesla_Dealth.csv"):
    filepath = "Tesla_Dealth.csv"
    print("loading from file")

else:
    filepath = "https://www.kaggle.com/datasets/thedevastator/tesla-accident-fatalities-analysis-and-statistic/data"
    print("loading from the internet")

penalty_data = pd.read_csv(filepath)
print("done")

penalty_data.head(1)


