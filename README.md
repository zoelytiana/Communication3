# README #

# Projet BQTSI

## description

## installation

Cloner le dêpot : 

```sh
$ git clone https://github.com/Epsi-POEC-11-BQTSI/Projet-BQTSI.git
$ cd PROJET-BQTSI
```

Créer un l'environnement virtuel et l'activer :

```sh
$ python -m venv venv
$ source venv/Scripts/activate
```

Installer les librairies :

```sh
(venv)$ pip install -r requirements.txt
```
le `(venv)` devant le prompt indique que ce terminal utilise l'environnement virtuel.

Copier vos fichiers de base de données db.sqlbpro et db.sqlite3 dans le dossier src.
Puis lancer le projet :
```sh
(venv)$ cd src
(venv)$ python manage.py runserver
```