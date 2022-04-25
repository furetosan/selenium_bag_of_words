# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
## !!! nuxt dont need no import

chrom = webdriver.Chrome()
chrom.get("http://google.com/search?q=o+que+é+website")
elementos = chrom.find_elements(by=By.XPATH, value='//*[@id="rso"]/*/div/*/div/a')

lista_de_sites = []
for i in range(len(elementos)):
    print(elementos[i].text)
    print(elementos[i].get_attribute("href"))
    site_a_visitar = {}
    site_a_visitar["text"] = elementos[i].text
    site_a_visitar["href"] = elementos[i].get_attribute("href")
    lista_de_sites.append(site_a_visitar)

textos = []
for s in lista_de_sites:
    chrom.get(s["href"])
    texto = chrom.find_element(by=By.XPATH, value="/html/body").text
    print(texto)
    textos.append(texto)

print([s for s in lista_de_sites])
print([t for t in textos])

chrom.close()
#get_ipython().run_line_magic('save', '1-13 mateste02.py')
