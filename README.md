# Bad Apple to PDF Converter
A simple script which creates a PDF document where each page is a frame from Bad Apple.
The document can be watched as a video by flipping through the pages fast enough.

## Installation
Download this repo and enter the directory:
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
### Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```
### Windows
```powershell
python -m venv .venv
.venv/Scripts/activate
pip install -e .
```

## How to use
This script is known to work on Linux Mint 21.2 and Windows 10 22H2.
However, I would assume that this script works similarily on other Linux distributions
and versions of Windows as the only requirement is Python.

Once you have downloaded the dependencies (see previous section), you can run the script as a command in your terminal:
```bash
bad-apple-pdf
```

Once the script has finished, you will see `Bad Apple.pdf` inside the directory.