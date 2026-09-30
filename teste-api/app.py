#UMA API É UM JEITO DE CONECTAR SISTEMAS OU INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTES SISTEMAS DE SOFTWARE
#SE COMUNIQUEM E TROQUEM DADOS ENTRE SI.

#NESTE EXEMPLO, SERÁ UTILIZADA A WEATHERapi.com PARA CONSULTAR AS CONDIÇÕES CLIMÁTICAS
#DE UMA DETERMINADA LOCALIDADE;

#CONSULTAR API ->
#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UMA CERTA CAPACIADADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA.

#API-KEY --> minha credencial para utilizar a plataforma

import requests #bibliotecas para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir os dados de forma legível

api_key = "813566133ff747e98c1224430262909"

link_api = "https://api.weatherapi.com/v1/current.json"

variavel_cidade = input("Digite o nome da cidade desejada: ")

hora_desejada = input("Digite o horário desejado: ")

com_polen = input("Quer pesquisar a qualidade do ar? (sim ou não): ")

aqi_opcao = "sim" if com_polen in ["sim", "s"] else "no"

parametros = {
    "key": api_key,
    "q": variavel_cidade, #cidade para qual queremos obter os dados
    "hour": hora_desejada,
    "aqi": aqi_opcao,
    "lang": "de" #Linguagem
}

#Armazenando a resposta da requisição na variável resposta

resposta = requests.get(link_api, params = parametros)

print(resposta, "\n")

print(resposta.content)

if resposta.status_code == 200:
    print("\nRequisição realizada com sucesso.")
    dados = resposta.json() #armazenando os dados em formato de JSON na variável dados
    pprint(dados)
    hora = dados["location"]["localtime"]
    cidade = dados["location"]["name"]
    temperatura = dados["current"]["temp_c"]
    descricao = dados["current"]["condition"]["text"]
    pollen = dados["current"]["pollen"]["Ragweed"]
    print(f"\nA temperatura atual em {cidade}, no horário {hora} é de {temperatura}°C")
    print(f"Descrição do clima é: {descricao}")
    print(f"O pólen tá assim: {pollen} grãos/m³")
else:
    print("\nErro na requisição.")