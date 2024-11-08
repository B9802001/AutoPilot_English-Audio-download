from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# 取得YouTube網址
youtube_url = input("請輸入YouTube網址：")

# 開啟網頁
driver = webdriver.Chrome()  # 使用ChromeDriver，請確保已安裝對應的驅動程式
driver.get("https://y2mate.nu/en-6X3r/")

try:
    # 找到輸入欄位，輸入網址
    input_field = driver.find_element(By.ID, "video")  # 假設欄位ID是"input"，請確認實際的ID
    input_field.send_keys(youtube_url)
    print("網址已經輸入")

    # 模擬按下 "Convert" 按鈕
    convert_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # 使用XPath來定位提交按鈕
    convert_button.click()
    print("convert按鈕已點擊")

    # 每10秒檢查是否出現 "Download" 按鈕
    download_button_found = False
    while not download_button_found:
        try:
            # 找到Download按鈕（假設按鈕ID為 "download" 或者你可以確認實際的ID或其他屬性）
            download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download')]")
            download_button.click()
            download_button_found = True
            print("Download 按鈕已點擊！")

        except NoSuchElementException:
            print("尚未找到 Download 按鈕，等待 10 秒後重試...")
            time.sleep(10)

except Exception as e:
    print("出現錯誤:", e)

# 關閉瀏覽器
finally:
    print("等待20秒後關閉")
    time.sleep(20)
    driver.quit()
