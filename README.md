
# 🤖 Reconnaissance de Gestes de la Main avec MediaPipe

Ce projet utilise **MediaPipe**, **OpenCV** et **Pillow** pour détecter et reconnaître en temps réel des **gestes de la main** via la webcam.  
L'interface vidéo affiche un texte lisible, même sur des arrière-plans complexes, grâce à un effet de contour.

---

## 📷 Démo

> *(Ajoutez ici une capture d’écran ou un GIF animé illustrant la détection des gestes)*

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

### 🔢 1. Calcul des angles (détection des postures)

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

---

## ▶️ Exécution

1. Clonez le dépôt :
```bash
git clone https://github.com/ton-utilisateur/hand-gesture-recognition.git
cd hand-gesture-recognition
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
│   └── arial.ttf         # Police TrueType utilisée pour le texte
└── README.md             # Ce fichier
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
ou
```
Geste : Paume ouverte
```

---

## 📜 Licence

Ce projet est open-source sous licence **MIT**.
