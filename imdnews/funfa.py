# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:24:33 2019

@author: tauab
"""
import importlib.util
spec = importlib.util.spec_from_file_location("models.py", "C:\\Users\\tauab\\Desktop\\WebScrappingRestDjango\\imdnews\\models.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
from spec import news
#from C:/Users/tauab/Desktop/WebScrappingRestDjango/imdnews import news
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
url = 'https://www.imd.ufrn.br/portal/noticias'
webPage = urlopen(url)
pageHTML = webPage.read()
webPage.close()
#html parser
page_soup = bs(pageHTML, "html.parser")

cartoes_texto = page_soup.findAll("div", {"class":"card-block p-2"})

listaTituloCartao = []
listaTextoCartao = []
listaDataCartao = []

for cartaoDummy in cartoes_texto:
    listaTituloCartao.append(cartaoDummy.h4.text)
    listaTextoCartao.append(cartaoDummy.p.text)
    listaDataCartao.append(cartaoDummy.div.text.split('\n')[1].split('por')[0])

lista_final = [[],[],[]]

lista_final[0].extend(listaTituloCartao)
lista_final[1].extend(listaTextoCartao)
lista_final[2].extend(listaDataCartao)


for i in range (0,len(lista_final[0])):
        a = news(title = lista_final[0][i], text = lista_final[1][i], date = lista_final[2][i])
        a.save()
        