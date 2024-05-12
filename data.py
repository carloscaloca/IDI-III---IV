# -*- coding: utf-8 -*-
"""data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VVyG20EzLiP3Kl8C4bulpIXtxkv9WCtV
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import plotly.graph_objects as go
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, roc_auc_score
from sklearn.neural_network import MLPClassifier

ruta = '/content/drive/MyDrive/TOG/IDI III/Datos/'
df = pd.read_excel(ruta+"datos_klines.xlsx")