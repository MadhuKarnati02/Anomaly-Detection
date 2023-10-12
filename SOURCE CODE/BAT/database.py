import sqlite3
import hashlib
import datetime
import MySQLdb

from flask import session
from random import randint

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="networkintrusion")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------



def emp_reg(username, password,  dob,mobile, email):
    try:
        c, conn = db_connect()
        print(username, password,  dob,mobile, email)
        
        id="0"
        j = c.execute("insert into user (id,username, password,  dob,mobile, email) values ('"+id+"','"+username +
                      "','"+password+"','"+dob+"','"+mobile+"','"+email+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
  

def requestact(request):
    try:
        c, conn = db_connect()
        id = "0"
        empname= session['username']
        print(request)
        c.execute("select * from user where username='"+empname+"'")
        result=c.fetchall()
        empid= result[0][0]
        j = c.execute("insert into requests (id,empid,empname,request) values ('"+id+"','"+empid+"','"+empname+"','"+request+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))  

def reqact(request,user):
    try:
        c, conn = db_connect()
        c.execute("select id from user where username='"+user+"'")
        result = c.fetchall()
        print(result)
        a = result
        aa=a[0]
        a2=aa[0]
        id = a2
        print(id)
        print(request,user)
        response = "Pending"
        status = "pending"
        reqid = 0
        j = c.execute("insert into userrequest (id,reqid,username,request,response,status) values ('"+str(id)+"','"+reqid+"','"+user+"','"+request+"','"+response+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))  



def respond_act(reqid,res):
    try:
        c, conn = db_connect()
        print(reqid,res)
        status =  "Completed"
        j = c.execute("update userrequest set  response='"+res+"',status = '"+status+"' where reqid='"+reqid+"' ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def view_response():
    c, conn = db_connect()
    username= session['username']
    c.execute("select * from userrequest where username='"+username+"'")
    result = c.fetchall()
    
    conn.close()
    print("result")
    return result


def view_emp():
    c, conn = db_connect()
    c.execute("select * from user")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def viewrequest():
    c, conn = db_connect()
    c.execute("select * from userrequest")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def v_response(empid,reqid):
    c, conn = db_connect()
    print(empid,reqid)
    c.execute("select * from userrequest where id='"+empid+"' and reqid='"+reqid+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

# -------------------------------Registration End-----------------------------------------------------------------
# -------------------------------Loginact Start-----------------------------------------------------------------

def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def emp_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))



if __name__ == "__main__":
    print(db_connect())
