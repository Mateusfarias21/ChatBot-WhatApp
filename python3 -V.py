from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

#Aqui ele abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #Aqui Abre o Zap Zap
time.sleep(30) #Tempo de logar com QRCODE

#Aqui coloco o nome do Contato/Grupos que vai enviar mensagem
contatos = ['GRUPO TESTE']


#Messagem que vai enviar

mensagem = 'Robozinho do zap '
mensagem2 = '     ,Desenvolvido Pelo Farias'

#Midia = Imagem que vou colocar para enviar
midia = "C:/Users/ADMINISTRATOR/Pictures/Meurobo.jpg"

#Funcao que pesquisa o Contato/Grupo do zap
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagem,mensagem2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(5)
    campo_mensagem[1].send_keys(str(mensagem) + str(contato) + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)


#Funcao que envia midia como mensagem
def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(5)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click() 

#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem,mensagem2)       
    enviar_midia(midia) 
    time.sleep(1)