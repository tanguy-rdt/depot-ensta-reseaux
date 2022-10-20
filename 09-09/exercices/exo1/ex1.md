## Problème

Un échange authentifié de fichier réalisé grâce au protocole FTP. Retrouvez le mot de passe utilisé par l’utilisateur.

> - L'utilsateur est ***cdts3500***
> - Le mot de passe est ***cdts3500*** 
>  
>![](./img/1.png)
>
>Il est facile d'obtenir c'est information en utilisant le filtre ```ftp```.


## Question bonus

En fait, qu'est-ce qu'a fait l'utilisateur pendant cette capture ?

> Il a réalisé un transfert de fichier à l'aide du protocole ftp *(File Transfert Protocol)* 
>
> On peut obtenir d'avantage d'information avec *clic droit &rarr; follow &rarr; TCP Stream* :
>```
>220-QTCP at fran.csg.stercomm.com.
>220 Connection will close if idle more than 5 minutes.
>USER cdts3500
>331 Enter password.
>PASS cdts3500
>230 CDTS3500 logged on.
>SYST
>215  OS/400 is the remote operating system. The TCP/IP version is "V5R2M0".
>SITE NAMEFMT
>250  Now using naming format "0".
>PWD
>257 "CDTS3500" is current library.
>PASV
>227 Entering Passive Mode (10,20,144,151,62,141).
>RETR qgpl/apkeyf.apkeyf
>150 Retrieving member APKEYF in file APKEYF in library QGPL.
>250 File transfer completed successfully.
>QUIT
>221 QUIT subcommand received.
>```

## Références bibliographiques

- La RFC du FTP : https://datatracker.ietf.org/doc/html/rfc959
