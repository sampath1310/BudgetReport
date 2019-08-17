from flask import Blueprint ,Flask
from flask_restplus import Api,Resource,fields
import  modules.sheet_utils as sht


blueprint = Blueprint('api', __name__)

api = Api(blueprint)

ns_conf = api.namespace('budget', description='Budget operations')
ns_conf_util = api.namespace('utility', description='Utility operations')
ns_conf_monthly =  api.namespace('monthlyloans', description='Monthly Loans operations')


service = sht.getSheetService() 




@ns_conf.route("/",)
class Budget(Resource):
    @ns_conf.doc('Budget')
    def get(self):
        '''
        Contains data of budget
        '''
        try:
            josn_result = sht.getBudget(service)
        except  Exception as e:
            print(e)
            josn_result = '{[]}'
        return josn_result
    def put(self):        
        return 0

@ns_conf_util.route("/")
class Utility(Resource):
    @ns_conf.doc('Utility')
    def get(self):
        '''
        Contains data of utility sheet
        '''
        try:
            josn_result = sht.getUtility(service)
        except  Exception as e:
            print(e)
            josn_result = '{[]}'
        return josn_result
    def put(self):        
        return 0

model_mon = api.model('Model', {
    'timeline': fields.String,
    'miscellaneous': fields.Integer,
    'month': fields.String,
    'year':fields.Integer
})



@ns_conf_monthly.route("/")
class MonthlyLoans(Resource):
    @api.marshal_with(model_mon, envelope='resource')
    @ns_conf.doc('Monthly')
    def get(self):
        '''
        Contains data of Monthly Loans sheet
        '''
        try:
            data = sht.getMonthlyLoans(service)
        except  Exception as e:
            print(e)
            data = '{[]}'
        key = ['timeline','miscellaneous',"month",'year']
        result = sht.to_son(data,key)        
        return result.to
    def put(self):        
        return 0