# Wifi - Exercice type

> Pascal Cotret, [ENSTA Bretagne](mailto:pascal.cotret@ensta-bretagne.fr) - FIPA24

Pour les questions suivantes, vous devrez utiliser le fichier `wpa2-psk-linksys.cap`. Utilisez les filtres suivants dans Wireshark : `wlan.fc.type`, `wlan.fc.subtype`.
**Ceci est un exercice type, non nôté. Malgré tout, faites l’effort de rédiger un document correct (peu importe le format : PDF, Markdown, Word, LibreOffice. . .), les réponses ne sont jamais très longues.**

(Google est votre ami)

## Question 1

Quel filtre permet d’afficher uniquement les trames de données ?

> ```data``` \
> ```wlan.fc.type_subtype == Data``` \
> ```wlan.fc.type_subtype == 32``` \
> ```wlan.fc.type==2 and wlan.fc.subtype==0``` \


## Question 2

Quel filtre permet d’afficher uniquement les trames relatives à l’authentification ?

> ```wlan.fc.subtype == 0xb``` \
> ```wlan.fc.type_subtype == Authentication```

## Question 3

Quel pourcentage du nombre total de paquets est consacré aux trames de type "contrôle" ?

> ```wlan.fc.type == 1``` \
> Il y a 163 trames, ce qui représente 32,7% de la trame total

## Question 4

Quel pourcentage de la quantité de données échangées est consacré aux trames de type "data" (type 2, sous-type 0) ?

> Menu: ```Statistics``` --> ```Capture files propreties``` --> ```bytes```  \
> Il y a 17935 paquets ce qui représente 48.9%

## Question 5

Quel pourcentage du nombre total de paquets est consacré aux trames de type "beacon frame" ?

> Menu: ```Statistics``` --> ```Capture files propreties``` --> ```bytes```  \
> Il y a 9265 paquets ce qui représente 25.2%


## Question 6

Quel pourcentage de la quantité de données échangées est consacré aux trames de type "beacon frame" ?

> Menu: ```Statistics``` --> ```Capture files propreties``` --> ```bytes```  \
> Il y a 1355 octets ce qui représente 3,7%



## Question 7

Quel pourcentage du nombre total de paquets est consacré aux trames de type "probe" ?

> ```wlan.fc.type_subtype == 4 or wlan.fc.type_subtype == 5```  \
> Il y a 24 trames soit 4,8%

## Question 8

Quel pourcentage de la quantité de données échangées est consacré aux trames de type "probe" ?

> Menu: ```Statistics``` --> ```Capture files propreties``` --> ```bytes```  \
> Il y a 1355 octets ce qui représente 3,7%

## Question 9

Remplissez le tableau suivant pour y ajouter des informations sur tous les réseaux actifs dans l’environnement où a été faite la capture (Ignorez les SSID nommés "Broadcast").

> On peur afficher la table des réseaux actif avec le menu: ```Wireless``` --> ```WLAN Trafic``` \
> (Cisco-Li_0f:03:32 apparait dans les trames mais pas sur la table)


|         SSID          |         MAC          |
| --------------------- | -------------------- |
|   IntelCor_55:98:ef   |  00:13:ce:55:98:ef   |
|   ArubaaHe_c2:a4:85   |  00:0b:86:c2:a4:85   |
|   Cisco-Li_e3:e4:01   |  00:0f:66:e3:e4:01   |
|   Cisco-Li_0f:03:32   |  00:14:bf:0f:03:32   | 





