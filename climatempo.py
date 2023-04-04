import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Instancia o driver do chrome e desabilita os logs
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)

# Entra no site do google e procura todas as informações necessarias
estado = input("Digite o nome do seu estado: ")
driver.get("https://www.google.com/search?q=clima+agora+"+estado.replace(" ","+"))
cidadenome = driver.find_element('xpath','//*[@id="oFNiHe"]/div/div/div/div[1]/span[2]').text
tempmin = driver.find_element('xpath','//*[@id="wob_dp"]/div[1]/div[3]/div[2]/span[1]').text
tempmax = driver.find_element('xpath','//*[@id="wob_dp"]/div[1]/div[3]/div[1]/span[1]').text
chuva = driver.find_element('xpath','//*[@id="wob_pp"]').text
vento = driver.find_element('xpath', '//*[@id="wob_ws"]').text
umidade = driver.find_element('xpath','//*[@id="wob_hm"]').text
temperatura = driver.find_element('xpath','//*[@id="wob_tm"]').text
infohoje = driver.find_element('xpath','//*[@id="wob_dc"]').text
tempo = driver.find_element('xpath','//*[@id="wob_dts"]').text
time.sleep(1)

print(f"Temperatura: {temperatura}°C   🏙 Cidade: {cidadenome}")
print(f"\u2B06 Minima: {tempmin}° \u2B07 Maxima: {tempmax}°")
print("\u2614 Chuva: " + chuva)
print("🍃 Vento: " + vento)
print("Umidade: " + umidade)
print("Situação: " + infohoje)
print(tempo)
# Fecha o driver para evitar de ficar aberto
driver.close()