import pytube

class Video(object):

    def __init__(self, link: str):
        self.youtube = pytube.YouTube(link)
        self.youtube.register_on_progress_callback(self.progress)

    def progress(self, stream, _, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        print(f"Downloaded {percentage_of_completion:.2f}%")

    def downloadAudio(self):
        print("Starting audio download...")
        audio_stream = self.youtube.streams.get_audio_only()
        audio_stream.download(filename_prefix="Audio")
        print("Audio download complete!")

    def downloadVideo(self):
        print("Starting video download...")
        video_stream = self.youtube.streams.get_highest_resolution()
        video_stream.download()
        print("Video download complete!")

    @staticmethod
    def main():
        try:
            link = input("Youtube URL: ")
            video = Video(link)
            
            print("1. Download Audio")
            print("2. Download Video")
            option = int(input("Option: "))

            if option == 1:
                video.downloadAudio()
            elif option == 2:
                video.downloadVideo()

        except pytube.exceptions.RegexMatchError as e:
            print(f'The Regex pattern did not return any matches for the video: {link}. Error: {e}')

        except pytube.exceptions.ExtractError as e:
            print(f'An extraction error occurred for the video: {link}. Error: {e}')

        except pytube.exceptions.VideoUnavailable as e:
            print(f'The following video is unavailable: {link}. Error: {e}')

        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

if __name__ == "__main__":
    Video.main()
