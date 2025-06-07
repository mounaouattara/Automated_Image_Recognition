# Automated Product Recognition

This project implements a complete system to classify products based on images and structured metadata, combining Deep Learning (PyTorch) and Machine Learning (XGBoost). It is structured for clarity, modularity, and reusability.

<<<<<<< HEAD
## Project Structure
=======
---

## Structure du projet
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5

```
ProductRecognizer/
├── product_recognizer/            # Source code
│   ├── data/                      # Image and tabular data
│   ├── models/                    # Saved models
│   ├── pipeline/                  # Model and training modules
│   └── visualizations/           # Figures and dashboards
├── notebooks/                    # Exploratory notebooks (optional)
├── dashboard/                    # Dash app for performance visualization
├── tests/                        # Unit tests
├── config.yaml                   # Training and path configuration
├── train.py                      # Training pipeline
├── setup.py                      # Installation file
└── README.md                     # This file
```

## Installation

<<<<<<< HEAD
1. Clone the repository:
=======
## Installation

### 1. Cloner le dépôt
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5
```bash
git clone https://github.com/your-username/ProductRecognizer.git
cd ProductRecognizer
```

2. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Required Data (Important)

<<<<<<< HEAD
This project does not include the actual data to reduce repository size. You must add them manually:
=======
## Préparer les données

Les données doivent être ajoutées localement.
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5

### 1. Image Data
- Download the dataset from [Fruits 360 - Kaggle](https://www.kaggle.com/datasets/moltean/fruits)
- Extract and place the folders as follows:
```
product_recognizer/data/images/Training/
product_recognizer/data/images/Test/
```

### 2. Tabular Metadata
- You need a CSV file with a column `label` and any other numeric or categorical features.
- Place the file here:
```
product_recognizer/data/product_metadata.csv
```

## Running the Project

<<<<<<< HEAD
Once the data is in place, train the models with:
=======
## Lancer l’entraînement

Tout est configurable dans `config.yaml`.

### Exécuter le pipeline :
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5
```bash
python train.py
```

This script:
- Trains a CNN on images using PyTorch
- Trains a classifier using XGBoost on tabular data
- Saves both models under `product_recognizer/models/`

<<<<<<< HEAD
## Dashboard
=======
---

## Visualiser les résultats

Un tableau de bord Dash est disponible :
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5

To visualize performance:
```bash
python dashboard/app.py
```
Then open your browser at `http://localhost:8050`

## Testing

<<<<<<< HEAD
Run basic structural tests:
=======
---

## Tests unitaires

Vérifie que la structure est correcte :
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5
```bash
pytest tests/
```

## Author

<<<<<<< HEAD
This project was built as a complete demonstration of applied data science with vision and tabular data integration, using real datasets and common tools.
=======
## À propos du projet

Ce projet est conçu pour illustrer une chaîne de traitement complète en Data Science appliquée à la vision par ordinateur et aux données structurées. Il peut servir de base pour des cas plus complexes, du transfer learning, ou des systèmes multi-modaux.

---
>>>>>>> f403f77231bdc26e546deef493ada918652c1fc5
