import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


df = pd.read_csv('AAPL.csv', index_col="Date", parse_dates=True)
df = df[['Adj Close']]

forecast = 30
df['Prediction'] = df[['Adj Close']].shift(-forecast)

X = np.array(df.drop(['Prediction'],1))
X = X[:-forecast]

y = np.array(df['Prediction'])
y = y[:-forecast]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size =0.2)


#Support Vector Regressor
svr = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr.fit(x_train, y_train)

svr_confidence = svr.score(x_test, y_test)
#print('Support Vector Regression Confidence: ', svr_confidence)


#Linear Regressor
linreg = LinearRegression()
linreg.fit(x_train, y_train)

linreg_confidence = linreg.score(x_test, y_test)
#print('Linear Regression Confidence: ', linreg_confidence)

x_forecast = np.array(df.drop(['Prediction'],1 ))[-forecast:]

def svr_pred():
    #print('Support Vector Regression prediction:')
    svm_prediction = svr.predict(x_forecast)
    return svm_prediction


def linreg_pred():
    #print('Linear Regression prediction:')
    linreg_prediction = linreg.predict(x_forecast)
    return linreg_prediction


print("Support vector regression prediction:" + str(svr_pred()))
print("Accuracy:" + str(svr_confidence))


print("Linear regression prediction:" + str(linreg_pred()))
print("Accuracy:" + str(linreg_confidence))


sys.stdout.flush()