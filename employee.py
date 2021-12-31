import pymysql
from app import *
from db import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
fh = logging.FileHandler("employee.log")
fh.setFormatter(f)

logger.addHandler(fh)


def nofound(self,_request_url):
    message = {
        'status': 404,
        'message': 'Not Found: ' + _request_url,
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp

# the class Employee will create object for employee details
class Employee:

    def add_employee(_json,_request_url):
        conn = None
        cursor = None

        _emp_name = _json["emp_name"]
        _emp_desi = _json["emp_desi"]
        _emp_salary = _json["emp_salary"]
        _emp_mobile = _json["emp_mobile"]
        _emp_email = _json["emp_email"]

        try:
            # validate the received values
            if _emp_name and _emp_desi and _emp_salary and _emp_mobile and _emp_email and request.method == 'POST':
                # save edits
                sql = "INSERT INTO tbl_employee(emp_name,emp_desi,emp_salary,emp_mobile,emp_email) VALUES(%s, %s, %s , %s, %s)"
                data = (_emp_name, _emp_desi, _emp_salary, _emp_mobile, _emp_email,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('Employee added successfully!')
                logger.debug("New employee successfully added to database...")
                resp.status_code = 200
                return resp
            else:
                logger.critical("Issue with employee addition...")
                return nofound(_request_url)
        except Exception as e:
            logger.critical("Issue with employee addition...")
            print(e)
        finally:
            cursor.close()
            conn.close()

    def get_all_employee():
        conn = None
        cursor = None
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT emp_id Id,emp_name Name,emp_desi Designation,emp_salary Salary,emp_mobile Mobile,"
                           "emp_email Email FROM tbl_employee")
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            logger.debug("fetching employees from database...")
            return resp
        except Exception as e:
            logger.critical("Issue with fetching records from database...")
            print(e)
        finally:
            cursor.close()
            conn.close()

    def get_employee(_id):
        conn = None
        cursor = None
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT emp_id Id,emp_name Name,emp_desi Designation,emp_salary Salary,emp_mobile Mobile,"
                           "emp_email Email FROM tbl_employee where emp_id="+str(_id))
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            logger.debug("fetching specific employee from database...")
            return resp
        except Exception as e:
            logger.critical("Issue with fetching record from database...")
            print(e)
        finally:
            cursor.close()
            conn.close()

    def update_employee(_json,_request_url):
        conn = None
        cursor = None
        _emp_id = _json["emp_id"]
        _emp_name = _json["emp_name"]
        _emp_desi = _json["emp_desi"]
        _emp_salary = _json["emp_salary"]
        _emp_mobile = _json["emp_mobile"]
        _emp_email = _json["emp_email"]

        try:
            # validate the received values
            if _emp_name and _emp_desi and _emp_salary and _emp_mobile and _emp_email and request.method == 'PUT':
                # save edits
                sql = "Update tbl_employee SET emp_name=%s,emp_desi=%s,emp_salary=%s,emp_mobile=%s," \
                      "emp_email=%s where emp_id=%s"
                data = (_emp_name, _emp_desi, _emp_salary, _emp_mobile, _emp_email,_emp_id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('Employee updated successfully!')
                logger.debug("Employee successfully updated to database...")
                resp.status_code = 200
                return resp
            else:
                logger.critical("Issue with employee updating...")
                return nofound(_request_url)
        except Exception as e:
            logger.critical("Issue with employee updating...")
            print(e)
        finally:
            cursor.close()
            conn.close()

    def delete_employee(_id,_request_url):
        conn = None
        cursor = None
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tbl_employee WHERE emp_id=%s", (_id,))
            conn.commit()
            resp = jsonify('Employee deleted successfully!')
            resp.status_code = 200
            logger.debug("Employee successfully deleted from database...")
            return resp
        except Exception as e:
            logger.critical("Issue with employee deletion...")
            print(e)
        finally:
            cursor.close()
            conn.close()


