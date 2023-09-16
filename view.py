from flask import request
from flask_restx import Namespace, Resource

from utils import Converter

api_ns = Namespace("api")


@api_ns.route('/rates')
class ConverterView(Resource):
    @staticmethod
    def get():
        from_exchange = request.args.get("from")
        to_exchange = request.args.get("to")
        value = request.args.get("value")

        if from_exchange and to_exchange and value:
            rates = Converter(from_exchange, to_exchange, value)
            result = rates.calculation()
            if type(result) == str:
                return result, 404
            else:
                return {"result": result}, 200
        else:
            return 'Недостаточно данных для конвертации', 418
