from flask_restful import Resource, reqparse

class ControllerBase(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('autorization', required=False, type=str, location='headers')
