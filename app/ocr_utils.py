import pytesseract
from PIL import Image
import io
from pdf2image import convert_from_bytes
import logging

logging.basicConfig(level=logging.INFO)

async def parse_transcript(file):
    content = await file.read()

    try:
        if file.filename.endswith(".pdf"):
            images = convert_from_bytes(content)
            logging.info("✅ Converted PDF to images successfully.")
        else:
            images = [Image.open(io.BytesIO(content))]
            logging.info("✅ Opened image file successfully.")

        full_text = "\n".join([pytesseract.image_to_string(img) for img in images])
        logging.info("✅ OCR complete. Extracted text:")
        logging.info(full_text[:500])  # Only print first 500 chars
        return {"raw_text": full_text}

    except Exception as e:
        logging.error("❌ Failed during OCR:", exc_info=True)
        raise e
