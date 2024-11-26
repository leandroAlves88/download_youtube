from pytube import YouTube

def download_video(url):
    "Download do videos"
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Download completo!")
    except Exception as e:
        print(f"Um erro ocorreu: {e}")


if __name__ == "__main__":
    url = input("Digite a URL do vídeo: ")
    download_video(url)
