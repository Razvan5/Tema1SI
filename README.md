## Utilizare

Se pornesc in aceasta ordine:
Se porneste UserKM
Se porneste UserA
Se porneste UserB

In userA se scrie de la tastatura ECB sau CFB

Din fisierul userA.txt se vor extrage informatiile si se vor afisa in terminalul lui B

## Functionalitati

Am folosit pycrtyptodome pt aes in mode_ecb

In UserA am trimis (dintr-un block try and except) tipul de encriptie
In UserB la fel
In UserKM memoram din cele doua threaduri pentru clienti ce alegeri au facut si apoi alegem la intamplare una din cele doua valori daca nu sunt egale

In UserKM continuma cu trimiterea unui flag lui UserA si UserB care semnifica tipul encriptie. De asemenea se trimite si key1/key2 cu init_vector criptate cu k3 dupa clientii au primit ok de la server si au trimis inapoi.

Cand serverul primeste un ok de la un client blocheaza threadul pt clientul respectiv pentru al astepta pe celalat.

Mereu citim 16 bytes!

Din UserA dupa ce am primit OK criptat folosid fie key1 sau key2 cu init_vector
incepem sa citim dintr-un fisier cate 16 bytes si apoi ii trimitem in UserKM care ii trimite mai departe lui UserB folosind vectorul de conexiuni care are in poz 0 pe A si in 1 pe B (De aici importanta initializarii clientilor)
Daca nu se citesc 16 bytes se paddeaza 

Algoritmul de padding padeaza fix cu numarul de spatii libere pentru a fi usor de eliminat

In UserB citim cate 16 bytes si ii decriptam in functie de branchul in care ne aflam 

La fel in modul CFB, unde singura diferenta este ca avem vectorul de initializare care isi actualizaza valoarea constant fiind criptat la fiecare pas din while-urile de citire/afisare