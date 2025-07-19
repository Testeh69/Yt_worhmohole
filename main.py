import argparse
import os
import tqdm
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from yt_dlp import YoutubeDL

EMOJIS = {
    "download": "⬇️",
    "success": "✅",
    "error": "❌",
    "start": "🚀",
    "music": "🎵",
    "video": "🎬"
}

def download_video(url, format, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True
    }
    
    if format == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    elif format == "mp4":
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        })

    tqdm.tqdm.write(f"{EMOJIS['start']} {EMOJIS['download']} Downloading {url} as {format}...")
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def pipeline_dl(input="down.txt", format="mp3", output_path="downloads", nb_threads=4):
    if input.endswith(".txt"):
        with open(input, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]

        tqdm_bar = tqdm.tqdm(total=len(urls), desc=f"{EMOJIS['music'] if format=='mp3' else EMOJIS['video']} Download Progress")

        def task(url):
            try:
                download_video(url, format, output_path)
                tqdm_bar.write(f"{EMOJIS['success']} Successfully downloaded: {url}")
            except Exception as e:
                tqdm_bar.write(f"{EMOJIS['error']} Error downloading {url}: {e}")
            finally:
                tqdm_bar.update(1)

        with ThreadPoolExecutor(max_workers=nb_threads) as executor:
            executor.map(task, urls)
        
        tqdm_bar.close()
        print(f"{EMOJIS['success']} All downloads completed.")
        return "Batch download completed successfully."

    else:
        try:
            download_video(input, format, output_path)
            print(f"{EMOJIS['success']} Download completed successfully.")
            return "Download completed successfully."
        except Exception as e:
            print(f"{EMOJIS['error']} Error downloading video: {e}")
            return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos or playlists.")
    parser.add_argument("input", type=str, help="Input file with URLs or a single URL.")
    parser.add_argument("--format", type=str, choices=["mp3", "mp4"], default="mp3", help="Format to download the video in.")
    parser.add_argument("--output_path", type=str, default="downloads", help="Directory to save downloaded files.")
    parser.add_argument("--nb_threads", type=int, default=4, help="Number of threads for downloading.")
    args = parser.parse_args()

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    pipeline_dl(input=args.input, format=args.format, output_path=args.output_path, nb_threads=args.nb_threads)
