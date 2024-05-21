import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

auto_df = pd.read_csv("autos.csv")
label_encoder = LabelEncoder()
auto_df["Type"] = label_encoder.fit_transform(auto_df["Type"])
X = auto_df.drop(["Type"], axis=1)
Y = auto_df["Type"]
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.3, random_state=3)
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X_train1, Y_train1)
tree.plot_tree(model, class_names=True)
class_names = auto_df['Type']
tree.plot_tree(model, class_names=class_names)
with open('AutoDerevo.pkl', 'wb') as pkl:
    pickle.dump(model, pkl)
