# Product Recognition from Images and Metadata

This repository contains a complete and production-ready pipeline to recognize products from images and structured data using PyTorch and XGBoost.

## Project Overview

The goal is to automate product classification by combining:
- **Image classification** using a Convolutional Neural Network (CNN) built with PyTorch
- **Metadata classification** using XGBoost on tabular features
- **Dashboard** for model performance visualization with Dash

## Features

- Fully modular project (separated code, models, data)
- Configuration file (`config.yaml`) for training parameters
- Model training scripts and test suite included
- Interactive dashboard for result visualization

---

## 1. Installation

```bash
git clone https://github.com/your-username/ProductRecognizer.git
cd ProductRecognizer
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -e .
```

---

## 2. ⚠️ Required Data (Not Included)

**This repository does not contain image or tabular data. You must download and place them locally.**

### a. Image Data
- Download the Fruits-360 dataset: https://www.kaggle.com/datasets/moltean/fruits
- Extract and place the folders like this:

```
product_recognizer/data/images/Training/
product_recognizer/data/images/Test/
```

### b. Metadata (Tabular CSV)
- Provide a CSV file named `product_metadata.csv` with:
  - One column named `label`
  - Other numeric or categorical features
- Place it in:

```
product_recognizer/data/product_metadata.csv
```

---

## 3. Train the Models

```bash
python train.py
```

This will:
- Train the CNN on image data
- Train the XGBoost model on metadata
- Save both models in `product_recognizer/models/`

---

## 4. Launch the Dashboard

```bash
python dashboard/app.py
```

Open your browser at: [http://localhost:8050](http://localhost:8050)

---

## 5. Run Tests

```bash
pytest tests/
```

---

## About

This project was built as a full-stack example of applied machine learning with vision and tabular data. All components are designed to be reusable, extensible, and readable.