from setuptools import setup, find_packages

setup(
    name='product_recognizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'pandas',
        'numpy',
        'xgboost',
        'dash',
        'plotly',
        'scikit-learn',
        'opencv-python',
        'joblib'
    ],
    author='TonNom',
    description='Reconnaissance de produits via images et métadonnées.',
)