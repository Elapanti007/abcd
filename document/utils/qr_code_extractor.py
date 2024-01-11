import fitz  # PyMuPDF
import os
import io
from PIL import Image,ImageEnhance
from pyzbar.pyzbar import decode

def extract_images_and_decode_qr(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)
    qr_data = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            if not image_bytes:
                continue  # Skip if no image bytes were extracted
            
            try:
                image = Image.open(io.BytesIO(image_bytes))
                # Save the extracted image
                image_path = os.path.join(output_folder, f"image_{page_num}_{img_index}.png")
                image.save(image_path)
                image = Image.open(io.BytesIO(image_bytes))
                enhancer = ImageEnhance.Contrast(image)
                enhanced_image = enhancer.enhance(2.0)  # Adjust contrast
                resized_image = enhanced_image.resize((300, 300))  # Resize if necessary

                decoded_objects = decode(resized_image)
                # Attempt to decode QR code if present
                # decoded_objects = decode(image)
                for obj in decoded_objects:
                    qr_data.append(obj.data.decode("utf-8"))
            except Exception as e:
                print(f"An error occurred while processing an image: {e}")
                continue  # Skip this image and move to the next one

    doc.close()
    return qr_data  