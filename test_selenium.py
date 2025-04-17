from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True  # Отключает открытие браузера на экране (необязательно)

service = Service()  # Geckodriver автоматически используется из PATH
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.example.com")
print("Title:", driver.title)


