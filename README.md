# reddit-wallpapers
This program will fetch, download, and save the 100 hottest wallpapers from the r/wallpaper subreddit to a folder in your computer. It can also optionally remove low-quality images, and then cycle through the dozens of images and set them as your desktop background.

## Requirements
- `requests` (`pip3 install requests`)
- `beautifulsoup4` (for BeautifulSoup) (`pip3 install beautifulsoup4`)
- `praw` (`pip3 install praw`)

All the above modules are available on PyPI. You can download them each individually or simply run `pip install requirements.txt`.

## Usage
In order for `reddit-wallpapers` to work, you must create your own Reddit bot. Reddit itself does not provide access to the links and content on its pages, so creating a bot that is given permission to go through its database is required. This takes about 5 mins, and the steps are outlind below.

1. Go to https://reddit.com/prefs/apps and login if you are asked to do so. This is where you will create the bot.
2. Scroll to the bottom and click 'create another application'. Fill out the details as follows:
  - Name: ImageBot
  - Type: script
  - Description: Any description you want
  - Redirect URL: http://localhost:8080

3. Once you have done the above, click `create app`. You should now see a bot named ImageBot on your page.
4. Go to the bottom left of the ImageBot square and click edit. You will now see some information about the bot - most importantly, your `personal use script` and `secret`.
5. Go to wherever you have saved the `add_images.py` program and start replacing. Replace `client_id` with your personal use script (seen at the top of the bot square). Replace your `client_secret` with your 27-character secret key (also seen in the bot square). Replace HIDDEN with your username, and `HIDDEN_PASSWORD` with your password.

You are now all set up with your very own Reddit bot that can read data from Reddit! There's only a few more things to do before you too can get that beautiful changing background!

First, you need to make sure that you have all the required modules intalled. These are all outlined in `requirements.txt` and they can be downloaded using `pip`. Without them downloaded, the program will not run.

Once you have done so, all you need to do is change the `os.chdir()` line. Currently, it is pointing to a folder on my Desktop, but you will need to change that so it matches an absolute path on your computer (i.e. change Users/Destaq to Users/<your name> and either create a directory in the Desktop or make it point to another *blanki* directory.

The only thing left to do at this point is run the program, with `python3 add_images.py`. Keep in mind that it may take a few minutes to download all the images due to hardware or Internet limitations. However, you can rest assured as there is a progress bar showing which image is currently being downloaded/processed.

You may notice at the bottom of the code that there are a few lines which check and delete small images. Not all images posted on r/wallpaper are clear, and so the program deletes ones which are smaller than 200 kB. You can change this size, or remove the deletion entirely (but fuzzy images may show up on Desktop).

*Last note*: Once you have all of your images downloaded to your folder, all you have to do is navigate to your System Preferences/Settings and change the directory where your computer gets its images from. Below are two images showing how to do so on Mac and Windows. I recommend setting random order to true for the real 'excitement'.
