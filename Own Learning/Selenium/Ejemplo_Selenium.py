from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
print(driver.title)  # Esto debería imprimir el título de la página de Google
driver.quit()
