from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask.ext.mysql import MySQL

app = Flask(__name__)
api = Api(app)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database_name'
app.config['MYSQL_DATABASE_HOST'] = 'server_location'
mysql.init_app(app)

class GetData(Resource):

    def get(self):
        try:
            # Parsing arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username')
            parser.add_argument('password')
            args = parser.parse_args()

            # extracting arguments
            _username = args['username']
            _password = args['password']

            # Creating connection
            conn = mysql.connect()
            cursor = conn.cursor()

            if _username is not None:
                cursor.execute("SELECT * FROM Alumni WHERE BINARY username = '" + _username + "' and password = '"
                           + _password + "'")
                data = cursor.fetchall()
            else:
                cursor.execute("SELECT * FROM Alumni")
                data = cursor.fetchall()

            if data is None:
                return {'INFO': 'NO DATA FOUND'}
            else:
                return {'DATA': data}

        except Exception as e:
            return {'ERROR': str(e)}


class PutData(Resource):

    def post(self):
        try:
            # parsing arguments
            parsor = reqparse.RequestParser()
            parsor.add_argument('username')
            parsor.add_argument('password')
            parsor.add_argument('job')
            parsor.add_argument('company')
            args = parsor.parse_args()

            # extract arguments
            _username = args['username']
            _password = args['password']
            _job = args['job']
            _company = args['company']

            # Creating database connection
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Alumni(username, password, job, company) VALUES (%s, %s, %s, %s)",
                           (_username, _password, _job, _company))
            conn.commit()

            return GetData().get()

        except Exception as e:
            return {'ERROR': str(e)}

api.add_resource(GetData, '/data')
api.add_resource(PutData, '/data')

if __name__ == '__main__':
    app.run(debug=True)
