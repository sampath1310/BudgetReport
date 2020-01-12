from flask_restplus import Namespace, fields
from flask_restplus import Api


class modelCall:
    def __init__(self, api):
        self.api = api


class Monthly(modelCall):
    def __init__(self, api):
        super().__init__(api)
        self.namespace = self.api.namespace('monthlyloans', description='Monthly Loans operations')

    def getNameSpace(self):
        return self.namespace

    def getModel(self):
        model = self.namespace.model('monthly model', {
            'timeline': fields.String,
            'miscellaneous': fields.Integer,
            'month': fields.String,
            'year': fields.Integer
        })
        return model


class Budget(modelCall):
    def __init__(self, api):
        super().__init__(api)
        self.namespace = self.api.namespace('budget', description='Budget operations')

    def getNameSpace(self):
        return self.namespace

    def getModel(self):
        model = self.namespace.model('Budget model', {
            'timeline': fields.String,
            'Parent Salary': fields.Integer,
            'child Salary': fields.Integer,
            'Utility Expenses': fields.Integer,
            'MonthlyLoan': fields.Integer,
            'Miscellaneous': fields.Integer,
            'Total': fields.Integer,
            'Balance': fields.Integer,
            'month': fields.String,
            'years': fields.Integer})
        return model


class Util(modelCall):
    def __init__(self, api):
        super().__init__(api)
        self.namespace = self.api.namespace('utility', description='Utility operations')

    def getNameSpace(self):
        return self.namespace

    def getModel(self):
        model = self.namespace.model('Util model', {'timeline': fields.String,
                                                    'Rent ': fields.Integer,
                                                    'Maintenance': fields.Integer,
                                                    'Internet Bill': fields.Integer,
                                                    'Electricity Bill (Variable)': fields.Integer,
                                                    'Food (Variable)': fields.Integer,
                                                    'Miscellaneous': fields.Integer,
                                                    'Monthly': fields.Integer,
                                                    'month': fields.String,
                                                    'years': fields.Integer})

        return model
