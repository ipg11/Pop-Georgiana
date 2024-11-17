# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []


# Afisare sablon initial
print('bine ai venit la jocul spanzuratoarea!')
print('cuvantul de ghicit:'+''.join(progres))
print(f'incercari ramase: {incercari_ramase}\n')

# Bucla principala de joc
while '_' in progres and incercari_ramase > 0:
    # a. crearea unei litere
    litera = input('Introdu o litera:').lower()

    # b. verificare validitate
    if len(litera) != 1 or not litera.isalpha():
        print('Te rog saintroduci osingura litera valida.')
        continue

    if litera in litere_incercate:
        print('Ai incercat deja aceasta litera. Incearca alta.')
        continue

    litere_incercate.append(litera)

    # c. Verificarea literei in cuvant
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print('cuvant de ghicit:'+''.join(progres))
        print(f'Corect! Litera "{litera}" se gaseste in cuvant.')
    else:
        incercari_ramase -= 1
        print(f'Incorect! Litera "{litera}" nu se gaseste in cuvant {incercari_ramase}')


# Afisarea progresului si incercarilor ramase
print('Progresul cuvantului este:'+ ''.join(progres))
print('Incercari ramase:', incercari_ramase)

# Încheierea jocului
if '_' not in progres:
  print('Felicitari! Ai ghicit cuvantul:'+ cuvant_de_ghicit)
else:
  print('Ai pierdut! Cuvantul era:'+ cuvant_de_ghicit)

