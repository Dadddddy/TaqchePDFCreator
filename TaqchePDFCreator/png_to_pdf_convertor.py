import sys

from PIL import Image
import os
import io

def resize_and_convert_png_to_jpg(image_path, max_size=(1280, 720), quality=85):
    with Image.open(image_path) as img:
        # Resize the image, maintaining aspect ratio
        img.thumbnail(max_size, Image.Resampling.LANCZOS)  # Updated resampling filter

        # If the image has an alpha channel, blend it onto a white background
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            alpha = img.convert('RGBA').split()[-1]
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=alpha)
            img = bg

        # Convert image to JPEG
        jpeg_img_bytes = io.BytesIO()
        img.save(jpeg_img_bytes, 'JPEG', quality=quality)
        jpeg_img_bytes.seek(0)

        # Open the JPEG image from bytes and return
        return Image.open(jpeg_img_bytes)

def pngs_to_pdf(source_folder, output_pdf, max_image_size, jpeg_quality):
    imagelist = []

    for i in range(1, 20):
        file_path = os.path.join(source_folder, f"{i}.png")
        sys.stdout.write(f"\rNumber of Pages processed: {i}")
        sys.stdout.flush()
        if os.path.exists(file_path):
            img = resize_and_convert_png_to_jpg(file_path, max_size=max_image_size, quality=jpeg_quality)
            imagelist.append(img)

    if imagelist:
        imagelist[0].save(output_pdf, save_all=True, append_images=imagelist[1:])

        # Close all images after saving to PDF
        for img in imagelist:
            img.close()

    print(f"\nPDF created successfully: {output_pdf}")

# Folder containing the PNG files
source_folder = 'book_2023-12-15_15-25-50'

# Output PDF file name
output_pdf = 'output.pdf'

# Maximum size of images and JPEG quality
max_image_size = (1280, 720)  # Adjust as needed
jpeg_quality = 85  # Adjust as needed

pngs_to_pdf(source_folder, output_pdf, max_image_size, jpeg_quality)
