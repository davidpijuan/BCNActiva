""" Sabries trobar el promitg dels beneficis anuals i del primer trimestre? """

ventes_mesos = [73259, 52943, 62971, 40526, 69017, 87322, 79034, 94213, 83617, 92345, 62352, 102341]
#promig anual
suma = ventes_mesos[0] + ventes_mesos[1] + ventes_mesos[2] + ventes_mesos[3] + ventes_mesos[4] + ventes_mesos[5] + ventes_mesos[6] + ventes_mesos[7] + ventes_mesos[8] + ventes_mesos[9] + ventes_mesos[10] + ventes_mesos[11] 
promig_anual = suma / len(ventes_mesos)
print(promig_anual)
#promig del primer trimestre
primer_trimestre = ventes_mesos[:3]
suma = primer_trimestre[0] + primer_trimestre[1] + primer_trimestre[2]
promig_trimestral = suma / len(ventes_mesos)
print(promig_trimestral)

