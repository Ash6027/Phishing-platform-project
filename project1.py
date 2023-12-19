import smtplib
import AI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import subprocess
gmail_user = 'Senders email address'
gmail_password = 'app level password'

attacker_link="url"

print("copy the subject for the email structure")
final_text=AI.create_mail()

def html_code(value,attacker_link):
    if(value==1):
        html_temp= """<a href={}> <button style="background-color: pink; opacity: 0.75; border-radius: 12.5%; box-shadow: 2%; color: black;
          font-size: 1.5em; height: 3.5em; width: 7em;">Buy Now</button> 
                </a>""".format(attacker_link)
        return html_temp
      # make the button html
    
    elif(value==2): # get the image ready
        response = AI.Image.create(prompt=input("what kind of picture you want to create"), n=1, size="256x256")
        response_url=response.data[0].url
        print(response_url)
        return """<a href={}> <img src={} /> </a>""".format(attacker_link,response_url)
    
    else:
        print("give me a valid choice")


type_of_clickable=int(input("please give the preference do you want a button, image to be clickable\t"))

code_embedding=html_code(type_of_clickable,attacker_link) #calling the function to get the html clickable code
message = MIMEMultipart()
message["From"] = gmail_user
reciever_mail=input("reciever's address\t").strip()
message["To"] = reciever_mail
message["Subject"] =input("please give a subject for the mail\t")


html_content ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Email Title</title>
</head>
<body>
    <!-- Your HTML content goes here -->
    <div style="display: flex; justify-content: center; flex-direction: row;">
        <div style="align-items: center; width: 70%; height: 80%; color: beige; opacity: 0.75; border: 1px solid black; background-color: beige; display: flex; justify-content: center; flex-direction: row;">
            <p style="width: 100%; height: 50%; text-align: center; font-style: oblique; color: black; font-size: 2em;">{}</p>
           {}
        </div>
    </div>
</body>
</html>
""".format(final_text,code_embedding)


html_part = MIMEText(html_content, "html")
message.attach(html_part)
#getting the server ready

def send():
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(gmail_user, reciever_mail, message.as_string())
        smtp_server.close()
        print ("Email sent successfully!")
           
    except Exception as ex:
        print ("Something went wrong….",ex)

send()

with open('Clone.py','r') as file:
    code=file.read()
    exec(code)



