# Bad Apple to PDF Converter
A simple script to which creates a PDF documents where each page is a frame from Bad Apple.

## Installation
Download this repo and enter the directory like so:
```bash
git clone https://github.com/OskarBrzeski/bad-apple-pdf.git
cd bad-apple-pdf
```

## Dependencies
This script requires Python 3.10 or later to run. It also requires the following packages
- fpdf2
- opencv-python
- tqdm
- yt-dlp

This repo contains a `pyproject.toml` file which can be used to download the dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## How to use
I can only validate that this script works as intended on Linux Mint 21.2.
However, I would assume that this script works similarily on other Linux distributions and it should word on Windows too.

Once you have downloaded the dependencies (see previous section), you can run the script like this:
```bash
bad-apple-pdf
```

The script will temporarily store the video in the directory from which you called the script.
It will also continuously save and overwrite an image file.
Do not do anything with them.

Once the script has finished, you will see a `Bad Apple.pdf` inside the directory.