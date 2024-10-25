

from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib


def create_html_body_email(i, dmalists, alldmas, emailrecipaints, emailsubjects, emailnotes, emailattachments):
        dmaList = dmalists[i]
        emailto = emailrecipaints[i]
        emailsubject = emailsubjects[i]
        emailnote = emailnotes[i]
        attachments = emailattachments[i]


        bodyhtml = ''
        for dma in dmaList:
            dmahtml = alldmas[dma][0]
            bodyhtml += dmahtml
        
        finalhtml =  '<html><body>' + emailnote + '<hr color="black" size="2" width="100%">' + bodyhtml +'</body></html'

        # Save the raw html
        file = open(f"html_outputs/test{i}.html","w") 
        file.write(finalhtml)
        file.close()

        # Initialize the message
        msg = EmailMessage()
        msg['Subject'] = ''
        msg['From'] = 'sn_audience_insights@outlook.com'
        msg['To'] = 'jack.driscoll@charter.com'

        msg.set_content('This is a plain text body.')

        # Set the message content to the interactive html
        msg.add_alternative(finalhtml, subtype = 'html')


        ## Add the images to the email
        for dma in dmaList:
            cid_dict = alldmas[dma][1]
            for path in cid_dict: 
                with open(path, 'rb') as img:
                    print(path)        
                    # know the Content-Type of the image
                    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                    # attach it
                    print('adding image.. ')
                    print(path)
                    print(cid_dict[path])
                    msg.get_payload()[1].add_related(img.read(), 
                                                        maintype=maintype, 
                                                        subtype=subtype, 
                                                        cid=cid_dict[path])

  

        # Sending the email
        
        print('Connecting to email server')
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
        print('\nlogged in..., sending mail...\n ')
        s.send_message(msg, 'sn_audience_insights@outlook.com', 'jack.driscoll@charter.com',)
        print('Sent mail')
        s.quit()
        


def test_smtp():

    
        # Attempt 2 
        msg = EmailMessage()
        msg['Subject'] = 'Hello there, this is a test'
        msg['From'] = 'sn_audience_insights@outlook.com'
        msg['To'] = 'jack.driscoll@charter.com'

        msg.set_content('This is a plain text body. This is a test.')\
        


        image_cid = make_msgid()
        # if `domain` argument isn't provided, it will 
        # use your computer's name
        print("creating body..")
        newbody = """
                <html>
                    <body>
                        <p>This is an HTML body.<br>
                        It also has an image.
                        </p>
                        <img src="cid:{image_cid}">
                    </body>
                </html>
            """.format(image_cid=image_cid[1:-1])
        

        msg.add_alternative(newbody, subtype='html')
        print(image_cid)

        with open('C:/Users/P3159331/OneDrive - Charter Communications/Documents - Audience Insights/5. Development/Nielsen Automation/nielsen_refactored/chart_images/S1TPtable.png', 'rb') as  img:
                print('attaching emails')
        # know the Content-Type of the image
                maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

                msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)


        import smtplib
        print('Connecting to email server')
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login('sn_audience_insights@outlook.com', 'AudienceInsights1')
        print('\nlogged in..., sending mail...\n ')
        s.send_message(msg, 'sn_audience_insights@outlook.com', 'jack.driscoll@charter.com',)
        print('Sent mail')
        s.quit()
        
if __name__ == '__main__':
       test_smtp()

        # Testing the .eml format - worked but idk how to open
        #msg = email.mime.text.MIMEText(finalhtml)
        # msg['Subject'] = 'Test message'
        # msg['From'] = 'sender@sending.domain'
        # msg['To'] = 'rcpt@receiver.domain'

        # # open a file and save mail to it
        # with open(f'html_outputs/test{i}.elm', 'w') as out:
        #     gen = email.generator.Generator(out)
        #     gen.flatten(msg)