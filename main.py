import requests
from sendemail import send_email

api_key = "de3ea3fd44fb491aba136040a807febf"

topic ="tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2022-12-21"\
    "&sortBy=publishedAt"\
    "&apiKey=de3ea3fd44fb491aba136040a807febf&language=en"

#Makes A Request
request = requests.get(url)

#Get a dictionary with data
content = request.json()



body = ""
# Access the article titles and description
for item in content["articles"][:20]:
    body ="Subject: Today's news"  + "\n" + body + str(item["author"]) + "\n" + str(item["title"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)