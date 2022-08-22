from pytube import YouTube
#Simple one 

def progress(stream,chunk,bytes_remaining):
    print(f"Video is being download! remaining {bytes_remaining}")
def complete(stream, file_path):
    print(f"Downloading completed {file_path}")
def download_1080p_mp4_videos(url: str):
    yt = YouTube(url=url,on_progress_callback=progress,on_complete_callback=complete)
    y=yt.streams.filter(file_extension="mp4")
    y=y.get_highest_resolution()
    y.download(output_path="./")

def fun():
    url = input("Input the url (q for exit): ")
    if url == "q":
        return
    try:
        download_1080p_mp4_videos(url=url)
    except:
        print("Check the URL \n ")
        fun()
fun()

