
import urllib.request
from bs4 import BeautifulSoup
import sched, time
import threading
import smtplib
from test_email import *

theurl = 'https://twitter.com/Imaqtpielol'

thepage = urllib.request.urlopen(theurl)

soup = BeautifulSoup(thepage, 'html.parser')

title = soup.title.text

s = sched.scheduler(time.time, time.sleep)

new_line = '\n'*1


#print bio desc
post = soup.find('p', {'class':'TweetTextSize TweetTextSize--16px js-tweet-text tweet-text'}).text,
clean_post = title + '\n' + str(post).strip('()').rstrip(',').replace('https://www.twitch.tv/imaqtpie', ' ').replace('\'',' ').replace('\\xa0', ' ').lstrip() 
last_post = None


def send_mail():
	TO = ''
	SUBJECT = 'Test Email'

#	acc_gmail = email username
#	pwd_gmail = email password
	msg = clean_post
	server = smtplib.SMTP('smtp.gmail.com', 587)
	#change above if not using gmail
	server.ehlo()
	server.starttls()
	server.ehlo
	server.login(acc_gmail, pwd_gmail)

	BODY = '\r\n'.join([
			'To: %s'%(TO,),
			'From: %s'%(acc_gmail,),
			'Subject: %s'%(SUBJECT,),
			' ',
			msg
			])
	try:
		server.sendmail(acc_gmail, [TO], BODY)
		print('Email sent containing \n{0}'.format(clean_post,))
	except:
		print('Error, email not sent!')

	server.quit()

def last_tweet():
	threading.Timer(3600.0, last_tweet).start()
	global last_post
	i = 0
	while i < 11:
		if post != last_post:
			print(i)
			send_mail()
			last_post = post
			i += 1
print('Running script..')
last_tweet()
