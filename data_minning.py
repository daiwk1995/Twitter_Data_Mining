from collections import defaultdict
import json
import operator
import validators
import json
import tweepy
api_key = '2hNqzcWDgUdZy4xBqhB5QZOW1'
api_secret = '7h83YOhKAhBSZDguPW1KLpcuzhCaE5q09qcXruweoKjYA6Qhtd'

access_token = '834824567864582144-j64sQIlJPeVxRbHn7JRpuCFqyfGFiHO'
access_token_secret = 'Y1udhZoHNN7sKdkov221VoTDWieFpQr3VAgjFQQoe0gCF'



auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

frequency = defaultdict(int)
for tweet in tweepy.Cursor(api.search, q="http://www.foxnews.com/politics/2017/03/27/sessions-takes-aim-at-dangerous-sanctuary-cities-warns-on-funding.html", rpp=100, count=20, result_type="recent", include_entities=True, lang="en").items(10):
   temp = tweet.entities.get("urls")
   for item in temp:
       frequency[item.get('url')]+=1


#data = []
#with open('1.json') as f:
    #for line in f:
        #data.append(json.loads(line))
#file1=open("4.txt","w")
#for x in range(len(data)):
    #file1.write(data[x]["text"])

#with open('5.txt') as f:
    #array = [[str(x) for x in line.split()] for line in f]

#frequency = defaultdict(int)
#for x in range (len(array)):
    #for y in range (len(array[x])):
        #data=array[x][y]
        #for symbol in data:
            #if(symbol=="#"):
                #frequency[data]+= 1

sorted_x = sorted(frequency.items(), key=operator.itemgetter(1),reverse=True)
for x in range(len(sorted_x)):




file=open("2.txt","w")
for x in range(len(sorted_x)):
    file.write(str(sorted_x[x][0]))
    file.write("["+str(sorted_x[x][1])+"]")
    file.write("\n")

#frequencyurl = defaultdict(int)
#for x in range (len(array)):
    #for y in range (len(array[x])):
        #data=array[x][y]
        #if("https" in data and "€" not in data):
            #if(validators.url(data)):
                #frequencyurl[data]+= 1

#sorted_x = sorted(frequencyurl.items(), key=operator.itemgetter(1),reverse=True)

file=open("3.txt","w")
for x in range(len(sorted_x)):
    file.write(str(sorted_x[x][0]))
    file.write("["+str(sorted_x[x][1])+"]")
    file.write("\n")