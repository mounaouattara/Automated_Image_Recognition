# Reconnaissance Automatisée de Produits

Ce projet propose un système complet de reconnaissance de produits à partir d'images et de métadonnées, en combinant Deep Learning (PyTorch) et Machine Learning (XGBoost). Il est conçu pour être facilement configurable, modulaire et professionnel.

---

## Structure du projet

```
ProductRecognizer/
├── product_recognizer/            # Code source du projet
│   ├── data/                      # Images et données tabulaires
│   ├── models/                    # Modèles entraînés
│   ├── pipeline/                  # Modules d'entraînement/modélisation
│   └── visualizations/           # Graphiques, dashboards
├── notebooks/                    # Notebooks exploratoires (optionnels)
├── dashboard/                    # Application Dash pour visualiser les performances
├── tests/                        # Tests unitaires
├── config.yaml                   # Fichier de configuration du pipeline
├── train.py                      # Pipeline complet d'entraînement
├── setup.py                      # Installation en tant que package
└── README.md                     # Ce fichier
```

---

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/ton-utilisateur/ProductRecognizer.git
cd ProductRecognizer
```

### 2. Créer un environnement virtuel
```bash
python -m venv env
source env/bin/activate       # Windows : env\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -e .
```

---

## Préparer les données

### 1. Télécharge les données d’images
- Va sur [Fruits 360 - Kaggle](https://www.kaggle.com/datasets/moltean/fruits) et télécharge le dataset.
- Place les images dans :
```
product_recognizer/data/images/Training/
product_recognizer/data/images/Test/
```

### 2. Prépare les données tabulaires
- Télécharge ou crée un fichier CSV contenant des colonnes de caractéristiques et une colonne `label`.
- Place-le ici :
```
product_recognizer/data/product_metadata.csv
```

---

## Lancer l’entraînement

Tout est configurable dans `config.yaml`.

### Exécuter le pipeline :
```bash
python train.py
```

Cela :
- Entraîne le CNN sur les images
- Entraîne XGBoost sur les métadonnées
- Sauvegarde les modèles dans `product_recognizer/models/`

---

## Visualiser les résultats

Un tableau de bord Dash est disponible :

```bash
python dashboard/app.py
```

Puis ouvre [http://localhost:8050](http://localhost:8050) dans ton navigateur.

---

## Tests unitaires

Vérifie que la structure est correcte :
```bash
pytest tests/
```

---

## À propos du projet

Ce projet est conçu pour illustrer une chaîne de traitement complète en Data Science appliquée à la vision par ordinateur et aux données structurées. Il peut servir de base pour des cas plus complexes, du transfer learning, ou des systèmes multi-modaux.

---
