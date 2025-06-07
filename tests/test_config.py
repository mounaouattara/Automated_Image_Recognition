import os
import yaml

def test_config_paths():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    assert os.path.exists(config["paths"]["train_images"]), "Dossier d'entraînement non trouvé"
    assert os.path.exists(config["paths"]["tabular_data"]), "Fichier tabulaire introuvable"