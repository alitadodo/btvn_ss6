from youtube_dl import YoutubeDL
# dl = YoutubeDL()
# # Sample 1
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# print(dl)


# # Sample 2: Download multiple youtube videos
# dl = YoutubeDL()
# # Put list of song urls in download function to download them, one by one
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])
# print(dl)



# # Sample 3: Download audio
# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])
# print(dl)


# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['Natural Imagine Dragons'])
print(dl)



# # Sample 5: Search and then download the first audio
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1, # Tell downloader to download only the first entry (audio)
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['Nhớ mưa sài gòn lam trường'])
# print(dl)