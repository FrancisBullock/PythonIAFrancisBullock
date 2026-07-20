import pandas as pd

# 1. Chargement
df_clients = pd.read_csv('clients.csv')

print("--- QUESTION 2 : MANIPULATION PANDAS ---")

# 2. Affichages
print(f"Nombre total de clients : {len(df_clients)}")
print("\n5 premières lignes :")
print(df_clients.head())
print("\nStatistiques descriptives :")
print(df_clients.describe())

# 3. Montant moyen par ville
print("\nMontant moyen des achats par ville :")
print(df_clients.groupby('ville')['montant_achat'].mean())

# 4 & 5. Extraction Premium et Sauvegarde
clients_premium = df_clients[df_clients['montant_achat'] > 500]
print(f"\nNombre de clients premium (> 500€) : {len(clients_premium)}")
clients_premium.to_csv('clients_premium.csv', index=False)
print("Fichier 'clients_premium.csv' créé avec succès.")