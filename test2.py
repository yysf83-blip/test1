import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Traceur de Fonction Linéaire")

# Saisie des valeurs de a et b
a = st.number_input("Entrez la valeur de a:", value=1.0)
b = st.number_input("Entrez la valeur de b:", value=0.0)

# Calculer les valeurs de x et y
x = np.linspace(-10, 10, 100)
y = a * x + b

# Tracer la fonction
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'y = {a}x + {b}', color='blue')
plt.title('Graphique de la fonction y = ax + b')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Ligne horizontale du zéro
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Ligne verticale du zéro
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Ajouter une grille
plt.legend()  # Afficher la légende
plt.xlim(-10, 10)  # Limites des x
plt.ylim(-20, 20)  # Limites des y

# Afficher le graphique
st.pyplot(plt)
