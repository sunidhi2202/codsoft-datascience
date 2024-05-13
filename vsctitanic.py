import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data_titanic = pd.read_csv(r"C:\Users\dines\Downloads\test.csv")
data_titanic.head()
data_titanic.shape