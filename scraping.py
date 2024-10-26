import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# URL of the blog website you want to scrape
url = 'https://website/'

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object with the website content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the blog post elements on the page
blog_posts = soup.find_all('div', id='left-area')   

print(blog_posts)

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://user:MDP@cluster"
 
# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)

db = client['posts']
print("okey")
print(blog_posts)
# Iterate over each blog post and extract the desired information
for post in blog_posts:
    # Extract the title of the blog post
    title = post.find('h2').text
    print(title)
    # Extract the content of the blog post
    content = post.find('p', class_='post-meta').text.strip()
    print(content)

    item = {
    "title": title,
    "content": content,
    "author": "authors",
    }
    db.posts.insert_one(item)
    
    # Print the title and content of each blog post
    print(f'Title: {title}')
    print(f'Content: {content}')
    print('---')
