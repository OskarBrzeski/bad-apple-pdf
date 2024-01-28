from collections.abc import Iterator
from io import BytesIO
import os

import cv2
from cv2.typing import MatLike
from fpdf import FPDF
from tqdm import tqdm
import yt_dlp


def download_bad_apple() -> None:
    with yt_dlp.YoutubeDL({"outtmpl": "Bad Apple", "paths": {"home": ".temp"}}) as ydl:
        ydl.download("https://www.youtube.com/watch?v=FtutLA63Cp8")


def video_frames(capture: cv2.VideoCapture) -> Iterator[MatLike]:
    while True: 
        ret, frame = capture.read();

        if ret == False:
            break

        yield frame


def add_image_to_pdf(pdf: FPDF, frame: MatLike) -> None:
    pdf.add_page()
    file = BytesIO(cv2.imencode(".png", frame)[1].tobytes())
    pdf.image(file, x=0, y=0, w=480, h=360)


def clean_up() -> None:
    os.remove(".temp/Bad Apple.webm")
    os.rmdir(".temp")


def main() -> None:
    if not os.path.exists(".temp"):
        os.mkdir(".temp")
    
    download_bad_apple()

    pdf = FPDF(unit="pt", format=(480, 360))
    capture = cv2.VideoCapture(".temp/Bad Apple.webm")
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame in tqdm(video_frames(capture), desc="Bad Apple to PDF", total=frame_count-1):
        add_image_to_pdf(pdf, frame)

    pdf.output("Bad Apple.pdf")
    
    del capture
    clean_up()


if __name__ == "__main__":
    main()
