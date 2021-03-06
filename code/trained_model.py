import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


data = pd.read_csv("data.csv")
data = data.drop('name',1)

#shuffle data
data = data.sample(frac=1).reset_index(drop=True)

x_train = data.drop(['malware'],1)
y_train = data['malware']


#over sampling
sm = SMOTE(random_state=12)
x_train_res, y_train_res = sm.fit_sample(x_train, y_train)

#logistic regression
logistic = LogisticRegression()

logistic.fit(x_train_res, y_train_res)
joblib.dump(logistic, 'trained_logistic.pkl', compress=9)