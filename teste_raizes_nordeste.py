# Projeto Multidisciplinar: Rede Raízes do Nordeste (App/Totem)
# Aluno: Ramirez Morais de Melo
# RU: 4594148
# Ênfase: Qualidade de Software

import subprocess
import sys
import platform

def verificar_ambiente():
    # Verifica a versão do Python
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    if sys.version_info < (3, 7):
        print("Erro: Este script requer Python 3.7 ou superior.")
        print(f"Sua versão atual é: {sys.version}")
        sys.exit(1)
    else:
        print(f"Versão do Python: {sys.version.split()[0]} - OK!")

    # Verifica e instala Selenium
    try:
        from selenium import webdriver
        print("Biblioteca Selenium já está presente no sistema.")
    except ImportError:
        print("A biblioteca 'Selenium' não foi encontrada.")
        escolha = input("Deseja que eu realize a instalação agora ? (s/n): ").lower()
        if escolha == 's':
            print("Iniciando instalação via pip, por favor aguarde...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
            print("Instalação concluída com sucesso!")
        else:
            print("Operação cancelada. O script não pode prosseguir sem o Selenium.")
            sys.exit(1)


verificar_ambiente()

# Início dos testes
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (Exemplo usando Chrome)
driver = webdriver.Chrome()

def test_login_invalido_fidelidade():
    try:
        # 1. Acessa a URL (fictícia) do portal de fidelidade Raízes do Nordeste
        driver.get("http://localhost:8000/fidelidade/login") 
        
        # 2. Localiza os campos de entrada (IDs fictícios)
        campo_cpf = driver.find_element(By.ID, "cpf_cliente")
        campo_senha = driver.find_element(By.ID, "senha_acesso")
        botao_entrar = driver.find_element(By.ID, "btn_login")

        # 3. Simula entrada de dados inválidos (Teste de barreira do sistema)
        campo_cpf.send_keys("000.000.000-00")
        campo_senha.send_keys("senha_errada_123")
        botao_entrar.click()

        # 4. Verifica se a mensagem de erro apareceu (Resultado Esperado)
        time.sleep(2) 
        mensagem_erro = driver.find_element(By.CLASS_NAME, "alert-danger").text
        
        if "inválido" in mensagem_erro.lower():
            print("Teste CT001: PASSOU - Sistema barrou acesso indevido aos dados do cliente.")
        else:
            print("Teste CT001: FALHOU - Sistema não exibiu alerta de erro.")

    except Exception as e:
        print(f"Erro na execução do teste: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_invalido_fidelidade()
