# Wifi - Exercice 2 - L'exercice se base sur la capture Wireshark trace-80211.pcap

> Pascal Cotret, [ENSTA Bretagne](mailto:pascal.cotret@ensta-bretagne.fr) - FIPA24

## Inspection d'une trace

### Question 1

Paquet #16. Record **Frame**

- A quelle date est arrivée le paquet ?

- Que peut-on dire de cet ensemble d'informations par rapport au protocole WiFi ?

### Question 2

Paquet #16. Record **IEEE 802.11**, champ **Frame Control**.

- Vérifier que le type et le sous-type sont conformes aux spécifications.

### Question 3

Paquet #16. Record **IEEE 802.11**.

- S'agit-il d'un dernier fragment ?

- Est-ce que celui-ci est protégé ?

## Couche physique du 802.11

### Question 4

Paquet #16. Quelle est la fréquence du signal ?

### Question 5

Ajouter une colonne dans Wireshark pour visualiser le RSSI (*Received Signal Strength Indication*). Quelles sont les différentes valeurs de RSSI que l'on peut observer ?

## Couche liaison

Menu `Statistics` => `Conversations` => `Conversation Types` et sélectionner 802.11.

### Question 6

Combien de paquets ont été transmis entre `00:16:b6:e3:e9:8d` et `70:56:81:a2:05:1d` ? Combien d'octets ?

### Question 7

Dans la capture, combien y a-t-il de paquet de type `Data` ?

# 
