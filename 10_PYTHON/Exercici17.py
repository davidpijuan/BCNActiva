""" Sabries resoldre les següents tasques?
- Tenim una data en format america i s'ha de transformar en format europeu. """

data = '2019-12-21'
#Tenim aquesta data en format america, pero desitgem mostrar-ho en format europeu
data_nova = data.split("-")
print(data_nova[2],"-",data_nova[1],"-",data_nova[0])