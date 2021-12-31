from employee import *
from flask import Flask
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
fh = logging.FileHandler("app.log")
fh.setFormatter(f)

logger.addHandler(fh)

#creating an instance of flask app
app = Flask(__name__)

#route to add employee
@app.route("/add_employee", methods=["POST"])
def add_employee():
    '''Function to add new employee to our database'''
    logger.debug("Adding new employee..")
    request_data = request.get_json() #getting data from client
    responce = Employee.add_employee(request_data, request.url)
    return responce

#route to show all employees
@app.route("/show_employee", methods=['GET'])
def show_all_employee():
    '''function to show employee data'''
    responce = Employee.get_all_employee()
    return responce

#route to show all employee with emp id
@app.route("/show_employee/<int:id>", methods=['GET'])
def show_employee(id):
    '''function to show employee data'''
    responce = Employee.get_employee(id)
    return responce

#route to update employee
@app.route("/update_employee", methods=["PUT"])
def update_employee():
    '''Function to update existing employee data to our database'''
    request_data = request.get_json() #getting data from client
    responce = Employee.update_employee(request_data, request.url)
    return responce

@app.route('/delete_employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    '''function to delete existing employee data from our database'''
    request_data = request.get_json()  # getting data from client
    responce = Employee.delete_employee(id, request.url)
    return responce

if __name__=="__main__":
    app.run(port=5000, debug=True)