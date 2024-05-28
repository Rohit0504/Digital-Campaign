# Import statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,ConfusionMatrixDisplay
import os
import flask
from flask import render_template, request, session
from flask import jsonify
import requests, json
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_session import Session
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from collections import Counter
import pickle


print("----Reading The Data----")
#file_path = 'newsData.txt'
data = pd.read_csv("Data/training_data.csv", nrows=10000)

print("----Initialize Vectorizer----")
# function to remove html elements from the reviews
def removeHTML(raw_text):
    clean_HTML = BeautifulSoup(raw_text, 'lxml').get_text() 
    return clean_HTML

# function to remove special characters and numbers from the reviews4961
def removeSpecialChar(raw_text):
    clean_SpecialChar = re.sub("[^a-zA-Z]", " ", raw_text)  
    return clean_SpecialChar

# function to convert all reviews into lower case
def toLowerCase(raw_text):
    clean_LowerCase = raw_text.lower().split()
    return( " ".join(clean_LowerCase)) 

# function to remove stop words from the reviews
def removeStopWords(raw_text):
    stops = set(stopwords.words("english"))
    words = [w for w in raw_text if not w in stops]
    return( " ".join(words))

model = pickle.load(open('Model/stack_election.pkl', 'rb'))

X = data['tweet']
Y = data['sentiment']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=30)

# X_training clean set
X_train_cleaned = []


for val in X_train:
    val = removeHTML(val)
    val = removeSpecialChar(val)
    val = toLowerCase(val)
    X_train_cleaned.append(val) 
    
# X_testing clean set
X_test_cleaned = []

for val in X_test:
    val = removeHTML(val)
    val = removeSpecialChar(val)
    val = toLowerCase(val)
    X_test_cleaned.append(val) 
    

tvec = TfidfVectorizer(use_idf=True,
strip_accents='ascii')

X_train_tvec = tvec.fit_transform(X_train_cleaned)

lr = LogisticRegression()
lr.fit(X_train_tvec, Y_train)

print("----Initializing The Flask Application----")
app = flask.Flask(__name__, template_folder='Templates')

print("----Database Connection----")
#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
app.config['MYSQL_DB'] = 'tweetapp'#database name

mysql = MySQL(app)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
    
@app.route('/tweetpage', methods=['GET', 'POST'])
def tweetpage():
    if flask.request.method == 'GET':
        return(flask.render_template('tweetpage.html'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if flask.request.method == 'GET':
        return(flask.render_template('admin.html'))
    
@app.route('/fullnews', methods=['GET', 'POST'])
def fullnews():
    if flask.request.method == 'GET':
        return(flask.render_template('fullnews.html'))
    
@app.route('/newshistory', methods=['GET', 'POST'])
def newshistory():
    if flask.request.method == 'GET':
        return(flask.render_template('newshistory.html'))
    
@app.route('/updatenews', methods=['GET', 'POST'])
def updatenews():
    
    return jsonify("res")


#User Login   
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return(flask.render_template('login.html'))
    if flask.request.method == 'POST':
        msg=''
        if request.method == 'POST':
            phone    = request.form['phone']
            password = request.form['password']

            con = mysql.connect
            con.autocommit(True)
            cursor = con.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user_details WHERE phone = % s and password = %s', (phone, password,))
            result = cursor.fetchone()
            
         
        if result:
            msg = "1"
            session["userid"]   = result["user_id"]
        else:
           msg = "0"
    return msg
       
@app.route('/registeruser', methods=['GET', 'POST'])
def registeruser():
    if flask.request.method == 'GET':
        return(flask.render_template('register.html'))
    if flask.request.method == 'POST':
        msg=''
        #applying empty validation
        if request.method == 'POST':
            
            uname       = request.form['uname']
            email       = request.form['email']
            phone       = request.form['phone']
            password    = request.form['password']
            
            con = mysql.connect
            con.autocommit(True)
            cursor = con.cursor(MySQLdb.cursors.DictCursor)
            result = cursor.execute('INSERT INTO user_details VALUES (NULL, % s, % s, % s, % s, NULL)', (uname, email, phone, password,))
            mysql.connect.commit()

            #displaying message
            msg = '1'
    return msg

@app.route('/getnews', methods=['GET', 'POST'])
def getnews():
    search           = request.form['search']
    """con = mysql.connect
    con.autocommit(True)
    cursor = con.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tweet_detail')
    result = cursor.fetchall()"""
    
    url = f"https://tweetcracks.000webhostapp.com/?search={search}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    
    return jsonify(data)

@app.route('/filternews', methods=['GET', 'POST'])
def filternews():
    search      = request.form['search']
    con = mysql.connect
    con.autocommit(True)
    cursor = con.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM tweet_detail WHERE tweet_content LIKE '%" + search + "%'")
    result = cursor.fetchall()
    
    return jsonify(result)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze(sentiment):
    sentimentdt = [str(sentiment)]
    prediction = lr.predict(tvec.transform(sentimentdt))[0]
    
    return prediction
    
@app.route('/gettweet', methods=['GET', 'POST'])
def gettweet():
    tweetid       = request.form['tweetid']  
    url = 'https://tweetcracks.000webhostapp.com/getbytweetid.php?tweetid='+tweetid
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    #print(data)    
    tweet_analyze = analyze(data[0]["tweet_content"])
    
    url = 'https://tweetcracks.000webhostapp.com/gettweetcomments.php?tweetid='+tweetid
    #print(url)
    response = requests.get(url)
    if response.status_code == 200:
        result1 = response.json()
        
    comment_analyze = []
    for i in range (len(result1)):
        pred = analyze(result1[i]["comment"])
        comment_analyze.append(pred)
    
    sentiment_counts = Counter(comment_analyze)
    sentiments = list(sentiment_counts.keys())
    occurrences = list(sentiment_counts.values())
    
    plt.figure(figsize=(8, 8))
    plt.pie(occurrences, labels=sentiments, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Campaign Analysis')
    plt.savefig('Static/senchart.png')
    
    plt.show()  
    out = {"tweet":data, "comments":result1, "tweet_analyze":tweet_analyze, "comment_analyze":comment_analyze}
    return jsonify(out)

@app.route('/gethistory', methods=['GET', 'POST'])
def gethistory():
    userid       = str(session.get("userid"))
    
    return jsonify(userid)

@app.route('/updatehistory', methods=['GET', 'POST'])
def updatehistory():
    if flask.request.method == 'POST':
        title       = request.form['title']   
        
    
    return jsonify(title)



if __name__ == '__main__':
    app.run(debug=False)