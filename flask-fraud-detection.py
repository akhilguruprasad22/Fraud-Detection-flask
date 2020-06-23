from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello"

@app.route('/<string:a>/', methods=['GET'])
def Return(a):
  return a+' Success.'

if __name__=='__main__':
  app.run()
