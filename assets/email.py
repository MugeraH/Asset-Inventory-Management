from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_response_email(name,receiver):
    # Creating message subject and sender
    subject = 'Thanks for reaching out to Assset  Management Inventory, we will get back you as soon as possible.'
    sender = 'jackotienokey@gmail.com'
    
    #passing in the context vairables
    text_content = render_to_string('Email/customeremail.txt',{"name": name})
    html_content = render_to_string('Email/customeremail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    
    
def send_email(name,receiver,date):
    # Creating message subject and sender
    subject = 'Welcome to the Awwwards clone'
    sender = 'testmugera@gmail.com'
    ctx= {
        "name": name,
       "date":date
    }


    #passing in the context vairables
    text_content = render_to_string('email/awwemail.txt',ctx)
    html_content = render_to_string('email/awwemail.html',ctx)

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
