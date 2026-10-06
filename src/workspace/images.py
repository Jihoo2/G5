"""JPG 목록 탐색과 이미지 읽기. 원본 파일은 변경하지 않습니다."""
from pathlib import Path
from PIL import Image, ImageOps
from configs import settings as C


def list_images(folder):
    return sorted(
        (p for p in Path(folder).iterdir()
         if p.is_file() and p.suffix.lower() in C.IMAGE_EXTS),
        key=lambda p: (p.name.casefold(), p.name),
    )


def load_image(path):
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert("RGB")
