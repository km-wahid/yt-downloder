from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp
import os
import uuid
import threading

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

progress_data = {}

def download_video(url, download_type, download_id):
    filename = f"{uuid.uuid4()}.{'mp3' if download_type == 'audio' else 'mp4'}"
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    def hook(d):
        if d['status'] == 'downloading':
            progress_data[download_id] = d['_percent_str'].strip()
        elif d['status'] == 'finished':
            progress_data[download_id] = "done"
            progress_data[download_id + "_path"] = filepath

    ydl_opts = {
        'outtmpl': filepath,
        'format': 'bestaudio/best' if download_type == 'audio' else 'best',
        'progress_hooks': [hook],
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if download_type == 'audio' else [],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/start-download", methods=["POST"])
def start_download():
    url = request.form["url"]
    download_type = request.form["type"]
    download_id = str(uuid.uuid4())
    progress_data[download_id] = "0%"

    threading.Thread(target=download_video, args=(url, download_type, download_id)).start()
    return jsonify({"download_id": download_id})

@app.route("/check-progress/<download_id>")
def check_progress(download_id):
    status = progress_data.get(download_id, "unknown")
    if status == "done":
        path = progress_data.get(download_id + "_path")
        response = send_file(path, as_attachment=True)
        # Cleanup
        threading.Timer(10, lambda: os.remove(path)).start()
        del progress_data[download_id]
        del progress_data[download_id + "_path"]
        return response
    return jsonify({"status": status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

