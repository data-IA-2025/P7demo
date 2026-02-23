"""
Genere le logo SANITORAL pour le projet P7demo
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Creer une image avec fond bleu ciel
width, height = 1200, 400
bg_color = (173, 216, 230)  # Bleu ciel (light blue)
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Essayer d'utiliser une police, sinon utiliser la par defaut
try:
    font_title = ImageFont.truetype("arial.ttf", 120)
    font_subtitle = ImageFont.truetype("arial.ttf", 40)
except:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()

# Dessiner un coeur dentaire stylise (cercle avec coeur)
# Position du coeur
heart_x, heart_y = 150, 200
heart_size = 80

# Dessiner le coeur (representation simple avec des courbes)
# Demi-cercles pour les "bosses" du coeur
draw.ellipse([heart_x - heart_size//2, heart_y - heart_size, 
              heart_x, heart_y - heart_size//2], 
             fill='white', outline='#008B8B', width=3)
draw.ellipse([heart_x, heart_y - heart_size, 
              heart_x + heart_size//2, heart_y - heart_size//2], 
             fill='white', outline='#008B8B', width=3)

# Triangle pour le bas du coeur
points = [(heart_x - heart_size//2, heart_y - heart_size//2),
          (heart_x + heart_size//2, heart_y - heart_size//2),
          (heart_x, heart_y + heart_size//2)]
draw.polygon(points, fill='#20B2AA', outline='#008B8B')

# Ajouter le texte "SANITORAL"
text = "SANITORAL"
bbox = draw.textbbox((0, 0), text, font=font_title)
text_width = bbox[2] - bbox[0]
text_x = (width - text_width) // 2 + 100
text_y = (height - (bbox[3] - bbox[1])) // 2

draw.text((text_x, text_y), text, fill='black', font=font_title)

# Ajouter un sous-titre
subtext = "Gestion des Projets Sanitaires"
bbox_sub = draw.textbbox((0, 0), subtext, font=font_subtitle)
sub_width = bbox_sub[2] - bbox_sub[0]
sub_x = (width - sub_width) // 2
sub_y = text_y + 100

draw.text((sub_x, sub_y), subtext, fill='#333333', font=font_subtitle)

# Sauvegarder le fichier
output_dir = Path("img")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "sanitoral_logo.png"

img.save(output_path)
print(f"✓ Logo sauvegarde: {output_path}")
print(f"✓ Dimensions: {width}x{height} pixels")
