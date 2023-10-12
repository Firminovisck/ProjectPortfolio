from http.server import HTTPServer, BaseHTTPRequestHandler # Importar do Módulo http.server o HTTPServer e o BaseHTTPRequestHandler
from types import TracebackType

class MainServer(BaseHTTPRequestHandler): #Criação do Server Herdando os métodos do BaseHTTPRequestHandler
    def do_GET(self) -> object: #do_GET é um dos métodos do BaseHTTPRequestHandler que permite Receber Get Requests
        if self.path == '/': #Definição do caminho onde estará o arquivo que o usuário irá acessar
            self.path = '/DiagEventList.html' #Arquivo a ser exibido
            try:  
                open_file = open(self.path[1:],).read() # O .read deste caso tem o objetivo de exibir na tela o texto ou as informações que estão dentro do 'open_file'
                                                        # O path[1:] indica que apenas desejamos pegar o nome que está depois do /
                self.send_response(200) # Neste caso o 200 indica um Status de OK para o Serviço/servidor que esteja sendo criado
                                        # Caso funcione o Try Termina aqui, caso contrário entrará no Excepet
            except:
                open_file = "404 - Not Found"
                self.send_response(404) # Neste caso o 404 indica um Status de NOK/Error para o Serviço/servidor que esteja sendo criado
            self.end_headers() # Método necessário para finalizar o envio dos Headers. Header é um block que contem lename, author, date, and a few other details of the file and the contents of that file
            self.wfile.write(bytes(open_file, 'utf-8')) # Utilizado para enviar os Conteudos da página | Para escrever na tela precisamos converter em Bytes, E todos os arquivos estão codificados em utf-8

httpd = HTTPServer (('localhost', 8080), MainServer) # Criamos aqui a variavél que irá armazenar os dados do HTTPServer, passando o Servidor (no caso a máquina local - localhost)
                                                     # o Mainserver (nossa Classe), é utilizado para customizar as funções dentro do HTTPServer.
httpd.serve_forever()

