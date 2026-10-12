"""9:16-Story (1080x1920) aus einem quadratischen Produktbild mit Home-Deluxe-Overlay
(Logo oben, Navy-Verlauf unten, NEW IN / Produktname / Beschreibung) – Layout wie Sauna-EVEREST-Vorlage.
Usage: story_overlay.py <bild> <fonts_dir> <out.png>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
NAVY = (15, 35, 52)      # #0f2334
WHITE = (254, 254, 254)  # #fefefe
HERE = os.path.dirname(os.path.abspath(__file__))
SRC, FONTS, OUT = sys.argv[1:4]
MX = 108  # linker Textrand

KICKER = "NEW IN"
NAME_LIGHT = "DESIGN CARPORT"
NAME_BOLD = "FALO"
BODY = ("Schützt dein Auto zuverlässig vor Regen, Schnee und Hagel – mit robustem "
        "Aluminiumrahmen und UV-beständigem Polycarbonat-Dach.")


def font(w, size):
    return ImageFont.truetype(os.path.join(FONTS, f"Poppins-{w}.ttf"), size)


def tracked(d, x, base, s, f, track):
    for c in s:
        d.text((x, base), c, font=f, fill=WHITE, anchor="ls")
        x += f.getlength(c) + track

def tracked_w(s, f, track):
    return sum(f.getlength(c) for c in s) + track * (len(s) - 1)


# --- Hintergrund: Bild auf 1200 px skalieren, mittig auf 1080 beschneiden, Ränder auffüllen ---
img = Image.open(SRC).convert("RGB")
S = 1200
img = img.resize((S, S), Image.LANCZOS).crop(((S - W) // 2, 0, (S - W) // 2 + W, S))
TOP = 80
cv = Image.new("RGB", (W, H))
# oben: Himmel aus den obersten Zeilen strecken
cv.paste(img.crop((0, 0, W, 40)).resize((W, TOP + 40), Image.BICUBIC).filter(ImageFilter.GaussianBlur(12)), (0, 0))
# unten: Pflaster gespiegelt fortsetzen (liegt später unter dem Verlauf)
bottom_h = H - (TOP + S)
mirror = img.crop((0, S - bottom_h - 60, W, S)).transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(3))
cv.paste(mirror, (0, TOP + S - 60))
# Original mit weicher Kante drüber
mask = Image.new("L", (W, S), 255)
md = ImageDraw.Draw(mask)
for i in range(40):
    a = int(255 * i / 40)
    md.line([(0, i), (W, i)], fill=a)
    md.line([(0, S - 1 - i), (W, S - 1 - i)], fill=a)
cv.paste(img, (0, TOP), mask)
cv = cv.convert("RGBA")

# --- Verläufe: oben leicht (Logo-Lesbarkeit), unten kräftig (Textfläche) ---
grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grad)
for y in range(0, 300):
    a = (1 - y / 300) ** 1.6 * 0.55
    gd.line([(0, y), (W, y)], fill=NAVY + (int(255 * a),))
for y in range(860, H):
    p = min(1.0, (y - 860) / 500)
    a = (p ** 1.5) * 0.96
    gd.line([(0, y), (W, y)], fill=NAVY + (int(255 * a),))
cv.alpha_composite(grad)

d = ImageDraw.Draw(cv)

# --- Logo oben mittig ---
logo = Image.open(os.path.join(HERE, "homedeluxe_logo_white.webp")).convert("RGBA")
LW = 350
logo = logo.resize((LW, round(logo.height * LW / logo.width)), Image.LANCZOS)
cv.alpha_composite(logo, ((W - LW) // 2, 62))

# --- Textblock ---
f_kick = font(400, 36)
f_light = font(400, 64)
f_bold = font(700, 64)
f_body = font(400, 29)

tracked(d, MX, 1296, KICKER, f_kick, 8)
tracked(d, MX, 1432, NAME_LIGHT, f_light, 3)
tracked(d, MX, 1516, NAME_BOLD, f_bold, 3)

# Beschreibung umbrechen
maxw = W - 2 * MX
words, lines, cur = BODY.split(), [], ""
for w in words:
    t = (cur + " " + w).strip()
    if tracked_w(t, f_body, 2) <= maxw:
        cur = t
    else:
        lines.append(cur)
        cur = w
lines.append(cur)
for i, ln in enumerate(lines):
    tracked(d, MX, 1612 + i * 48, ln, f_body, 2)

cv.convert("RGB").save(OUT, quality=95)
print(OUT, len(lines), "Zeilen")
