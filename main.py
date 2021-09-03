import base64
from selenium import webdriver
import time
from PIL import Image


def screenshot_all_page(blink):
    imagelist = []
    driver = webdriver.Firefox()
    driver.set_window_size(500, 800)
    driver.get(blink)
    time.sleep(5)
    for this_p in range(int(driver.find_element_by_xpath('//*[@id="totalPages"]').text)):
        canvas = driver.find_element_by_css_selector("#canvas0")
        canvas_base64 = driver.execute_script(f"return arguments[0].toDataURL('image/png').substring(21);", canvas)
        canvas_png = base64.b64decode(canvas_base64)
        with open(rf"book/{this_p}.png", 'wb') as f:
            f.write(canvas_png)
        driver.find_element_by_id('___nextPageMobile').click()

        image = Image.open(f'book/{this_p}.png')
        image.load()
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])
        imagelist.append(background)
    imagelist[0].save(f'book/shit.pdf', save_all=True, append_images=imagelist)


blink = "https://reader.taaghche.com/book/66260/%D8%A7%DB%8C%D8%AF%D9%87-%DB%8C-%D8%B9%D8%A7%D9%84%DB%8C-%D9%85%D8%B3%D8%AA%D8%AF%D8%A7%D9%85?f=false"
screenshot_all_page('shit', blink)
