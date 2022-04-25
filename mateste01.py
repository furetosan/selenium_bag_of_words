# coding: utf-8
from selenium import webdriver
chrom = webdriver.Chrome()
from selenium.webdriver.common.by import By
chrom.get('http://google.com')
busca = chrom.find_element('//body/*/form/*/input/')
busca = chrom.find_element(by=By.XPATH,value='//body/*/form/*/input/')
busca = chrom.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
busca.send_keys('website')
busca.send_keys('\n')
# get_ipython().run_line_magic('save', 'mateste01.py 1-10')
