import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://siwon:rlaznf11@cluster0.icysouv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsiwon

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    movie = tr.select_one('td.title > div > a')
    if movie is not None:
        title = movie.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        rating = tr.select_one('td.point').text
        doc = {
            'title': title,
            'rank': rank,
            'rating': rating
        }
        #db.movies.insert_one(doc)

# Quiz 1
movieRating = db.movies.find_one({'title':'가버나움'})['rating']
print(movieRating)

# Quiz 2
targetRating = db.movies.find_one({'title':'가버나움'})['rating']

movies = list(db.movies.find({},{'_id':False}))

for movie in movies:
    rating = movie['rating']
    if rating == targetRating:
        title = movie['title']
        print(title)

# Quiz 3
db.movies.update_one({'title':'가버나움'},{'$set':{'rating':0}})