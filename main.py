from api import Api
import matplotlib.pyplot as plt

code = open('.key').read().strip()

api = Api('https://transporteservico.urbs.curitiba.pr.gov.br',code)

pontosLinha = api.get_pontos_linha('011')


#for ponto in pontosLinha:
    #print(ponto['NOME'])

veiculos = api.get_veiculos_linha('011')

for veiculo in veiculos:
    v = veiculos[veiculo]
    print(v['LAT'])
    print(v['LON'])


shape = api.get_shape_linha('011')
x = [s['LON'] for s in shape]
y = [s['LAT'] for s in shape]

plt.scatter(x, y)
plt.show()


    