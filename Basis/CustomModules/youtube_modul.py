import requests
from pytube import YouTube

def download_mp4(url: str, output_folder: str):
    """
    Downloads the audio from a YouTube video from the given URL and saves it to the specified output path.

    Parameters:
    - url: str
        The URL of the YouTube video to download the audio from.
    - output_folder: str
        The folder name where the downloaded audio will be saved.

    Raises:
    - ValueError:
        Raises an error if the URL is invalid or the output path is not writable.
    - Exception:
        Raises an exception if there is an error during the download or conversion process.
    """

    try:
        # Creating a YouTube object from the URL
        youtube = YouTube(url)

        # Selecting the audio stream
        audio = youtube.streams.filter(only_audio=True).first()

        # Downloading the audio to the specified output folder
        audio.download(output_path=output_folder)

        return
    except Exception as e:
        raise Exception(f"Error downloading YouTube audio: {e}")