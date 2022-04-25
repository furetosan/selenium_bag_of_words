# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

# inicializar o chromedriver no selenium

chrom = webdriver.Chrome()
#chrom.get('http://google.com')
## copied xpath for search input element


# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input

chrom.get('http://google.com/search?q=o+que+é+website')

# 1. acima - escolher uma forma de pegar os resultados da busca
# 2. guardar textos e links de cada resultado para visita posterior
# 3. iterar visitando e salvando todo o texto de todos os elementos de
#   cada pagina dos resultados (por enquanto da primeira pagina)

# //*[@id="rso"]/div[7]/div/div/div[1]
elementos = chrom.find_elements(by=By.XPATH,value='//*[@id="rso"]/*/div/*/div/a')

# rso = results search organic?

lista_de_sites = []
for i in range(len(elementos)):
    print(elementos[i].text)
    print(elementos[i].get_attribute('href'))
    site_a_visitar = {}
    site_a_visitar['text'] = elementos[i].text
    site_a_visitar['href'] = elementos[i].get_attribute('href')
    lista_de_sites.append(site_a_visitar)

textos = []
for s in lista_de_sites:
    chrom.get(s['href'])
    texto = chrom.find_element(by=By.XPATH,value="/html/body").text
    print(texto)
    textos.append(texto)

chrom.close()
## fe-show!

# de fato, consigo agora pegar os textos das paginas .. web semantics?
