# Automated Product Recognition

This project implements a complete system to classify products based on images and structured metadata, combining Deep Learning (PyTorch) and Machine Learning (XGBoost). It is structured for clarity, modularity, and reusability.

## Project Structure

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

1. Clone the repository:
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

This project does not include the actual data to reduce repository size. You must add them manually:

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

Once the data is in place, train the models with:
```bash
python train.py
```

This script:
- Trains a CNN on images using PyTorch
- Trains a classifier using XGBoost on tabular data
- Saves both models under `product_recognizer/models/`

## Dashboard

To visualize performance:
```bash
python dashboard/app.py
```
Then open your browser at `http://localhost:8050`

## Testing

Run basic structural tests:
```bash
pytest tests/
```

## Author

This project was built as a complete demonstration of applied data science with vision and tabular data integration, using real datasets and common tools.