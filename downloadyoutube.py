from pytube import YouTube


def download_1080p_mp4_videos(url: str):
    yt = YouTube(url)
    y=yt.streams.filter(file_extension="mp4")
    y=y.get_highest_resolution()
    y=y.download(output_path="./")

url=input("Input the url: ")
try:
    download_1080p_mp4_videos(url=url)
except:
    raise Exception("Check the url")

