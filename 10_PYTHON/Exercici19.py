""" Sabries resoldre les següents tasques?
- Ara segons el que ens han demanat, hem de fer un dialeg per poder retirar 1 peça de uniformitat
- En la resposta tenim que incloure una unitat que s'ha retirat, quans articles queden i quans havien originalment.
- També tenim que fer un dialeg per retornar la uniformitat
- Realitzarem un cercador per si existeix l'article que ens indiquin. """

stock = {'polos':23, 'bates':58, 'pantalons':17, 'sabates':34}
#Ara segons el que ens han demanat, hem de fer un dialeg per poder retirar 1 peça de uniformitat
#En la resposta tenim que incloure una unitat que s'ha retirat, quans articles queden i quans havien originalment.
print("Quina peça vols retirar?")
article_retirar = input()
num_articles = stock[article_retirar]
num_articles_restants = num_articles - 1
print("S'ha restat 1",article_retirar," i queden", num_articles_restants," de les ", num_articles," que hi havia")
#També tenim que fer un dialeg per retornar la uniformitat
print("Que vols retornar?")
article_retornar = input()
num_articles = stock[article_retornar]
num_articles_restants = num_articles + 1
print("S'ha afegit 1 ",article_retornar," i queden ",num_articles_restants," de les ",num_articles)
#Realitzarem un cercador per si existeix l'article que ens indiquin
claus = stock.keys()
print("Que vols cercar?")
article_buscar = input()
print(article_buscar in list(claus))
