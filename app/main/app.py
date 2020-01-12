import sys
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/main')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/modules')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/blueprint')
sys.path.insert(1, '/home/kid/Desktop/BudgetReport/app/apis')

from flask import Flask,request
from flask_restplus import Api,Resource
from apis.api import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run( port=5051,debug=True)