import base64
import io
import os
import sys
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

from PIL import Image, ImageEnhance
import io

from PIL import Image, ImageEnhance
import io

def resize_and_convert_png_to_jpg(image_path, max_size=(1280, 720), quality=85, contrast_factor=50, brightness_factor=0.01):
    """
    Resize and convert a PNG image to JPEG, enhancing the contrast and brightness of the text.
    Args:
        image_path (str): Path to the PNG image.
        max_size (tuple): Maximum size of the image (width, height).
        quality (int): Quality of the output JPEG image.
        contrast_factor (float): Factor by which to increase the contrast.
        brightness_factor (float): Factor by which to adjust the brightness.
    Returns:
        PIL.Image: Resized and converted JPEG image.
    """
    with Image.open(image_path) as img:
        # Resize the image, maintaining aspect ratio
        img.thumbnail(max_size, Image.Resampling.LANCZOS)

        # Enhance the contrast
        contrast = ImageEnhance.Contrast(img)
        img = contrast.enhance(contrast_factor)

        # Enhance the brightness
        brightness = ImageEnhance.Brightness(img)
        img = brightness.enhance(brightness_factor)

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
    """
       Convert PNG images in a folder to a single PDF.
       Args:
           source_folder (str): Path to the folder containing PNG images.
           output_pdf (str): Path for the output PDF file.
           max_image_size (tuple): Maximum size of images.
           jpeg_quality (int): Quality of JPEG images.
       """
    imagelist = []

    for i in range(1, 7):
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

    print(f"\nPDF created successfully: {os.path.abspath(output_pdf)}")

def screenshot_all_page(login_page_url, directory_name):
    """
        Take screenshots of all pages of a web application.
        Args:
            login_page_url (str): URL of the login page.
            directory_name (str): Directory name to save the screenshots.
    """
    # Check if the 'book' directory exists and create it if not
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    driver = webdriver.Firefox()
    driver.set_window_size(791, 671)

    # Navigate to the login page
    driver.get(login_page_url)
    print("Waiting for 60 seconds...")
    time.sleep(45)

    try:
        current_page = int(driver.find_element(By.XPATH, '//*[@id="pageNo"]').text)
        print("Current Pages: " + str(current_page))
        totalPages = int(driver.find_element(By.XPATH, '//*[@id="totalPages"]').text)
        print("Total Pages: " + str(totalPages))

        this_p = 1
        while current_page != totalPages:
            sys.stdout.write(f"\rNumber of screenshots taken: {this_p}")
            sys.stdout.flush()
            time.sleep(1)
            canvas = driver.find_element(By.CSS_SELECTOR, "#canvas0")
            canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
            canvas_png = base64.b64decode(canvas_base64)
            with open(f"{directory_name}/{this_p}.png", 'wb') as f:
                f.write(canvas_png)

            driver.find_element(By.ID, '___nextPageMobile').click()
            this_p += 1
            current_page = int(driver.find_element(By.XPATH, '//*[@id="pageNo"]').text)
        print("Number of screen shots: " + str(this_p))
    finally:
        driver.quit()


def user_input_prompt():
    """
    Prompt the user for an action choice.
    Returns:
        str: User's choice.
    """
    print("Select an action:\n1. Screenshot All Pages\n2. Convert Screen shots to PDF\n3. Exit")
    return input("Enter your choice (1, 2, or 3): ")


def main():
    """
    Main function to execute the script.
    """
    choice = user_input_prompt()

    if choice == '1':
        # URL of the login page
        login_page_url = input("Enter the URL of the login page: ")
        directory_name = input("Enter the Directory name for saving the screen shots: ")
        screenshot_all_page(login_page_url, directory_name)

    elif choice == '2':
        source_folder = input("Enter the source folder path: ")
        output_pdf = input("Enter the output PDF file name (e.g. output.pdf): ")
        max_image_size = (1280, 720)  # Adjust as needed
        jpeg_quality = 85  # Adjust as neededل

        pngs_to_pdf(source_folder, output_pdf, max_image_size, jpeg_quality)

    elif choice == '3':
        print("Exiting program.")
        sys.exit(0)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)


if __name__ == "__main__":
    main()