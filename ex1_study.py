from youtube_dl import YoutubeDL
dl = YoutubeDL()
# Sample 1
dl.download(['https://www.youtube.com/watch?v=Ph54wQG8ynk'])
print(dl)


# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=Em7vc8NWUNY', 'https://www.youtube.com/watch?v=3b1YSNsF2eE'])
print(dl)



Sample 3: Download audio
options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=Ph54wQG8ynk'])
print(dl)


# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['havana camila cabello'])
print(dl)



# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['crush david archuleta'])
print(dl)