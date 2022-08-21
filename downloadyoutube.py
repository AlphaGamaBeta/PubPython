from pytube import YouTube
#This version give you the ability to only download highest quality and mp4 extension only 

def download_mp4_video(url: str):
    yt = YouTube(url)
    y=yt.streams.filter(file_extension="mp4")
    y=y.get_highest_resolution()
    y=y.download(output_path="./")

url=input("Input the url: ")
try:
    download_mp4_video(url=url)
except:
    raise Exception("Check the url")

