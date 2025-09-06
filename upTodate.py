import requests #fetch data from the web
import smtplib #send emails to smtp protocols
from email.mime.text import MIMEText #helps build the email
from email.mime.multipart import MIMEMultipart
from datetime import datetime #add current date to our email
from config import * 

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)  # Change working directory to the script's location
print(f"Script running from: {script_dir}")

#function definitions

def getNews():
    print("fetching news")
    

    url = f"https://newsapi.org/v2/everything?q=South Africa&sortBy=publishedAt&language=en&pageSize=10&apiKey={newsApiKey}"
    
    response = requests.get(url)
    print(f"api response status: {response.status_code}")

    if response.status_code !=200:
        return "Error, could not fetch news at this time"
    
    newsData = response.json()

    
    if newsData['status'] != 'ok':
        return f"Error from news Api: {newsData.get('message, ''uknown error')}"

    articles = newsData['articles']
    
   
    print(f"Number of articles found: {len(articles)}")
    if len(articles) == 0:
        print("DEBUG: Full API response:", newsData)
   

    emailBody = "<h2>Your Morning News Digest</h2>"
    emailBody += f"<p><i>Date: {datetime.now().strftime('%A, %B %d, %Y')}</i></p>"


    for article in articles[:5]:

        title = article['title']
        description = article['description'] or "No description provided"
        url = article['url']
        sources = article['source']['name']

        emailBody += f"""
        <hr>
        <h3>{title}</h3>
        <p><strong>Source:</strong> {sources}</p>
        <p>{description}</p>
        <p><a href='{url}'>Read full article</a></p>
        """

    return emailBody


def sendMail(body_text):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Your Daily News Digest - {datetime.now().strftime('%y-%m-%d')}"
    msg['From'] = emailSender
    msg['To'] = emailReceiver

    htmlText = MIMEText(body_text,'html')
    msg.attach(htmlText)

    try:
        server = smtplib.SMTP(smtpServer,smtpPort)
        server.starttls()

        server.login(emailSender,emailAppPass)

        server.sendmail(emailSender,emailReceiver,msg.as_string())

    except Exception as e:
        print(f'Error sending email: {e}')
        return False
    
    finally:
        server.quit()
        print("disconnected..")

    return True

#main 
if __name__ == "__main__":

    print("="*50)
    print("starting")
    print("="*50)

    news = getNews()

    if news.startswith("Error"):
        print(f"terminated due to error: {news}")

    else:

        success = sendMail(news)
        if success:
            print('completed successfully')
        else:
            print('failed to send email')

