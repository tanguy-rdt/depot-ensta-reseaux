# PCAP 1: Ping

1. Adresse IP de l'hôte qui est pingé ?

   > `192.168.2.1`

   

2. Les trois couches dans le paquet #1?

   > ICMP &rarr; IPv4 &rarr; Ethernet 
   >
   > +haut niveau ----- +bas niveau

   

3. Est-ce que le protocole de plus haut-niveau utilise des ports ?

   > Non, UDP et TCP utilise des ports

   

4. Pour le paquet #1, faites un schéma avec la longueur de chaque portion (la longueur totale doit être de 98 octets).

   

# PCAP 2: SMTP

1. Sur quel port tourne le serveur SMTP ?
2. Le client utilise quel port ?
3. Sur quel protocole tourne SMTP ?
4. 1. Quel paquet représente la requête ? 
   2. Quel flag représente le début de la connexion ? 
   3. Quel paquet contient la réponse du serveur SMTP ? 

# PCAP 3 : Traceroute

`traceroute.pcap` capture une trace depuis une VM vers un serveur. Les paquets 1 à 4 sont issus d'une autre commande.

1. Quelle est l'adresse IP de l'hôte qui demande le traceroute ?

   > Il suffit de regarder l'adresse source du paquet #5 : 192.168.0.102
   >
   > ![](/Users/tanguy/Documents/ENSTA_depot/depot-ensta-reseaux/26-10/images/2022-10-27-13-53-08-image.png)

   

2. Comment l'hôte détermine l'adresse IP de la cible ?

   > Dans le screenshot ci-dessus, on voit que le paquet #5 demande une adresse IPv4, le paquet #6 une adresse IPv6. Ca se fait avec le protocole DNS.

   

3. Après avoir récupérer l'adresse IP, on commence à envoyer des données. Quel est le protocol de transport pour ces paquets ?

   > UDP (screenshot pas indispensable dans un compte-rendu réel)
   >
   > ![](/Users/tanguy/Documents/ENSTA_depot/depot-ensta-reseaux/26-10/images/2022-10-27-13-54-50-image.png)

   

4. Combien de paquets avant la première réponse ?

   > 13 paquets de données (encadré en bleu)
   >
   > ![](/Users/tanguy/Documents/ENSTA_depot/depot-ensta-reseaux/26-10/images/2022-10-27-13-57-52-image.png)

   

5. Quel est le TTL du dernier paquet avant de recevoir la première réponse ?

   > 5, d'ailleurs, c'est le seul paquet de données qui n'est pas en rouge. Si on regarde les autres, ils ont un TTL de 1 : dernière valeur avant extinction, d'où la couleur !![](/Users/tanguy/Documents/ENSTA_depot/depot-ensta-reseaux/26-10/images/2022-10-27-13-59-11-image.png)

