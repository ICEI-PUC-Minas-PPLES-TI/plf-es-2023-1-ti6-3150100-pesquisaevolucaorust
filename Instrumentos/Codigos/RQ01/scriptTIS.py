from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import time
from datetime import datetime
import os


# Inicializa o driver do Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Navega até a página de login do LinkedIn
driver.get("https://www.linkedin.com/login")

# Digita o e-mail e senha e clica no botão de login
email_input = driver.find_element(By.ID, "username")
email_input.send_keys("login")
password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("senha")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
login_button.click()

# Aguarda a página ser carregada antes de navegar para a página de empregos
wait = WebDriverWait(driver, 15)
wait.until(EC.title_contains("Feed"))

# Navega até a URL do LinkedIn Jobs
driver.get("https://www.linkedin.com/jobs")

# Aguarda a página ser carregada antes de procurar o campo de pesquisa
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Pesquisar cargo, competência ou empresa']")))

# Digita "RUST" no campo de pesquisa e pressiona Enter
search_input.send_keys(" ", Keys.ENTER)
time.sleep(2)

# Clica no filtro "Data do anúncio"
botao = driver.find_element(By.XPATH, '//button[text()="Data do anúncio"]')
botao.click()
time.sleep(1)

# Seleciona a opção de "Últimas 24 horas"
search_input = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label")
search_input.click()
time.sleep(1)

# Clica no botão para filtrar
search_input = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span")
search_input.click()
time.sleep(2)

linguagens = ["RUST","JavaScript","Python","Java","C#","PHP","TypeScript","Swift","Kotlin","Dart"]
regioes = ["Europe", "USA", "Brazil", "Australia", "Asia", "Canada"]

cabecalho = ""
linha = ""

for linguagem in linguagens:
   
    # Limpa o campo de pesquisa e digita a linguagem
    search_input = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[1]/div/div/input[1]")
    search_input.clear()
    search_input.send_keys(linguagem, Keys.ENTER)
    time.sleep(2)

    for regiao in regioes:

        # Limpa o campo de local e seleciona o pais
        search_input = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
        search_input.clear()
        search_input.send_keys(regiao, Keys.ENTER)
        time.sleep(2)

        try:
            # Aguarda o resultado da pesquisa ser carregado antes de extrair o número de vagas
            result = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/header/div[1]/small")
            result = result.text.split()[0]
        except:
            result = 0

        cabecalho += linguagem + "/" + regiao + ","
        linha += str(result) + ","
        print(result)
        time.sleep(2)

linha = linha[:-1]
cabecalho = cabecalho[:-1]


arquivo = 'C:\\Users\\Dell\\Desktop\\TESTE_SELENIUM\\RESULT_TIS\\results.csv'

if os.path.exists(arquivo):
    # Se o arquivo existe, adiciona uma linha no final
    with open(arquivo, 'a') as f:
        f.write(linha + "\n")
else:
    # Se o arquivo não existe, cria o arquivo e adiciona a linha
    with open(arquivo, 'w') as f:
        f.write(cabecalho + "\n")
        f.write(linha + "\n")
