import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Создаем настройки браузера
options = webdriver.ChromeOptions()

# Предотвращаем закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)

# Запускаем Chrome с автоматически установленным драйвером и заданными опциями
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовые данные
base_url = "http://www.saucedemo.com/"
valid_username = "performance_glitch_user"
valid_password = "secret_sauce"

# Генерация имени скриншота с датой, когда он был сделан
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
screenshot_name = f"screenshot_{now_date}.png"

# Переход на страницу авторизации  и разворачивание окна на весь экран
driver.get(base_url)
driver.maximize_window()

# Ввод логина
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(valid_username)
print("Input login")

# Ввод пароля
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_password)
print("Input password")

# Клик по кнопке "Login"
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click login button")

# Сделать скриншот страницы
time.sleep(3)
driver.save_screenshot(
    f'C:\\Users\\admin\\PycharmProjects\\AutoTesting\\selenium_home_works\\screen\\ {screenshot_name}'
)
print("Screenshot made")

# Выход из браузера
driver.quit()
print("Browser is closed")