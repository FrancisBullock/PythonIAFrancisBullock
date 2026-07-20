import numpy as np

# 1. Création du tableau NumPy
ventes = np.array([12, 15, 14, 10, 18, 20, 17, 16, 13, 19, 22, 21, 18, 17, 23])

# 2. Calcul de la moyenne, médiane et écart-type
moyenne = np.mean(ventes)
mediane = np.median(ventes)
ecart_type = np.std(ventes)

# 3. Identification des ventes supérieures à la moyenne
ventes_sup_moyenne = ventes[ventes > moyenne]

# 4. Normalisation Z-score
ventes_normalisees = (ventes - moyenne) / ecart_type

# 5. Affichage des résultats
print("--- ANALYSE DES VENTES AVEC NUMPY ---")
print(f"Tableau des ventes : {ventes}")
print(f"Moyenne : {moyenne:.2f} milliers d'euros")
print(f"Médiane : {mediane:.2f} milliers d'euros")
print(f"Écart-type : {ecart_type:.2f}")
print(f"Ventes supérieures à la moyenne : {ventes_sup_moyenne}")
print("\nDonnées normalisées (Z-score) :")
for v, v_norm in zip(ventes, ventes_normalisees):
    print(f"  Vente initiale: {v} -> Normalisée: {v_norm:.4f}")