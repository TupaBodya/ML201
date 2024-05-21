import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

auto_df = pd.read_csv(".csv")
label_encoder = LabelEncoder()
auto_df["Type"] = label_encoder.fit_transform(auto_df["Type"])
X = auto_df.drop(["Type"], axis=1)
Y = auto_df["Type"]
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.3, random_state=3)
model = LogisticRegression()
model.fit(X_train1, Y_train1)
with open('AutoLogist', 'wb') as pkl:
    pickle.dump(model, pkl)
