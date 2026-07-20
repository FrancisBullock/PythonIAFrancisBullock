import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Charger les données
try:
    df_ventes = pd.read_csv('ventes.csv')
except FileNotFoundError:
    print("Erreur : Le fichier 'ventes.csv' est introuvable.")
    exit()

print("--- ÉTUDE COMPLÈTE DU JEU DE DONNÉES (VENTES.CSV) ---")

# 2. Analyse exploratoire
print(f"\nDimensions du jeu de données : {df_ventes.shape} (lignes, colonnes)")
print("\nRecherche des valeurs manquantes :")
print(df_ventes.isnull().sum())
print("\nStatistiques descriptives :")
print(df_ventes.describe())

# 3. Matrice de corrélation (variables numériques uniquement)
# On exclut la colonne 'date' si elle est présente sous forme de texte
df_numerique = df_ventes.select_dtypes(include=['float64', 'int64'])
matrice_corr = df_numerique.corr()
print("\nMatrice de corrélation :")
print(matrice_corr)

# 4. Affichage graphique de la matrice de corrélation
plt.figure(figsize=(6, 5))
plt.imshow(matrice_corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
# Configuration des axes avec le nom des variables
tick_marks = range(len(matrice_corr.columns))
plt.xticks(tick_marks, matrice_corr.columns, rotation=45)
plt.yticks(tick_marks, matrice_corr.columns)
plt.title("Graphique de la matrice de corrélation")
plt.tight_layout()
plt.show()

# 5. Modèle de régression linéaire multiple
X_mult = df_ventes[['temperature', 'budget_publicitaire']]
y_mult = df_ventes['ventes']

model_mult = LinearRegression()
model_mult.fit(X_mult, y_mult)

# 6. Évaluation du modèle
y_mult_pred = model_mult.predict(X_mult)
r2_mult = r2_score(y_mult, y_mult_pred)

# 7. Affichage des coefficients
print("\n--- RÉSULTATS DU MODÈLE MULTIPLE ---")
print(f"Score R² : {r2_mult:.4f}")
print(f"Coefficient pour la Température : {model_mult.coef_[0]:.2f}")
print(f"Coefficient pour le Budget Publicitaire : {model_mult.coef_[1]:.2f}")
print(f"Constante (Intercept) : {model_mult.intercept_:.2f}")

# 8. Résumé et interprétation des résultats
print("\n--- RÉSUMÉ ET INTERPRÉTATION DES RÉSULTATS ---")
print(f"Le modèle de régression linéaire possède un coefficient de détermination R² de {r2_mult:.2f}.")
print(f"Cela signifie que environ {r2_mult*100:.1f}% de la variation des ventes est expliquée par la température et le budget publicitaire.")
print("\nInterprétation des variables :")
print(f"- Chaque augmentation d'un degré de température génère une variation de {model_mult.coef_[0]:.2f} unités de ventes.")
print(f"- Chaque unité supplémentaire investie dans le budget publicitaire génère {model_mult.coef_[1]:.2f} unités de ventes.")
print("La variable ayant le coefficient le plus élevé ou la corrélation la plus forte dans la matrice a l'impact le plus significatif sur la performance commerciale.")