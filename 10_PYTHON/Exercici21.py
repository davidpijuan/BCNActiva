""" Hi ha treballadors que tenen varies unitats d’un mateix article i no tinc cap registre d’aixo.
Podries realitzar un registre de qui agafa o retorna roba?
També comprovar que només agafin un de cada siusplau.
Per ultim que no permeti retirar si no poseeix cap unitat del article """

stock = {'polos':23, 'bates':58, 'pantalons':17, 'sabates':34}
#Hem de crear un diccionari de treballadors i uniformitats
treballadors = {"Albert":["pantalons"],"Anna":[],"Ricard":[]}
#Ara segons el que ens han demanat, hem de fer un dialeg per poder retirar 1 peça de uniformitat
#En la resposta tenim que incloure una unitat que s'ha retirat, quans articles queden i quans havien originalment.
#Hem de preguntar qui es el treballador i obtenir-ho amb un input
print("Qui ets?")
treballador = input()
print('Que vols retirar?')
article_retirar = input()

#comprovem que existeixi el treballador
claus_treballadors = treballadors.keys()
if treballador in list(claus_treballadors):
    #comprovem que existeixi el article 
    claus = stock.keys()
    if article_retirar in list(claus):
        #filtrem que només pugui retirar si te unitats del article
        idarticle = treballadors[treballador].index(article_retirar)
        roba_treballador = treballadors[treballador]
        if article_retirar in roba_treballador:
            del treballadors[treballador][idarticle]
            num_articles = stock[article_retirar]
            num_articles_restants = num_articles - 1
            print("S'ha restat 1",article_retirar,"i queden",num_articles_restants,'de les',num_articles,'que hi havia.')
            #Mostrem el estat actual dels treballadors i la seva uniformitat
            print(treballadors)
        else:
            print("No hi han unitats d'aquest article")
    else:
        print('El article no existeix')
else:
    print("No existeix el treballador")

#També tenim que fer un dialeg per retornar la uniformitat
print('Que vols retornar?')
article_retornar = input()
#comprovem que existeixi el article
claus = stock.keys()
if article_retornar in list(claus):
    #Afegim el article al registre de treballadors i articles de cada un
    treballadors[treballador].append(article_retornar)
    num_articles = stock[article_retornar]
    num_articles_restants = num_articles + 1
    print("S'ha afegit 1",article_retornar,"i queden",num_articles_restants,'de les',num_articles,'que hi havia.')
    #Mostrem el estat actual dels treballadors i la seva uniformitat
    print(treballadors)
else:
    print('El article no existeix')

#Realitzarem un cercador per si exiteix el article que ens indiquin
claus_buscar = stock.keys()
print('Que vols cercar?')
article_buscar = input()
#comprovem que existeixi el article
if article_buscar in list(claus_buscar):
    print(article_buscar in list(claus_buscar))
else:
    print('El article no existeix')

#mostrem llistat de treballadors i articles asignats
print(treballadors)