from collections.abc import Iterator
import os

import cv2
from fpdf import FPDF
from PIL import Image
from tqdm import tqdm
import yt_dlp


def download_bad_apple() -> None:
    with yt_dlp.YoutubeDL({"outtmpl": "Bad Apple"}) as ydl:
        ydl.download("https://www.youtube.com/watch?v=FtutLA63Cp8")


def video_frames(capture: cv2.VideoCapture) -> Iterator[cv2.UMat]:
    while True: 
        ret, frame = capture.read();

        if ret == False:
            break

        yield frame


def add_image_to_pdf(pdf: FPDF, frame: cv2.UMat) -> None:
    pdf.add_page()
    cv2.imwrite("currentframe.png", frame)
    pdf.image(Image.open("currentframe.png"), x=0, y=0, w=480, h=360)


def clean_up() -> None:
    os.remove("Bad Apple.webm")
    os.remove("currentframe.png")


def main() -> None:
    download_bad_apple()
    
    pdf = FPDF(unit="pt", format=(480, 360))
    capture = cv2.VideoCapture("Bad Apple.webm")
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame in tqdm(video_frames(capture), desc="Bad Apple to PDF", total=frame_count):
        add_image_to_pdf(pdf, frame)

    pdf.output("Bad Apple.pdf")
    
    del capture
    clean_up()


if __name__ == "__main__":
    main()
