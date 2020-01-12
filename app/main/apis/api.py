from flask import Blueprint, Flask
from flask_restplus import Api, Resource, fields, Model
import config
import modules.sheet_utils as sht
from model.models import Monthly, modelCall, Budget, Util
import json

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Budget Report',
          version='1.0',
          description='reporting tool')


@blueprint.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


service = sht.getSheetService()

monthly = Monthly(api)
budget = Budget(api)
util = Util(api)

ns_conf_budget = budget.getNameSpace()
ns_conf_util = util.getNameSpace()
ns_conf_monthly = monthly.getNameSpace()
# Models
monthly_model = monthly.getModel()
budget_model = budget.getModel()
util_model = util.getModel()


@ns_conf_budget.route("/" )
class Budget(Resource):
    @ns_conf_budget.doc('Budget')
    @ns_conf_budget.response(200, 'Success')
    @ns_conf_budget.marshal_with(budget_model, envelope='content')
    def get(self):
        """
        Contains data of budget
        """
        try:
            data = sht.getBudget(service)
            key = ['timeline', 'Parent Salary', 'child Salary', 'Utility Expenses', 'MonthlyLoan', 'Miscellaneous',
                   'Total', 'Balance', 'month', 'years']
            result = sht.to_son(data, key)
            print(result)
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
        """
        Contains data of utility sheet
        """
        try:
            data = sht.getUtility(service)
            key = ['timeline', 'Rent ', 'Maintenance', 'Internet Bill', 'Electricity Bill (Variable)',
                   'Food (Variable)', 'Miscellaneous', 'Monthly', 'month', 'years']
            result = sht.to_son(data, key)

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
    @ns_conf_monthly.response(200, 'Success', )
    # @api.response(400, 'Validation Error')
    # @ns_conf.expect(monthly_model)  ##use for validation purpose only
    def get(self):
        """
        Contains data of Monthly Loans sheet
        """
        try:
            data = sht.getMonthlyLoans(service)
            key = ['timeline', 'miscellaneous', "month", 'year']
            result = sht.to_son(data, key)
        except  Exception as e:
            print(e)
            data = '{[]}'
        return result

    def put(self):
        return 0
