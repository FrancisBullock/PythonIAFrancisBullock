import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df_clients = pd.read_csv('clients.csv')

# 1. Histogramme de la distribution des âges
plt.figure(figsize=(8, 5))
plt.hist(df_clients['age'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution de l'âge des clients")
plt.xlabel("Âge")
plt.ylabel("Nombre de clients")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Nuage de points (Âge vs Montant d'achat)
plt.figure(figsize=(8, 5))
plt.scatter(df_clients['age'], df_clients['montant_achat'], color='purple', alpha=0.6)
plt.title("Relation entre l'âge et le montant d'achat")
plt.xlabel("Âge")
plt.ylabel("Montant d'achat (€)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 3. Graphique en barres (Montant moyen par ville)
plt.figure(figsize=(8, 5))
moyenne_par_ville = df_clients.groupby('ville')['montant_achat'].mean().sort_values(ascending=False)
moyenne_par_ville.plot(kind='bar', color='coral', edgecolor='black')
plt.title("Montant moyen des achats par ville")
plt.xlabel("Ville")
plt.ylabel("Montant moyen (€)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Évite que les labels soient coupés
plt.show()