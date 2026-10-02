#UMA API É UM JEITO DE CONECTAR SISTEMAS OU INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTES SISTEMAS DE SOFTWARE
#SE COMUNIQUEM E TROQUEM DADOS ENTRE SI.

#NESTE EXEMPLO, SERÁ UTILIZADA A WEATHERapi.com PARA CONSULTAR AS CONDIÇÕES CLIMÁTICAS
#DE UMA DETERMINADA LOCALIDADE;

#CONSULTAR API ->
#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UMA CERTA CAPACIADADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA.

#API-KEY --> minha credencial para utilizar a plataforma

import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém a chave do arquivo .env
api_key = os.getenv("API_KEY")

# Alterado para o endpoint de previsão (forecast)
link_api = "https://api.weatherapi.com/v1/forecast.json"

variavel_cidade = input("Digite o nome da cidade desejada: ")
hora_input = input("Digite a hora desejada (0 a 23 ou ex: 14:00): ")
com_polen = input("Quer pesquisar a qualidade do ar? (sim ou não): ")

# Extrai apenas o número da hora (ex: transforma "14:00" em 14)
try:
    hora_int = int(hora_input.split(":")[0].strip())
except ValueError:
    hora_int = 12  # Valor padrão caso o usuário digite um formato inválido

# A WeatherAPI espera "yes" ou "no" para o parâmetro aqi
aqi_opcao = "yes" if com_polen.lower() in ["sim", "s"] else "no"

parametros = {
    "key": api_key,
    "q": variavel_cidade,
    "days": 1,  # Previsão para o dia atual
    "hour": hora_int,  # Filtra a hora específica (0 a 23)
    "aqi": aqi_opcao,
    "lang": "pt",
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    print("\nRequisição realizada com sucesso.")
    dados = resposta.json()

    # Acessa os dados retornados para a hora filtrada
    dados_hora = dados["forecast"]["forecastday"][0]["hour"][0]

    cidade = dados["location"]["name"]
    horario_previsto = dados_hora["time"]
    temperatura = dados_hora["temp_c"]
    descricao = dados_hora["condition"]["text"]

    print(
        f"\nA previsão para {cidade} no horário {horario_previsto} é de"
        f" {temperatura}°C"
    )
    print(f"Descrição do clima: {descricao}")
else:
    print("\nErro na requisição. Verifique sua chave ou os dados digitados.")