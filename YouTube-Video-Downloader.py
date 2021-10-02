from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=RkC0l4iekYo&t=41s")  # Video URL
print(video.thumbnail_url)
print(video.length)

print(video.title)
print("downloading...")

stream = video.streams.get_highest_resolution()
stream.download(output_path='/Users/aryamaddel/Desktop')

print('Downloaded successfully!')
