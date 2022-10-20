# Cours de réseaux - FIPA 24

Dans la mesure du possible, les supports de cours, exercices et documents annexes seront mis sous Moodle et, en priorité sur Gitlab, dans la journée après le cours.

## Installation de Wireshark sur les laptop ENSTA-B

```bash
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark
```

## Planning des séances restantes

```mermaid
gantt
    excludes weekends
    title Planning des séances restantes
    dateFormat  YYYY-MM-DD
    axisFormat  %d / %m
    section Cours + TD
    Cours + ateliers Wireshark           :milestone, 2022-10-14,0h
    TD (pas noté) sur simulateur routeur           :milestone, 2022-10-20, 0h
    Euronaval ? => Suppression à confirmer      :crit, active,milestone, 2022-10-21, 0h
    Fin TD + révisions           :milestone, 2022-10-26, 0h
    section Exam
    Exam (PC)           :crit,milestone, 2022-10-28, 0h
```
