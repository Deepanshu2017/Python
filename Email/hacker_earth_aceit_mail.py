text = "Hey Folk,\nWant to grow your programming skills and don't know from where to start. Well then we " \
       "bring HackerEarth to our campus. We are calling all the passionate programmers from ACEIT, Jaipur " \
       "to come and be a part of the fastest growing community in the world.\n\nWhat is HackerEarth?\nIt " \
       "provides a platform to compete with the best developers and challenge yourself. It permits 25 " \
       "programming languages which you can learn and compete. It also provides tutorials " \
       "for strong programming foundation.\nWhat you need to do right now is create a developer account on " \
       "HackerEarth Platform. Follow this link :\nhttps://www.hackerearth.com/\n\nAnd also join us on our " \
       "Facebook Page for more updates and upcoming challenges.\nhttps://www.facebook.com/HackerEarthACEIT\n" \
       "\nWe will conduct programming challenges in our college every month and the winners will get " \
       "exciting prizes from HackerEarth. So tighten up your seat belts and get ready for a thrilling " \
       "journey.\n\nRegards,\nHackerEarth"
username = 'hackerearthaceit@gmail.com'

with file('email_list.txt', 'r') as f:
    # Because of some unknown reasons hacker earth aceit gmail accound is not delivering more email to more then one
    # account at the same time this is why creating entirely new mail including new smtplib object
    
    for line in f.readlines():
        l = len(line)
        recipients = line[:l - 1]  # remove new line character
        from email.mime.text import MIMEText
        msg = MIMEText(text)
        msg['Subject'] = 'HackerEarth ACEIT Programming Club Jaipur'
        msg['From'] = username
        msg['To'] = recipients
        msg = msg.as_string()

        import smtplib
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(username, 'enter password here')
        server.sendmail(username, recipients, msg)
        server.quit()
