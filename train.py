import os
import yaml
import joblib
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Chargement de la config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Paramètres
batch_size = config["training"]["batch_size"]
epochs = config["training"]["epochs"]
lr = config["training"]["learning_rate"]
image_size = tuple(config["training"]["image_size"])

# === CNN TRAINING ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize(image_size),
    transforms.ToTensor(),
])

train_dir = config["paths"]["train_images"]
test_dir = config["paths"]["test_images"]

train_data = datasets.ImageFolder(train_dir, transform=transform)
test_data = datasets.ImageFolder(test_dir, transform=transform)

train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_data, batch_size=batch_size)

class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Linear(32 * 23 * 23, 256),
            nn.ReLU(),
            nn.Linear(256, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)

model = SimpleCNN(num_classes=len(train_data.classes)).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

for epoch in range(epochs):
    model.train()
    epoch_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    print(f"Epoch {epoch+1}/{epochs} - Loss: {epoch_loss:.4f}")

torch.save(model.state_dict(), config["paths"]["cnn_model_path"])
print("✅ Modèle CNN sauvegardé.")

# === XGBOOST TRAINING ===
df = pd.read_csv(config["paths"]["tabular_data"])
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
xgb_model = xgb.XGBClassifier(n_estimators=100, max_depth=5, use_label_encoder=False, eval_metric='mlogloss')
xgb_model.fit(X_train, y_train)

preds = xgb_model.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"✅ Précision XGBoost : {acc:.2%}")

joblib.dump(xgb_model, config["paths"]["xgb_model_path"])
print("✅ Modèle XGBoost sauvegardé.")