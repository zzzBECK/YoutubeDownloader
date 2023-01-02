import pytube

class Video(object):

    def __init__(self, link: str):
        self.youtubeVideo = pytube.YouTube(link)
        self.youtubeVideo = self.youtubeVideo.streams.get_highest_resolution()
       
    def downloadVideo(self):
        print("Starting download...")
        self.youtubeVideo.download()
        print("Download complete!")

    def main(self):
        try:
            link = input("Youtube URL: ")
            video = Video(link)

            video.downloadVideo()

        except pytube.exceptions.RegexMatchError:
            print(f'The Regex pattern did not return any matches for the video: {link}')

        except pytube.exceptions.ExtractError:
            print (f'An extraction error occurred for the video: {link}')

        except pytube.exceptions.VideoUnavailable:
            print(f'The following video is unavailable: {link}')

        except:
            print("An unexpected error has ocurred")

if __name__ == "__main__":
    Video.main(Video)