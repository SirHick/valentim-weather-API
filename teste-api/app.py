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

link_api = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "São Paulo", #cidade para qual queremos obter os dados
    "lang": "pt" #Linguagem
}

#Armazenando a resposta da requisição na variável resposta

resposta = requests.get(link_api, params = parametros)

print(resposta)

print(resposta.content)