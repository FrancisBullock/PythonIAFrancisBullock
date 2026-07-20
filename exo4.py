import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Charger les données
df_clients = pd.read_csv('clients.csv')

# 2. Construction des variables X (explicative) et y (cible)
# Scikit-Learn attend un tableau 2D pour X, d'où le double crochet [['age']]
X = df_clients[['age']]
y = df_clients['montant_achat']

# 3. Division en 80% train / 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entraînement de la régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Prédictions sur le jeu de test pour l'évaluation
y_pred = model.predict(X_test)

# 5. Évaluation du modèle
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("--- RÉSULTATS DE LA RÉGRESSION LINÉAIRE (ÂGE -> MONTANT) ---")
print(f"Coefficient de détermination (R²) : {r2:.4f}")
print(f"Erreur quadratique moyenne (MSE) : {mse:.2f}")
print(f"Équation de la droite : Montant = {model.coef_[0]:.2f} * Âge + {model.intercept_:.2f}")

# 6. Graphique : Données réelles vs Droite de régression
plt.figure(figsize=(8, 5))
# Affichage de tous les points réels
plt.scatter(X, y, color='blue', alpha=0.5, label='Données réelles')
# Tracé de la droite de régression sur l'ensemble du domaine d'âge
X_droite = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_droite = model.predict(X_droite)
plt.plot(X_droite, y_droite, color='red', linewidth=2, label='Droite de régression')

plt.title("Régression linéaire : Montant d'achat en fonction de l'âge")
plt.xlabel("Âge")
plt.ylabel("Montant d'achat (€)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()