![Yt_worhmhole](logo.png)

# 🪐 ytwormhole — Téléchargeur YouTube multithreadé

ytwormhole est un outil Python en ligne de commande (CLI) qui te permet de télécharger rapidement des vidéos ou des audios YouTube à partir d’un fichier .txt contenant plusieurs liens. Il est rapide, propre, configurable, et basé sur yt-dlp avec support du multithreading et d’une barre de progression (tqdm).

## 🚀 Fonctionnalités
    - 📁 Téléchargement en batch depuis un fichier .txt

    - 🎧 Mode audio-only (convertit en .mp3)

    - 🎞️ Téléchargement des vidéos en haute qualité

    - ⚡ Multithreading pour des téléchargements parallèles rapides

    - 📊 Barre de progression avec ETA grâce à tqdm

    - 🔧 Configuration du dossier de sortie et du nombre de threads

## 🛠️ Installation

### 1. Clone du dépôt
```bash

git clone https://github.com/ton-utilisateur/ytwormhole.git
cd ytwormhole
```
### 2. Installation des dépendances
```bash

pip install -r requirements.txt
```
## 📄 Exemple de fichier urls.txt

https://www.youtube.com/watch?v=id

## 🚀 Utilisation
```bash

python main.py input [--format FORMAT] [--output_path PATH] [--nb_threads N]

```

### 📋 Arguments
Argument	Description	Exemple
input	URL unique ou fichier .txt avec URLs	down.txt ou https://www.youtube.com/watch?v=XYZ
--format	Format de téléchargement : mp3 (audio) ou mp4 (vidéo)	--format mp3
--output_path	Dossier de sortie des fichiers téléchargés	--output_path downloads
--nb_threads	Nombre de threads parallèles (default 4)	--nb_threads 4

## 🎯 Exemples
Télécharger une vidéo en MP3 (par défaut) :

```bash
python main.py https://www.youtube.com/watch?v=YKDuTlSxb5Q
```

Télécharger plusieurs vidéos listées dans un fichier texte en MP4 avec 6 threads :

```bash
python main.py down.txt --format mp4 --nb_threads 6
```
Télécharger en MP3 et sauvegarder dans un dossier personnalisé :

```bash
python main.py down.txt --output_path my_downloads --nb_threads 3
```
## 💡 Notes importantes

Le fichier texte doit contenir une URL YouTube par ligne.

Les noms des fichiers sont générés automatiquement à partir du titre vidéo et de l’ID pour éviter les conflits.

Assurez-vous que ffmpeg est installé et accessible en ligne de commande pour la conversion audio.

Pour éviter les conflits de fichiers, évitez d’utiliser des dossiers synchronisés comme OneDrive.

## 📦 requirements.txt
```shell
yt-dlp>=2024.4.9
tqdm>=4.66.0
```

## 📚 Licence
Ce projet est sous licence MIT. Tu peux l’utiliser, le modifier, ou le distribuer librement.

## 🙋 Aide & Contributions
Tu veux ajouter une interface graphique ?

Ajouter un système de logs ou un fichier .csv de reporting ?

Ajouter le support de playlists complètes ?

### ➡️ Ouvre une issue ou propose une pull request sur GitHub

## ✨ Nom de code : ytwormhole
"Plonge dans le vortex et récupère le contenu à la vitesse de la lumière."

