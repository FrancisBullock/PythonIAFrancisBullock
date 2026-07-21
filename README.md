 Initiation Python IA
 21 Juillet 2026  



Ce dépôt contient la résolution complète des exercices du devoir de rattrapage en Initiation Python IA.



  Technologies et bibliothèques utilisées

* Python 3.x
* NumPy : Calcul numérique et normalisation des données.
* Pandas : Manipulation, filtrage et traitement des données tabulaires (CSV).
* Matplotlib : Représentation graphique des données (histogrammes, nuages de points, diagrammes en barres).
* Scikit-Learn : Création, entraînement et évaluation de modèles de régression linéaire (simple et multiple).

---

 Structure du projet

* `question1.py` : Analyse numérique des ventes journalières avec NumPy (moyenne, médiane, écart-type, normalisation Z-score).
* `question2.py` : Manipulation du jeu de données `clients.csv` avec Pandas et extraction des clients premium dans `clients_premium.csv`.
* `question3.py` : Visualisation graphique des données clients avec Matplotlib.
* `question4.py` : Régression linéaire simple avec Scikit-Learn (prédiction du montant d'achat selon l'âge).
* `question5.py` : Étude complète du fichier `ventes.csv` (analyse exploratoire, matrice de corrélation et régression linéaire multiple).
* `clients.csv` / `ventes.csv` : Jeux de données d'entrée.

---

 Installation et exécution

1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/ton-pseudo/rattrapage-python-ia.git](https://github.com/ton-pseudo/rattrapage-python-ia.git)
   cd rattrapage-python-ia

   2 Installer les dépendances:
 pip install numpy pandas matplotlib scikit-learn

 python -m pip install pandas numpy matplotlib scikit-learn --break-system-packages --trusted-host pypi.org --trusted-host files.pythonhosted.org

 3:Exécuter un script spécifique
 python question1.py
python question2.py
python question3.py
python question4.py
python question5.py