import streamlit as st

from bs4 import BeautifulSoup
import requests
#cidade = input('Digite a cidade').replace(' ', '-').lower()
#print(cidade)
site ='https://www.accuweather.com/pt/br/conselheiro-lafaiete/33787/weather-forecast/33787'
#print(site)
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}


resposta = requests.get(site ,headers=headers,verify=False)
sopa = BeautifulSoup(resposta.text , 'html.parser')

climas= sopa.find_all('span' , class_="temp-hi")
localidade = sopa.find('h1')
previsao = sopa.find_all('p',class_="no-wrap")
dias = sopa.find_all('p',class_="day")

for i, clima in enumerate(climas):
    st.write(f'### {dias[i].text.capitalize()}\n ', f'\n #### A temperatura é: {clima.text}C\n' , f'\nE a previsao para o dia será de :  {previsao[i].text}')
    st.write('-'*50)
