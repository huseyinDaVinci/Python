'''
Created on Apr 8, 2015

@author: barin.huseyin
'''
import webbrowser
import subprocess
import smtplib

def launchFirefox():
    subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe',
    '-new-tab', 'http://www.nba.com/gameline'])  
    
    subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe',
    '-new-tab', 'http://mail.google.com/'])  
    
    
    
def __init__():
    #first open firefox and some tab I needed
    # webbrowser.get('firefox').open_new_tab('http://www.google.com')

    print webbrowser.browser
        
    #webbrowser.open_new("google.com")   #default open the current browser you used.
    
    launchFirefox()
    
    #sendMailViaGmail()
    


def sendMailViaGmail():
   
    try:
        gmail_user = "bjkkaragunes@gmail.com"
        gmail_pwd = "kartal1903"
        FROM = 'bjkkaragunes@gmail.com'
        TO = ['barin.huseyin@yandex.com'] #must be a list
        SUBJECT = "Testing sending using gmail"
        TEXT = "Testing sending mail using gmail servers"

            # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        
        
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_pwd)
        server.sendmail(FROM, TO, message)
                #server.quit()
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        print "failed to send mail",e
     
    
__init__()
