import time
from bs4 import BeautifulSoup
import requests
import argparse

# Instancia o ArgumentParser
parser = argparse.ArgumentParser(prog='ClimaTempo',description="Veja o clima de hoje direto do seu terminal!")

#Adiciona o argumento "--local" com explicação
parser.add_argument('-l', '--local', help='especifique um local', default='+')
args = parser.parse_args()

# Entra no site do google e procura todas as informações necessarias
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
html = requests.get(f"https://www.google.com/search?q=clima+agora+{args.local}", headers=headers).content
soup = BeautifulSoup(html, 'html.parser')
body = soup.find("body")

time.sleep(1)

cidadenome = soup.find("span", class_="BBwThe").text
tempmin = soup.select_one("#wob_dp > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)").text
tempmax = soup.select_one("#wob_dp > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1)").text
temperatura = soup.select_one("#wob_tm").text
chuva = soup.select_one("#wob_pp").text
vento = soup.select_one("#wob_ws").text
umidade = soup.select_one("#wob_hm").text
infohoje = soup.select_one("#wob_dc").text
tempo = soup.select_one("#wob_dts").text.capitalize()
print(f"Temperatura: {temperatura}°C   🏙 Cidade: {cidadenome}")
print(f"\u2B06 Minima: {tempmin}° \u2B07 Maxima: {tempmax}°")
print("\u2614 Chuva: " + chuva)
print("🍃 Vento: " + vento)
print("Umidade: " + umidade)
print("Situação Hoje: " + infohoje)
print(tempo)