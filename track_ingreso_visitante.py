from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()

try:
    driver.get("https://app.sportclub.com")  # URL real o de prueba
    time.sleep(3)

    # Simular clic en "Ingresar sin registro"
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Ingresar sin registro')]")
    btn.click()
    time.sleep(2)

    # Validar ingreso exitoso
    assert "Clubes" in driver.page_source

    # Simular registro del evento
    evento = {
        "event": "ingreso_sin_registro",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "selenium_test",
        "tipo_usuario": "visitante"
    }

    r = requests.post("https://mi-api.com/metricas", json=evento)
    print("Evento enviado:", r.status_code)

finally:
    driver.quit()