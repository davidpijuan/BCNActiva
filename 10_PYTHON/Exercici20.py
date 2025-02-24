""" Ara que ja sabeu realitzar condicionals, segur que podreu solventar un bug que hi ha en el projecte.
Problema:
Quan algú indica un article que no existeix en el diccionari, falla tot el script.
Podeu desenvolupar la solució? """

stock = {'polos':23, 'bates':58, 'pantalons':17, 'sabates':34}
#Ara segons el que ens han demanat, hem de fer un dialeg per poder retirar 1 peça de uniformitat
#En la resposta tenim que incloure una unitat que s'ha retirat, quans articles queden i quans havien originalment.
print('Que vols retirar?')
article_retirar = input()
#comprovem que existeixi el article 
claus = stock.keys()
if article_retirar in list(claus):
    num_articles = stock[article_retirar]
    num_articles_restants = num_articles - 1
    print("S'ha restat 1",article_retirar,"i queden",num_articles_restants,'de les',num_articles,'que hi havia.')
else:
    print("L'article no existeix")
#També tenim que fer un dialeg per retornar la uniformitat
print('Que vols retornar?')
article_retornar = input()
#comprovem que existeixi el article
claus = stock.keys()
if article_retornar in list(claus):
    num_articles = stock[article_retornar]
    num_articles_restants = num_articles + 1
    print("S'ha afegit 1",article_retornar,"i queden",num_articles_restants,'de les',num_articles,'que hi havia.')
else:
    print("L'article a retornar no existeix")
#Realitzarem un cercador per si exiteix el article que ens indiquin
claus = stock.keys()
print('Que vols cercar?')
article_buscar = input()
#comprovem que existeixi el article
if article_buscar in list(claus):
    print(article_buscar in list(claus))
else:
    print("L'article no existeix")
