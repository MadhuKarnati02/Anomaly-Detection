from __future__ import print_function
import os
import pandas as pandas
import csv
import pandas as pd
import numpy as np
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error)
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error, roc_curve, classification_report,auc)
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect,  admin_loginact,emp_reg,v_response,respond_act, emp_loginact,viewrequest,userrequest_act
from database import reqact,view_emp,requestact
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)

traindata = pd.read_csv('kddtrain.csv', header=None)
testdata = pd.read_csv('kddtest.csv', header=None)

X = traindata.iloc[:,1:42]
Y = traindata.iloc[:,0]
C = testdata.iloc[:,0]
T = testdata.iloc[:,1:42]

scaler = Normalizer().fit(X)
trainX = scaler.transform(X)

scaler = Normalizer().fit(T)
testT = scaler.transform(T)


traindata = np.array(trainX)
trainlabel = np.array(Y)

testdata = np.array(testT)
testlabel = np.array(C)

@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/employee")
def employee():
    return render_template("employee.html")




@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")

@app.route("/userhome")
def userhome():
    return render_template("userhome.html")



@app.route("/viewreq")
def viewrequest1():
    data = viewrequest()
    return render_template("viewreq.html",req=data)

@app.route("/respond")
def respond():
    empid = request.args.get('empid')
    reqid  = request.args.get('reqid')
    data = v_response(empid,reqid)
    return render_template("viewreq1.html",res=data)

@app.route("/analyze")
def analyze():
    return render_template("analyze.html")

@app.route("/view")
def view():
    data=pandas.read_csv("C:\\Users\\dell\\Documents\\Python\\BAT\\KDDTest+_2.csv")
    peek=data.head(30)
    return render_template("analyze1.html",tables=[peek.to_html(classes='data')])

@app.route("/preprocess")
def preprocess():
    traindata = pd.read_csv('kdd/binary/Training.csv', header=None)
    testdata = pd.read_csv('kdd/binary/Testing.csv', header=None)

    X = traindata.iloc[:,1:42]

    Y = traindata.iloc[:,0]
    C = testdata.iloc[:,0]
    T = testdata.iloc[:,1:42]

    x=  X[0:10]
    
    print(x)
    print(Y[0:5])
    
    

    return render_template("preprocess.html",tables=[x.to_html(classes='data')])

@app.route("/lr")
def lr():
    model = LogisticRegression()
    model.fit(traindata, trainlabel)

    # make predictions
    expected = testlabel
    np.savetxt('classical/expected.txt', expected, fmt='%01d')
    predicted = model.predict(testdata)
    proba = model.predict_proba(testdata)

    np.savetxt('classical/predictedlabelLR.txt', predicted, fmt='%01d')
    np.savetxt('classical/predictedprobaLR.txt', proba)

    y_train1 = expected
    y_pred = predicted
    accuracy = accuracy_score(y_train1, y_pred)
    recall = recall_score(y_train1, y_pred , average="binary")
    precision = precision_score(y_train1, y_pred , average="binary")
    f1 = f1_score(y_train1, y_pred, average="binary")

    print("accuracy")
    print("%.3f" %accuracy)
    print("precision")
    print("%.3f" %precision)
    print("racall")
    print("%.3f" %recall)
    print("f1score")
    print("%.3f" %f1)

    return render_template("predicted.html",accuracy=accuracy,precision=precision,recall=recall,f1=f1)

@app.route("/request")
def request5():
    return render_template("request.html")
# -------------------------------Registration-----------------------------------------------------------------    
@app.route("/empreg", methods = ['GET','POST'])
def userreg():
   if request.method == 'POST':      
      status = emp_reg(request.form['username'],request.form['password'],request.form['dob'],request.form['mobile'],request.form['email'])
      if status == 1:
       return render_template("employee.html",m1="sucess")
      else:
       return render_template("empreg.html",m1="failed")






@app.route("/responded", methods = ['GET','POST'])
def request7():
   if request.method == 'POST':      
      status = respond_act(request.form['reqid'],request.form['res'])
      if status == 1:
       return render_template("adminhome.html",m1="sucess")
      else:
       return render_template("viewreq.html",m1="failed")
# -------------------------------Registration End-----------------------------------------------------------------
# -------------------------------Loginact-----------------------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])       
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

@app.route("/emplogact", methods=['GET', 'POST'])       
def emplogact():
        if request.method == 'POST':
           status = emp_loginact(request.form['username'], request.form['password'])
           print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("emphome.html", m1="sucess")
        else:
            return render_template("employee.html", m1="Login Failed")


# -------------------------------Loginact End-----------------------------------------------------------------

@app.route("/requestact", methods = ['GET','POST'])
def requestact():
   if request.method == 'POST':  
      user = session['username']    
      status = reqact(request.form['request'],user)
      if status == 1:
       return render_template("request.html",m1="sucess")
      else:
       return render_template("request.html",m1="failed")








@app.route("/viewres")
def response():
    data = view_response()
    print(data)
    return render_template("response.html", res = data)


@app.route("/viewemp")
def viewemp():
    data = view_emp()
    print(data)
    return render_template("viewemp.html", empdetails = data)

@app.route("/userviewrequest")
def userviewrequest():
    data = userrequest_act()
    print(data)
    return render_template("userviewrequest.html", request = data)


   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
