
import pytesseract
from PIL import Image
import io
from pdf2image import convert_from_bytes

async def parse_transcript(file):
    content = await file.read()
    if file.filename.endswith(".pdf"):
        images = convert_from_bytes(content)
    else:
        images = [Image.open(io.BytesIO(content))]

    full_text = "\n".join([pytesseract.image_to_string(img) for img in images])
    return {"raw_text": full_text}
