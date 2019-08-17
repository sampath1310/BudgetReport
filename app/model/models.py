from flask_restplus import Namespace, fields


class Monthly:
    api = Namespace('monthlyloans', description='Monthly Loans operations')


    monthly_model = api.model('monthly model', {
        'timeline': fields.String,
        'miscellaneous': fields.Integer,
        'month': fields.String,
        'year':fields.Integer
    })
