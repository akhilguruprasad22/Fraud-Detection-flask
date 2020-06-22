from flask import Flask

app = Flask(__name__)

@app.route('/<string:a>/', methods=['POST'])
def Return(a):
  return a+' Success.'

if __name__=='__main__':
  app.run()
