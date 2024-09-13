import smtplib 

to = input("Enter the email address of the receiver")

message  input("Enter the message :-")

def sendEmail(to,message):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.starttls()0
    server.login('username','password') #enter ur email id and password
    server.sendmail(senderemail,to,message) ##enter the reciver's email address 
    server.close()

sendEmail()