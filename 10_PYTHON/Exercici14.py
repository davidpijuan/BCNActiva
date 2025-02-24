""" Sabries resoldre les següents tasques?
- Llistat complert de l'alumnat
- El.laborar dos llistats que correspondran a dos aules A y B.
- Els 5 primers alumnes tenen que anar a la aula A y la resta a la B.
- Per ultim mostrar ambes llistes. """

llista_alumnes = ['Anna', 'Joan', 'Oriol', 'Silvia', 'Ricard', 'Iria', 'Francesc']
alumnes_ultima_hora = ['Josep', 'Lidia', 'Alba']
#Llistat complert de l'alumnat
llista_alumnes.extend(alumnes_ultima_hora)
print(llista_alumnes)
#Elaborar dos llistats que correspondran a dos aules A i B.
aula_a = []
aula_b = []
#Els 5 primers alumnes han d'anar a la aula A i la resta a la B.
aula_a = llista_alumnes[:5]
aula_b = llista_alumnes[5:]
#Per ultim mostrar ambes llistes.
print(aula_a)
print(aula_b)