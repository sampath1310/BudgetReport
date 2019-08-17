import sys
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/main')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/modules')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/blueprint')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/apis')

from flask import Flask,request
from flask_restplus import Api,Resource
from  apis import blueprint as api


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api/1')

if __name__ == '__main__':
    app.run( port=5051,debug=True)