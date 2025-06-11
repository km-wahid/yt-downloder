# Simple YouTube Downloader

This is a straightforward script for downloading videos and audio from YouTube using `yt-dlp`.

## Features

* Downloads videos in various qualities.
* Downloads audio only.
* Easy to use.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3:** [Download Python](https://www.python.org/downloads/)
* **yt-dlp:** You can install it via pip:
    ```bash
    pip install yt-dlp
    ```

## Usage

1.  **Save the script:** Save the provided Python code (your `yt-dlp` script) as a `.py` file (e.g., `downloader.py`).

2.  **Run from your terminal:**
    ```bash
    python downloader.py <YouTube_URL> [options]
    ```

    **Example:**

    To download a video:
    ```bash
    python downloader.py [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    ```

    To download only audio:
    ```bash
    python downloader.py [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ) --audio-only
    ```

## Options (assuming common `yt-dlp` usage in your script)

While your script might have specific options, here are some common `yt-dlp` flags you might integrate or use:

* `-f <format_code>`: Specify the desired format code (e.g., `bestvideo+bestaudio`, `bestaudio`).
* `--audio-only`: Download only the audio stream.
* `-o <output_template>`: Specify the output filename template (e.g., `%(title)s.%(ext)s`).
* `--verbose`: Print more information during the download process.

For a comprehensive list of `yt-dlp` options, refer to the official documentation: [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

## Contributing

If you'd like to improve this simple downloader, feel free to fork the repository and submit pull requests.

## License

[Specify your license here, e.g., MIT License]
