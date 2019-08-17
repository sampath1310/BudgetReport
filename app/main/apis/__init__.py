from flask import Blueprint ,Flask
from flask_restplus import Api,Resource,fields,Model

import  modules.sheet_utils as sht
from model.models import Monthly


blueprint = Blueprint('api', __name__)

api = Api(blueprint)

ns_conf_budget = api.namespace('budget', description='Budget operations')
ns_conf_util = api.namespace('utility', description='Utility operations')
ns_conf_monthly =   api.namespace('monthlyloans', description='Monthly Loans operations')

service = sht.getSheetService() 

#Models
monthly_model = ns_conf_monthly.model('Monthly', {
    'timeline': fields.String,
    'miscellaneous': fields.Integer,
    'month': fields.String,
    'year':fields.Integer
})
budget_model = ns_conf_budget.model('Budget model',{
    'timeline':fields.String,
    'Parent Salary':fields.Integer,
    'child Salary':fields.Integer, 
    'Utility Expenses':fields.Integer,
    'MonthlyLoan':fields.Integer,
    'Miscellaneous':fields.Integer,
    'Total':fields.Integer,
    'Balance':fields.Integer,
    'month':fields.String,
    'years':fields.Integer})

util_model = ns_conf_util.model('Budget model',{'timeline':fields.String,
    'Rent ':fields.Integer,
    'Maintenance':fields.Integer,
    'Internet Bill':fields.Integer,
    'Electricity Bill (Variable)':fields.Integer,
    'Food (Variable)':fields.Integer,
    'Miscellaneous':fields.Integer,
    'Monthly':fields.Integer,
    'month':fields.String,
    'years':fields.Integer})

@ns_conf_budget.route("/",)
class Budget(Resource):
    @ns_conf_budget.doc('Budget')
    @ns_conf_budget.response(200, 'Success')
    @ns_conf_budget.marshal_with(budget_model, envelope='content')
    def get(self):
        '''
        Contains data of budget
        '''
        try:
            data = sht.getBudget(service)
            key = ['timeline', 'Parent Salary', 'child Salary', 'Utility Expenses', 'MonthlyLoan', 'Miscellaneous', 'Total', 'Balance','month','years']
            result = sht.to_son(data,key)
        except  Exception as e:
            print(e)
            result = '{[]}'
        return result
    def put(self):        
        return 0

@ns_conf_util.route("/")
class Utility(Resource):
    @ns_conf_util.doc('Utility')
    @ns_conf_util.response(200, 'Success')
    @ns_conf_util.marshal_with(util_model, envelope='content')
    def get(self):
        '''
        Contains data of utility sheet
        '''
        try:
            data = sht.getUtility(service)
            key = ['timeline', 'Rent ', 'Maintenance', 'Internet Bill', 'Electricity Bill (Variable)', 'Food (Variable)', 'Miscellaneous', 'Monthly','month','years']
            result = sht.to_son(data,key)
        except  Exception as e:
            print(e)
            result = '{[]}'
        return result
    def put(self):        
        return 0


@ns_conf_monthly.route("/")
class MonthlyLoans(Resource):
    @ns_conf_monthly.marshal_with(monthly_model, envelope='content')
    @ns_conf_monthly.doc(monthly_model)
    @ns_conf_monthly.response(200, 'Success')
    #@api.response(400, 'Validation Error')
    #@ns_conf.expect(monthly_model)  ##use for validation purpose only
    def get(self):
        '''
        Contains data of Monthly Loans sheet
        '''
        try:
            data = sht.getMonthlyLoans(service)
            key = ['timeline','miscellaneous',"month",'year']
            result = sht.to_son(data,key)
        except  Exception as e:
            print(e)
            data = '{[]}'                
        return result
    def put(self):        
        return 0