print("Hello world!" + " Jak se máš?") #Pokud chci více datových typů v printu - musím si je oddělit čárkou
#vytvoření proměnné deklarace/inicializace
cislo = 1 #do proměnné číslo je uložená hodnota 1: datový typ int
print("Druhý způdob s proměnnou", cislo)
#Vytvoření proměnné s názvem text
text = "Zde je v proměnné uložený text" #Datocý typ string
#Do konzole vypisujeme obě proměnné, oddělujeme čárkou
print(text, cislo)
#proměnná text vypíše, co je v ní ullžené
#proměnná cislo vypíše číslo, kteé je v ní uložené
#vytvoření vstupní hodnoty - uživatel musí zadat hodnotu do terminálu
#následně se hodnota zadaná do terminálu uloží do proměnné
vstupni_promenna = input() #input - příkaz pro vstupní data
druha_vstupni_promenna = inpt("Zadejte číslo: ")
#print nám vypíše, co uživatel zadal do inputu
print(vstupni_promenna, druha_vstupni_promenna)