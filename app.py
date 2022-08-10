from flask import Flask

app= Flask(__name__)

@app.route('/',methods = ['GET','POSt'])
def index():
    return 'starting machine learning project(CI CD pipeline)'


if __name__=='__main__':
    app.run(debug=True)