meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []


cati_papanasi_erau_la_inceput = meniu.count('papanasi')
cati_papanasi_s_au_comandat = comenzi.count('papanasi')
pret_papanasi = preturi[0][1]
castig_papanasi = cati_papanasi_s_au_comandat*pret_papanasi

print(cati_papanasi_erau_la_inceput-cati_papanasi_s_au_comandat)
print(cati_papanasi_s_au_comandat*pret_papanasi)

cata_ceafa_era_la_inceput = meniu.count('ceafa')
cata_ceafa_s_a_comandat = comenzi.count('ceafa')
pret_ceafa = preturi[1][1]
castig_ceafa = cata_ceafa_s_a_comandat*pret_ceafa

print(cata_ceafa_era_la_inceput-cata_ceafa_s_a_comandat)
print(cata_ceafa_s_a_comandat*pret_ceafa)

cat_guias_era_la_inceput = meniu.count('guias')
cat_guias_s_a_comandat = comenzi.count('guias')
pret_guias = preturi[2][1]
castig_guias = cat_guias_s_a_comandat*pret_guias

print(cat_guias_era_la_inceput-cat_guias_s_a_comandat)
print(cat_guias_s_a_comandat*pret_guias)

while studenti :
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f'studentul {student} a comandat {comanda}')
    istoric_comenzi.append([student, comanda])
    tavi.pop()


# 2. Inventar
# Numar portii conandate
portii_comandate = {produs: 0 for produs in ['papanasi', 'ceafa', 'guias']}
for comanda in istoric_comenzi:
    for produs in portii_comandate.keys():
        if produs in comanda:
            portii_comandate[produs] +=1

# Afisare tavi nramase
print(f'mai sunt {len(tavi)} tavi.')

#Verificare portii disponibile
mai_sunt_portii_disponibile = {
    'papanasi' : meniu.count('papanasi'),
    'ceafa' : meniu.count('ceafa'),
    'guias' : meniu.count('guias'),
}
for produs in ['ceafa', 'papanasi', 'guias']:
    if mai_sunt_portii_disponibile[produs] > 0:
        print(f'exista portii de{produs} disponibile.')
    else:
        print(f'nu exista portii de{produs} disponibile.')


# 3. Finante
#total venit cantina
total_venit = 0
for comanda in istoric_comenzi:
    for produs, pret in preturi:
        if produs in comanda:
            total_venit += pret

print(f'Cantina a incasat in total: {total_venit} lei.')

# Produse care costa cel mult 7 lei
produse_ieftine = [i for i in preturi if i[1]<=7]
print(f'Produse care costa cel mult 7 lei: {produse_ieftine}')

