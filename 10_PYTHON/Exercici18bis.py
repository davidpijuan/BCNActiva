""" Sabries resoldre les següents tasques?
- Hem de obtenir el total de la compra
- També podem obtenir el promig de la compra, de forma automatitzada i independentment de que incloguem nous articles o en retirem
- Incloem un nou article, mostrem el total i el promig de nou.
- Tenint en compte que paguem amb un bitllet de 50 euros... quin canvi ens donaran?. """

carro = {'pebrots':7.50,'formatge':10.22,'suc de poma':0.80,'sucre':1.04}
#Hem de obtenir el total de la compra
valors = carro.values()
print(sum(list(valors)))
#També podem obtenir el promig de la compra, de forma automatitzada i independentment de que incloguem nous articles o en retirem
total = sum(list(valors))
mitjana = (total/len(list(valors)))
print(mitjana)
#Incloem un nou article, mostrem el total i el promig de nou.
print('Quin nou producte vols?')
nou_producte = input()
print('Quan val?')
nou_pvp = input()
carro[nou_producte] = float(nou_pvp)
valors = carro.values()
total = sum(list(valors))
mitjana = (total/len(list(valors)))
print(total)
print(mitjana)
#Tenint en compte que paguem amb un bitllet de 50 euros... quin canvi ens donaran?
canvi = 50 - total
print(canvi)