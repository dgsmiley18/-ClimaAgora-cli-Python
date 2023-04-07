import time
from bs4 import BeautifulSoup
import requests
import argparse

def pegar_tempo_info(local):
    # Entra no site do google e procura todas as informações necessárias
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    html = requests.get(f"https://www.google.com/search?q=clima+agora+{local}", headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')

    # Encontra as informações necessárias
    cidade_nome = soup.find("span", class_="BBwThe").text
    temp_min = soup.select_one("#wob_dp > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)").text
    temp_max = soup.select_one("#wob_dp > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1)").text
    temperatura = soup.select_one("#wob_tm").text
    chuva = soup.select_one("#wob_pp").text
    vento = soup.select_one("#wob_ws").text
    umidade = soup.select_one("#wob_hm").text
    info_hoje = soup.select_one("#wob_dc").text
    tempo = soup.select_one("#wob_dts").text.capitalize()
    try:
        tipo_alerta = soup.select_one(".vk_h").text
        alerta_hora = soup.select_one("div.Uekwlc:nth-child(3)").text
        mais_info = soup.select_one("div.Uekwlc:nth-child(5) > a:nth-child(1)").text
    except:
        tipo_alerta = "Alerta: Nenhum"
        alerta_hora = ""
        mais_info = ""


    return {
        "cidade_nome": cidade_nome,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "temperatura": temperatura,
        "chuva": chuva,
        "vento": vento,
        "umidade": umidade,
        "info_hoje": info_hoje,
        "tempo": tempo,
        "tipo_alerta": tipo_alerta,
        "alerta_hora": alerta_hora,
        "mais_info": mais_info
    }

if __name__ == "__main__":
    # Instancia o ArgumentParser
    parser = argparse.ArgumentParser(prog='ClimaTempo',description="Veja o clima de hoje direto do seu terminal!")

    #Adiciona o argumento "--local" com explicação
    parser.add_argument('-l', '--local', help='especifique um local', default='+')
    args = parser.parse_args()

    # Mostra as informações na tela
    info = pegar_tempo_info(args.local)
    print(f"🏙 Cidade: {info['cidade_nome']}")
    print(f"🌡️ Temperatura: {info['temperatura']}°C")
    print(f"\u2B06 Minima: {info['temp_min']}° \u2B07 Maxima: {info['temp_max']}°")
    print("\u2614 Chuva: " + info['chuva'])
    print("🍃 Vento: " + info['vento'])
    print("Umidade: " + info['umidade'])
    print("Situação Hoje: " + info['info_hoje'])
    print(info['tempo'])
    print("\033[33m{}\033[0m".format(info['tipo_alerta']))
    print("\033[33m{}\033[0m".format(info["alerta_hora"]))
    print("\033[33m{}\033[0m".format(info["mais_info"]))
