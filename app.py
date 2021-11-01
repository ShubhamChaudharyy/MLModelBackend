import os
import pyrebase 
from flask import Flask

app = Flask(__name__)

config = {
  "apiKey": "AIzaSyA361PtSQdAUABwHBCJmuVTdOVD4o0N7i8",
  "authDomain": "minorproj-d3dae.firebaseapp.com",
  "databaseURL": "https://minorproj-d3dae-default-rtdb.firebaseio.com",
  "projectId": "minorproj-d3dae",
  "storageBucket": "minorproj-d3dae.appspot.com",
  "messagingSenderId": "94044198270",
  "appId": "1:94044198270:web:9b2ae70fe75b1eac284f2f",
  "measurementId": "G-K8FF7T5NC8"
}

firebase = pyrebase.initialize_app(config); 

db = firebase.database()
storage = firebase.storage()

@app.route('/run-model/get/<id>/<format>',methods=['GET','POST'])
def getFile(id,format): 
  my_image = str(id)+'.' + format
  storage.child("reports/"+my_image).download(filename="model."+format)

if __name__ == "__main__":
  app.run(debug=True)