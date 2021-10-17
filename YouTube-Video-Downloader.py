from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Video URL
print(video.thumbnail_url)
print(video.length)

print(video.title)
print("downloading...")

stream = video.streams.get_highest_resolution()
stream.download(output_path='/Users/aryamaddel/Desktop')

print('Downloaded successfully!')
