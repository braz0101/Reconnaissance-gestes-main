
# ✋ Reconnaissance de Gestes de la Main avec MediaPipe

Ce projet utilise **MediaPipe**, **OpenCV** et **Pillow** pour détecter et reconnaître en temps réel des **gestes de la main** via la webcam.  
L'interface vidéo affiche un texte lisible, même sur des arrière-plans complexes, grâce à un effet de contour.

---

## 📷 Démo

![deux doigts levés](https://github.com/user-attachments/assets/29c9bf7a-2230-403a-8c29-23695b77dd37)

![poing fermé](https://github.com/user-attachments/assets/41e28134-fd78-4761-95a4-a6ee8cb508e9)

---

## ✨ Fonctionnalités

- 🎯 Détection en temps réel de **4 gestes prédéfinis**
- 🧠 Basée sur les **landmarks** de MediaPipe
- 🖼️ Texte lisible grâce à un **effet de surimpression stylisé**
- 🎨 Prise en charge des **polices personnalisées** (y compris Unicode/Emoji)

---

## 🧠 Gestes Reconnaissables

| Geste              | Condition de détection                                      |
|--------------------|-------------------------------------------------------------|
| 👍 Pouce levé       | Pouce étendu, autres doigts repliés                         |
| ✋ Paume ouverte    | Tous les doigts étendus                                     |
| ✌️ Deux doigts levés | Index et majeur levés, les autres doigts repliés            |
| ✊ Poing fermé       | Tous les doigts repliés (aucun doigt levé)                  |

---

## 🔍 Explication du Code

### 📐 1. Calcul des angles (détection des postures)

```python
def calculate_angle(a, b, c):
    # Calcule l’angle entre trois points
```

Utile pour déterminer si un doigt est levé ou replié (ex. : détection du pouce levé).

---

### ✋ 2. Fonctions de détection des gestes

```python
is_thumb_up(landmarks)          # Seul le pouce est levé
is_palm_open(landmarks)         # Tous les doigts sont étendus
is_two_fingers_up(landmarks)    # Index et majeur levés uniquement
is_fist_closed(landmarks)       # Tous les doigts repliés
```

---

### 🎨 3. Affichage lisible avec texte en contour

```python
draw_text_with_outline(...)
```

Utilise Pillow pour afficher du texte avec contour/ombre, pour une meilleure lisibilité.

---

### 🎥 4. Capture Vidéo en Temps Réel

Le flux vidéo est capturé via **OpenCV**, traité image par image avec **MediaPipe** pour détecter les mains, puis les gestes sont identifiés.


https://github.com/user-attachments/assets/32e87459-0b99-492e-884d-6dd4595462f0


---

## ⚡ Exécution

1. Clonez le dépôt :
```bash
git clone https://github.com/braz0101/Reconnaissance-gestes-main.git
cd Reconnaissance-gestes-main
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez le script :
```bash
python main.py
```

Appuyez sur Échap pour fermer la fenêtre.

---

## 📁 Structure du Projet

```
hand-gesture-recognition/
├── main.py               # Script principal
├── requirements.txt      # Dépendances Python
├── fonts/
│   └── arial.ttf         # Police TrueType utilisée pour le texte (Personnalisable)
└── README.md             
```

---

## 🖋️ Police Personnalisée

Le script utilise `arial.ttf`. Si elle n’est pas disponible :

✅ Options :

- **Windows** : Copiez `C:\Windows\Fonts\arial.ttf` vers `fonts/arial.ttf`
- **Linux/macOS** : Utilisez une alternative libre (Noto Sans, DejaVu Sans, Liberation Sans)

Modifiez le chemin dans le script si nécessaire :

```python
draw_text_with_outline(..., font_path="fonts/arial.ttf")
```

---

## 🧪 Exemple de Résultat

Lors de l’exécution avec une webcam, vous verrez une vidéo enrichie d’un encadré semi-transparent indiquant :

```
Geste : Pouce levé
```
![pouce levé](https://github.com/user-attachments/assets/fde029e6-c16c-4129-94dc-fd8eb6df4de5)

ou
```
Geste : Paume ouverte
```
![paume ouverte](https://github.com/user-attachments/assets/5e599413-37c1-4fcf-a32f-8b271b4a959d)
---

## 📜 Licence

Ce projet est open-source sous licence **MIT**.

⚠️ Droit à l’image
📸 Les captures d’écran et vidéos présentes dans ce dépôt sont uniquement fournies à des fins de démonstration.
❌ Leur réutilisation, reproduction ou diffusion sans mon accord explicite est interdite.
Ces médias peuvent contenir des éléments personnels soumis au droit à l’image.
