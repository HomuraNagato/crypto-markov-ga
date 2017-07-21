#mod-1-lecture-notes.py

from sklearn import linear_model # Imports the model library

df = df.get_dummies() # Convert categorical to dummy

X = df2[['a', 'b']].as_matrix() # get features into numpy array
Y = df2.label.as_matrix().ravel() # 1-D label array

lg = linear_model.LogisticRegression(arguments) # Defines model
logr = lg.fit(X, Y) # fits model
score = logr.predict_log_proba(X) # computes scored label