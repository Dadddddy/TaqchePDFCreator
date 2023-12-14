import base64
import os
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


def screenshot_all_page(login_page_url):
    # Check if the 'book' directory exists and create it if not
    if not os.path.exists('book'):
        os.makedirs('book')
    imagelist = []
    driver = webdriver.Firefox()
    driver.set_window_size(791, 671)

    # Navigate to the login page
    driver.get(login_page_url)
    print("Waiting for 60 seconds...")
    time.sleep(60)

    try:
        current_page = int(driver.find_element(By.XPATH, '//*[@id="pageNo"]').text)
        print("Current Pages: " + str(current_page))
        totalPages = int(driver.find_element(By.XPATH, '//*[@id="totalPages"]').text)
        print("Total Pages: " + str(totalPages))

        this_p = 1
        while current_page != totalPages:
            time.sleep(1)
            canvas = driver.find_element(By.CSS_SELECTOR, "#canvas0")
            canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
            canvas_png = base64.b64decode(canvas_base64)
            with open(f"book/{this_p}.png", 'wb') as f:
                f.write(canvas_png)

            driver.find_element(By.ID, '___nextPageMobile').click()

            image = Image.open(f'book/{this_p}.png')
            image.load()
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])
            imagelist.append(background)
            this_p += 1
            current_page = int(driver.find_element(By.XPATH, '//*[@id="pageNo"]').text)
        # Save the first image as PDF and append the rest
        if imagelist:
            imagelist[0].save('book/book.pdf', save_all=True, append_images=imagelist[1:])
        # Close the images after PDF creation
        for image in imagelist:
            image.close()
        print("Number of SCs: " + str(this_p))
    finally:
        driver.quit()

# URL of the login page
login_page_url = "https://taaghche.com/"
screenshot_all_page(login_page_url)
