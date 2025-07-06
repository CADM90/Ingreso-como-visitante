from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()

try:
    driver.get("https://app.sportclub.com")  # URL real o staging
    time.sleep(3)

    # Clic en “Hacerse socio”
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Hacerse socio')]")
    btn.click()
    time.sleep(2)

    # Validar llegada a formulario
    assert "Formulario" in driver.page_source or "Registro" in driver.page_source

    # Enviar métrica simulada
    evento = {
        "event": "click_hacerse_socio",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "selenium_test",
        "intencion_conversion": True
    }

    r = requests.post("https://mi-api.com/metricas", json=evento)
    print("Evento enviado:", r.status_code)

finally:
    driver.quit()