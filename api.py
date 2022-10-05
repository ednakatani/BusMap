import requests

class Api:
    def __init__(self, url, code):
        self.url = url
        self.code = code

    def get_linhas(self):
        url = self.url + '/getLinhas.php' + '?c=' + self.code
        response = requests.get(url)
        return response.json()

    def get_pontos_linha(self, linha):
        url = self.url + '/getPontosLinha.php' + '?c=' + self.code + '&linha=' + linha
        response = requests.get(url)
        return response.json()

    def get_veiculos_linha(self, linha):
        url = self.url + '/getVeiculos.php' + '?c=' + self.code + '&linha=' + linha
        response = requests.get(url)
        return response.json()
    
    def get_shape_linha(self, linha):
        url = self.url + '/getShapeLinha.php' + '?c=' + self.code + '&linha=' + linha
        response = requests.get(url)
        return response.json()
