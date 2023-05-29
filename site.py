from selenium import webdriver
from selenium.webdriver.common.by import By


class Colombo:
    def __init__(self):
        self.celular = {
                'samsung':'https://www.colombo.com.br/produto/Smartphone-e-Celular/Samsung',
                'motorola':'https://www.colombo.com.br/produto/Smartphone-e-Celular/Motorola',
                'xiaomi':'https://www.colombo.com.br/produto/Smartphone-e-Celular/Xiaomi',
                'lg':'https://www.colombo.com.br/produto/Smartphone-e-Celular/LG',
                'positivo':'https://www.colombo.com.br/produto/Smartphone-e-Celular/Positivo',
                'nome': '/html/body/div[1]/div/section[2]/div/div[7]/main/div[2]/ul/li[name]/a/h2',
                'preco': '/html/body/div[1]/div/section[2]/div/div[7]/main/div[2]/ul/li[dindin]/a/div[3]/p[2]/span[2]'
        }
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.samsung()
        self.motorola()
        self.xiaomi()
        self.lg()
        self.positivo()

    def samsung(self):
        self.driver.get(self.celular['samsung'])  # abrir e fechar site
        try:
            for marca1 in range(1, 11):
                print(marca1, end=' ')
                print(self.driver.find_element(By.XPATH, self.celular['nome'].replace('name', str(marca1))).text)
                print(self.driver.find_element(By.XPATH, self.celular['preco'].replace('dindin', str(marca1))).text)
                
            print('')
        finally:
            pass
        
    def motorola(self):
        self.driver.get(self.celular['motorola'])  # abrir e fechar site
        try:
            for marca2 in range(1, 11):
                print(marca2, end=' ')
                print(self.driver.find_element(By.XPATH, self.celular['nome'].replace('name', str(marca2))).text)
                print(self.driver.find_element(By.XPATH, self.celular['preco'].replace('dindin', str(marca2))).text)
                
            print('')
        finally:
            pass

    def xiaomi(self):
        self.driver.get(self.celular['xiaomi'])  # abrir e fechar site
        try:
            for marca3 in range(1, 11):
                print(marca3, end=' ')
                print(self.driver.find_element(By.XPATH, self.celular['nome'].replace('name', str(marca3))).text)
                print(self.driver.find_element(By.XPATH, self.celular['preco'].replace('dindin', str(marca3))).text)
                
            print('')
        finally:
            pass
        
    def lg(self):
        self.driver.get(self.celular['lg'])  # abrir e fechar site
        try:
            for marca4 in range(1, 11):
                print(marca4, end=' ')
                print(self.driver.find_element(By.XPATH, self.celular['nome'].replace('name', str(marca4))).text)
                print(self.driver.find_element(By.XPATH, self.celular['preco'].replace('dindin', str(marca4))).text)
                
            print('')
        finally:
            pass
        
    def positivo(self):
        self.driver.get(self.celular['positivo'])  # abrir e fechar site
        try:
            for marca5 in range(1, 11):
                print(marca5, end=' ')
                print(self.driver.find_element(By.XPATH, self.celular['nome'].replace('name', str(marca5))).text)
                print(self.driver.find_element(By.XPATH, self.celular['preco'].replace('dindin', str(marca5))).text)
                
            print('')
        finally:
            pass

teste = Colombo()
