from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        print("Starting download...")
        youtubeObject.download()
        print("Download complete!")
    except:
        print("An error has ocurred")


link = "https://www.youtube.com/watch?v=cp4kWvgrNUQ"

download(link)