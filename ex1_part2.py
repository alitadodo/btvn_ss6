from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")

soup = BeautifulSoup(html_content,"html.parser")

section = soup.find("section", "section chart-grid")

li_list = section.find_all("li")

for li in li_list:
    h3_name = li.h3
    a_name = h3_name.a
    music_names = a_name.string

    h4_artists = li.h4
    a_artists = h4_artists.a
    artists = a_artists.string
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1
    }
    dl = YoutubeDL(options)
    dl.download([music_names + artists])


# pyexcel.save_as(records=name_artits, dest_file_name="itunes_top.xls")