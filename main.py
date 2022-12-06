from sqlManagerLib import sqlManager

from flask import Flask, request

app = Flask(__name__)
db = sqlManager(server="localhost",
                database="cochesDb",
                username="Libreria",
                password="monkey1!")


@app.route("/")
def test():
    return "helloworld"


@app.route('/getOrders')
def getOrders():
    return list(db.Get5Orders())


# http://127.0.0.1:5000/insertOffice/?officeCode=12&city=yes&phone=051127&addressLine1=necochea2350&state=resistencia&country=argentina&postalCode=3500
@app.route('/insertOffice/')
def insertOffice():
    request.args.keys
    record = dict()
    record = request.args.to_dict()
    db.insertOffice(record)
    return f'Record {record} written.'


if __name__ == "__main__":
    app.run()
