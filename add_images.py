import praw
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import quote
import requests
import sys
import os

storage_directory = "/Users/Destaq/Desktop/Background_Images"
os.chdir(storage_directory)  # change to your blank directory
print("Navigated to directory...")

# clear directory each day to prevent duplicates
filelist = [f for f in os.listdir(storage_directory)]
for f in filelist:
    os.remove(f)
print("Removed previous files...\n")

SCRIPT = "HIDDEN_SCRIPT"  # check README
SECRET = "HIDDEN_SECRET"  # check README
NUM_IMAGES = 100

reddit = praw.Reddit(
    client_id=SCRIPT,
    client_secret=SECRET,
    user_agent="ImageBot",
    username="MY_USERNAME",  # your username
    password="HIDDEN_PASSWORD",  # your password
)

subreddit = reddit.subreddit("wallpaper")

links = []
for submission in subreddit.hot(limit=NUM_IMAGES):
    links.append("https://reddit.com" + submission.permalink)


images = []
for i in range(len(links)):
    sys.stdout.write(f"\rProcessing image {i+1} of {NUM_IMAGES}.")

    link_decoded = links[i][:21] + quote(links[i][21:])

    req = Request(link_decoded, headers={"User-Agent": "Mozilla/5.0"})

    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    for link in soup.findAll("a"):

        if (
            "https://i.redd.it/" in str(link.get("href"))[0:18]
            and str(link.get("href")) not in images
        ):
            images.append(link.get("href"))

sys.stdout.flush()

for i in range(len(images)):
    sys.stdout.write(f"\rWriting image {i+1} of {len(images)}.")
    img_data = requests.get(images[i]).content
    with open(f"image_{i+1}.{images[i][-3:]}", "wb") as handler:
        handler.write(img_data)
        if (
            os.stat(f"image_{i+1}.{images[i][-3:]}").st_size < 200000
        ):  # delete images under 200 kB; too fuzzy
            os.remove(f"image_{i+1}.{images[i][-3:]}")

sys.stdout.write("\n")
