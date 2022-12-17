# -*- coding: utf-8 -*-

from flask import Flask, render_template, request ,redirect ,url_for
import key_config as keys
import boto3 

app = Flask(__name__)


dynamodb_client = boto3.resource('dynamodb', region_name='us-east-1',
                    aws_access_key_id=keys.ACCESS_KEY_ID,
                    aws_secret_access_key=keys.ACCESS_SECRET_KEY,
                    aws_session_token=keys.AWS_SESSION_TOKEN)

from boto3.dynamodb.conditions import Key, Attr

TABLENAME="InforCustom"


class InforCustom :
    
    def __init__(self, Email, Phone, Accountbalance, Name, Office):
        self.Email=Email
        self.Phone=Phone
        self.AccountBalance=Accountbalance
        self.Name=Name
        self.Office=Office

class Userdata :
    def __init__(self, email, name, password, phone):
        self.email=email
        self.name=name
        self.password=password
        self.phone=phone



class ConnectDynamoDB :
    def __init__(self, dynamodb ,NAMETABLE):
        table = dynamodb.Table(NAMETABLE)
        response = table.scan()

        self.tablename = NAMETABLE
        self.listItems = response
        self.names = response['Items']
        self.count = response['Count']

    def getcountItem (self):
        print('Number of items in table : '+ str(self.count))
        return self.count
    def getlistItemNames (self):
        return self.names

class TableByPhone :
    def __init__(self ,dynamodb ,nametable,phone):
        self.dynamodb = dynamodb
        self.nametable = nametable
        self.phone = phone

    def loadDatabyPhone(self):
        PHONE = self.phone
        INFO = None
        data=DynamoDb(dynamodb_client, TABLENAME)
        list=data.loadDATA()
        for i in list:
            if i.Phone == PHONE:
                INFO = InforCustom(i.Email,i.Phone,i.AccountBalance,i.Name,i.Office)
                break
        return INFO
        
class DynamoDb :
    def __init__(self ,dynamodb ,nametable):
        self.dynamodb = dynamodb
        self.nametable = nametable

    def loadDATA (self):
        LISTINFOR = []
        list = ConnectDynamoDB(dynamodb=dynamodb_client, NAMETABLE=TABLENAME)
        for obj in list.getlistItemNames() :
            acc = InforCustom( obj['Email'],obj['Phone'], obj['Account balance'], obj['Name'], obj['Office'])   
            LISTINFOR.append(acc)
        return LISTINFOR

    # def addAccount (self):
    #     try :
    #         table = self.dynamodb.Table(self.nametable)
    #         response = table.put_item(
    #             Item = { 
    #                 'Name': self.name,
    #                 'Email': self.email
    #             }
    #         )
    #         return True
    #     except:
    #         print("Tao tai khoan khong thanh cong !")
    #         return False

    # def deleteAccount (self):
    #     try :
    #         table = self.dynamodb.Table(self.nametable)
    #         response = table.delete_item(
    #             Key = {
    #                 'Name': self.name,
    #                  'Email': self.email
    #                  })
    #         print(response)
    #         return True
    #     except:
    #         print("Tai khoan khong ton tai !")
    #         return False

    # def readAccount (self):
    #     try :
    #         table = self.dynamodb.Table(self.nametable)
    #         response = table.get_item(
    #             Key={
    #                 'Name': self.name,
    #                 'Email': self.email
    #             }
    #         )
    #         resp = response['Item']
    #         print(resp)
    #         return resp
    #     except:
    #         print("Tai khoan khong ton tai !")
    #         return None




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    phone = request.args.get('phone')
    test = TableByPhone (dynamodb_client,TABLENAME,phone)
    LISTINFO = []
    Info = test.loadDatabyPhone()
    LISTINFO.append(Info)
    return render_template('home.html', LISTINFO = LISTINFO , name = Info.Name)

@app.route('/signup', methods=['post'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        table = dynamodb_client.Table('userdata')
        
        table.put_item(
                Item={
                'name': name,
                'email': email,
                'password': password,
                'phone': phone,
            }
        )
        msg = "Registration Complete. Please Login to your account !"
        return render_template('login.html',msg = msg)

    return render_template('index.html')

@app.route('/login')
def login():    
    return render_template('login.html')


@app.route('/check',methods = ['post'])
def check():
    if request.method=='POST':
        
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb_client.Table('userdata')
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            PHONE = items[0]['phone']
            return redirect(url_for('home',phone = PHONE))

    return render_template("login.html")


@app.route('/updateBalanceform')
def updateBalanceForm():
    return render_template("updatebalance.html")

@app.route('/updateBalance',methods = ['post'])
def updateBalance():
    if request.method=='POST':
        balance = request.form['balance']
        phone = request.form['phone'] 
        print(balance)
        print(phone)
        
        test = TableByPhone (dynamodb_client,TABLENAME,phone)
        Info = test.loadDatabyPhone()
        table = dynamodb_client.Table(TABLENAME)
        # get item
        response = table.get_item(Key={
                'Email': Info.Email,
                'Phone': Info.Phone
                })
        item = response['Item']

        # update
        item['Account balance'] = balance

        # put (idempotent)
        table.put_item(Item=item)
    return redirect(url_for('home',phone = Info.Phone))




if __name__ == "__main__":
    
    app.run()