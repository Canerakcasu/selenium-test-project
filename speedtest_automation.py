from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("Speedtest.net açılıyor...")
    driver.get("https://www.speedtest.net/")

    print("5 saniye bekleniyor...")
    time.sleep(5)


    print("Başlat butonu aranıyor...")
    go_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
    )
    print("Başlat butonuna tıklanıyor...")
    go_button.click()

    print("Test devam ediyor, lütfen bekleyin...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-data"))
    )

    # Download and upload speeds
    download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
    upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text

    print(f"İndirme Hızı: {download_speed} Mbps")
    print(f"Yükleme Hızı: {upload_speed} Mbps")

except Exception as e:
    print(f"Hata oluştu: {e}")

finally:
    print("Tarayıcı kapatılıyor...")
    driver.quit()
