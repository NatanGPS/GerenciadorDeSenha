import  sqlite3

from PySimpleGUI import PySimpleGUI as sg 

class GereciadorDeSenhas():
    
    def __init__(self):

        self.respostas = ['nova', 'serviços', 'ver', 'sair']

        # cria uma senha mestra
        self.max_password = '3452'

        # cria a pasta pra servir de banco de dados e me conecto a ela
        self.conn = sqlite3.connect('passwords.db')

        self.cursor = self.conn.cursor()

        # Cria uma tabela com algumas opções, caso essa tabela ja não exista usuarios
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS users(
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );  

        ''')    
    

    def Iniciar(self):
        self.senha_op = input('Qual a senha mestre?')
       
        if self.senha_op != self.max_password:
            print('Senha Inválida! Encerrando...')
            exit()
        else:
            print('Senha Validada! Seja bem vindo ao Gerenciador')

        while True:
            self.menu()
            self.op = input('O que voce deseja fazer?')

            if self.op not in self.respostas:
                print(" Essa opção não é válida!")
                continue

                    
            if self.op == 'sair':
                break

                
            if self.op == 'nova':
                service = input('Qual o serviço? ')
                username = input('Qual o username? ')
                password = input(' Qual a senha ? ')
                self.inserir_senha(service, username, password)
                print('Dados salvos com sucesso!')
                        
                        
            if self.op == 'serviços':
                self.mostrar_servicos()


            if self.op == 'ver':
                service = input('Qual serviço voce deseja saber a senha?')
                self.get_password(service)

            self.conn.close()

    # Define um menu pra ser printado3
    def menu(self):
        print('==========================================')
        print('= nova : Para inserir nova senha         =')
        print('= serviços : Para ver os serviços salvos =')
        print('= ver  : Para recuperar uma senha        =')
        print('= sair : Para sair                       =')
        print('==========================================')



    def get_password(self, service):
        self.cursor.execute(f'''
            SELECT username, password FROM users
            WHERE service = '{service}'
    ''' )
        
        
        if self.cursor.rowcount == 0:
            print('Esse serviço não está no nosso sistema, por favor use a opção " serviços" para verificar seus serviços')
        else:
            for user in self.cursor.fetchall():
                print(user)




    def inserir_senha(self, service, username, password):
        self.cursor.execute(f''' 
            INSERT INTO users (service, username, password)
            VALUES ('{service}', '{username}', '{password}')
        ''')
        self.conn.commit()


    def mostrar_servicos(self):
        self.cursor.execute(''' 
            SELECT service FROM users;
        ''')
        for service in self.cursor.fetchall():
            print(service)



rodar = GereciadorDeSenhas()
rodar.Iniciar()



