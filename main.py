import mysql.connector
mydb=mysql.connector.connect(user='root',password='Ramani_rk@2903',database='bank_management')

def openacc():
    n =input("Enter the Name : ")
    acc = input("Enter the Account Number : ")
    dob = input("Enter the Date of Birth : ")
    add = input("Enter the Address : ")
    cno = int(input("Enter the Contact Number : "))
    ob= int(input("Enter the Opening Balance : "))

    data1 = (n,acc,dob,add,cno,ob)
    data2 = (n, acc, ob)
    sql1 = ('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()

def deposit():
    amount = int(input("Enter the Amount for Deposit : "))
    acc = input("Enter the Account Number : ")
    a=('select BAL from amount where ACCNo = %s')
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    t=result[0]+amount
    sql=('update amount set BAL=%s where ACCNo = %s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    main()

def withdraw():
    amount = int(input("Enter the Amount for Withdraw: "))
    acc = input("Enter the Account Number : ")
    a = ('select BAL from amount where ACCNo = %s')
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amount set BAL=%s where ACCNo = %s')
    d = (t, acc)
    x.execute(sql, d)
    mydb.commit()
    main()


def bal_enq():
    acc=input("Enter the Account Number : ")
    a=('select * from amount where ACCNo = %s')
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for Account ",acc,"is",result[-1])
    main()

def dis_det():
    acc = input("Enter the Account Number : ")
    a = ('select * from account where ACCNo = %s')
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for res in result:
        print(res,end=' ')
    main()

def closeacc():
    acc = input("Enter the Account Number : ")
    sql1 =('delete from account where ACCNo=%s')
    sql2 = ('delete from amount where ACCNo=%s')
    data = (acc,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    main()


def main():
    print(''' 
            1.) OPEN NEW ACCOUNT
            2.) DEPOSIT AMOUNT
            3.) WITHDRAW AMOUNT
            4.) BALANCE ENQUIRY
            5.) DISPLAY ACCOUNT HOLDER DETAILS
            6.) CLOSE AN ACCOUNT''')

    option = input("Enter the Task You want to Perform : ")
    if (option=='1'):
        openacc()

    elif (option=='2'):
        deposit()

    elif (option=='3'):
        withdraw()

    elif (option=='4'):
        bal_enq()

    elif (option=='5'):
        dis_det()

    elif (option=='6'):
        closeacc()

    else:
        print('Invalid Option')
main()