"""Render motion-graphics overlay frames (RGBA PNG, 1080x1920 @ 24fps) for the carport reel."""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 24
SH = 22 / 24  # Polycarbonat-Szene gekuerzt (3.25s -> 4.1667s entfernt)
DUR = 10.041667 - SH
N = int(round(DUR * FPS))
NAVY = (15, 35, 52)      # #0f2334
WHITE = (254, 254, 254)  # #fefefe
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
CUTS = [2.0, 3.25, 7.458333 - SH]
X0 = 64  # left safe margin


def font(w, size):
    return ImageFont.truetype(os.path.join(FONTS, f"Poppins-{w}.ttf"), size)


# ---------- easing ----------
def clamp(v, a=0.0, b=1.0):
    return max(a, min(b, v))

def prog(t, start, dur):
    return clamp((t - start) / dur)

def ease_out(p):  # cubic
    return 1 - (1 - p) ** 3

def ease_in(p):
    return p ** 3

def ease_io(p):
    return 4 * p ** 3 if p < 0.5 else 1 - (-2 * p + 2) ** 3 / 2

def ease_back(p, s=1.6):
    p -= 1
    return p * p * ((s + 1) * p + s) + 1


# ---------- element builders ----------
def text_w(f, s, track=0):
    if not track:
        return f.getlength(s)
    return sum(f.getlength(c) for c in s) + track * (len(s) - 1)

def draw_text(d, x, base, s, f, fill, track=0):
    if not track:
        d.text((x, base), s, font=f, fill=fill, anchor="ls")
        return
    for c in s:
        d.text((x, base), c, font=f, fill=fill, anchor="ls")
        x += f.getlength(c) + track

def box(s, f, bg, fg, padx=34, pady=22, track=0, icon=None, min_h=0, arrow=False):
    """Square-cornered label box. Returns (layer, box_rect). Layer has shadow margin."""
    cap = f.getbbox("H", anchor="ls")
    cap_h = -cap[1]
    tw = text_w(f, s, track)
    icon_w = 0
    if icon:
        icon_w = int(cap_h * 1.55) + 22
    arr_w = int(cap_h * 1.25) + 18 if arrow else 0
    bw = int(tw + 2 * padx + icon_w + arr_w)
    bh = max(int(cap_h + 2 * pady), min_h)
    m = 40
    layer = Image.new("RGBA", (bw + 2 * m, bh + 2 * m), (0, 0, 0, 0))
    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([m, m + 10, m + bw, m + bh + 10], fill=NAVY + (90,))
    layer = Image.alpha_composite(layer, sh.filter(ImageFilter.GaussianBlur(16)))
    d = ImageDraw.Draw(layer)
    d.rectangle([m, m, m + bw - 1, m + bh - 1], fill=bg + (255,))
    tx = m + padx
    if icon:
        sq = int(cap_h * 1.55)
        sy = m + (bh - sq) // 2
        d.rectangle([tx, sy, tx + sq, sy + sq], fill=fg + (255,))
        # check mark
        k = sq / 10
        d.line([(tx + 2.4 * k, sy + 5.2 * k), (tx + 4.3 * k, sy + 7.1 * k), (tx + 7.8 * k, sy + 3.0 * k)],
               fill=bg + (255,), width=max(4, int(k * 1.25)), joint="curve")
        tx += icon_w
    base = m + (bh + cap_h) / 2
    draw_text(d, tx, base, s, f, fg + (255,), track)
    if arrow:
        ax0 = tx + tw + 18
        ax1 = ax0 + cap_h * 1.25
        ay = base - cap_h / 2
        lw = max(5, int(cap_h * 0.17))
        d.line([(ax0, ay), (ax1 - lw * 0.4, ay)], fill=fg + (255,), width=lw)
        hh = cap_h * 0.48
        d.line([(ax1 - hh, ay - hh), (ax1, ay), (ax1 - hh, ay + hh)], fill=fg + (255,), width=lw, joint="curve")
    return layer, m, bw, bh


class El:
    """An animated box: wipes in left->right with text sliding up, exits sliding left + fade."""

    def __init__(self, s, f, bg, fg, x, y, t_in, t_out, wipe=0.38, exit=0.26, align="l", **kw):
        self.img, self.m, self.bw, self.bh = box(s, f, bg, fg, **kw)
        self.bg = bg
        self.x = x if align == "l" else int((W - self.bw) / 2)
        self.y = y
        self.t_in, self.t_out, self.wipe, self.exit = t_in, t_out, wipe, exit

    def render(self, cv, t):
        if t < self.t_in:
            return
        p = ease_io(prog(t, self.t_in, self.wipe))
        if p <= 0:
            return
        q = ease_in(prog(t, self.t_out, self.exit)) if self.t_out else 0
        if q >= 1:
            return
        m, bw, bh = self.m, self.bw, self.bh
        dx = int(-120 * q)
        alpha = 1 - q
        # box (+shadow) revealed by width
        reveal = int(m + bw * p)
        layer = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
        # text slides up inside the box after the wipe passes
        pt = ease_out(prog(t, self.t_in + self.wipe * 0.45, self.wipe))
        boxonly = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
        ImageDraw.Draw(boxonly).rectangle([m, m, m + bw - 1, m + bh - 1], fill=self.bg + (255,))
        # shadow+box only (no text) for reveal phase
        base = self.img.copy()
        # mask text: paste box colour over text, then paste text shifted
        base.paste(boxonly.crop((m, m, m + bw, m + bh)), (m, m))
        layer.paste(base.crop((0, 0, reveal if p < 1 else self.img.size[0], self.img.size[1])), (0, 0))
        if pt > 0:
            off = int((1 - pt) * bh * 0.9)
            txt = self.img.crop((m, m, m + bw, m + bh))
            shifted = Image.new("RGBA", (bw, bh), self.bg + (255,))
            shifted.paste(txt, (0, off))
            clipw = min(bw, max(0, reveal - m))
            if clipw > 0:
                layer.paste(shifted.crop((0, 0, clipw, bh)), (m, m))
        # leading-edge accent bar during wipe
        if 0 < p < 1:
            ex = m + int(bw * p)
            acc = WHITE if self.bg == NAVY else NAVY
            ImageDraw.Draw(layer).rectangle([ex - 10, m, ex, m + bh - 1], fill=acc + (255,))
        if alpha < 1:
            a = layer.getchannel("A").point(lambda v: int(v * alpha))
            layer.putalpha(a)
        cv.alpha_composite(layer, (self.x - m + dx, self.y - m))


# ---------- scene content ----------
F_TAG = font(600, 30)
F_H1 = font(800, 118)
F_H2 = font(800, 84)
F_LB = font(700, 50)
F_SB = font(500, 36)
F_CH = font(600, 37)
F_CTA = font(700, 42)
F_URL = font(500, 32)

els = []
# Scene 1 – hook (rain)
els += [
    El("HOME DELUXE", F_TAG, NAVY, WHITE, X0, 1110, 0.02, 1.66, padx=26, pady=18, track=6),
    El("Regen?", F_H1, NAVY, WHITE, X0, 1194, 0.12, 1.70, padx=40, pady=34),
    El("Kein Problem.", F_H2, WHITE, NAVY, X0, 1378, 0.32, 1.74, padx=36, pady=28),
]
# Scene 2 – roof detail callout
S2_DOT = (330, 470)
S2_LBL_Y = 1150
els += [
    El("Polycarbonat-Dach", F_LB, NAVY, WHITE, X0, S2_LBL_Y, 2.32, 2.96, padx=34, pady=28),
    El("100 % UV-beständig", F_SB, WHITE, NAVY, X0, S2_LBL_Y + 112, 2.44, 2.99, padx=28, pady=20),
]
# Scene 3 – feature chips (aerial)
chips = ["Pulverbeschichtetes Aluminium", "Korrosionsbeständig & langlebig", "Schutz vor Regen, Schnee & Hagel"]
for i, s in enumerate(chips):
    els.append(El(s, F_CH, NAVY, WHITE, X0, 1236 + i * 92, 4.42 - SH + i * 0.22, 7.06 - SH + i * 0.05,
                  padx=24, pady=20, icon=True))
# Scene 4 – end card (sunny)
els += [
    El("HOME DELUXE", F_TAG, NAVY, WHITE, 0, 250, 7.62 - SH, None, padx=26, pady=18, track=6, align="c"),
    El("Design Carport", F_H2, NAVY, WHITE, 0, 328, 7.78 - SH, None, padx=40, pady=30, align="c"),
    El("Bei jedem Wetter geschützt.", F_SB, WHITE, NAVY, 0, 480, 7.98 - SH, None, padx=28, pady=20, align="c"),
]

# CTA button (scale-pop) + URL
cta_img, cta_m, cta_w, cta_h = box("Jetzt entdecken", F_CTA, WHITE, NAVY, padx=46, pady=30, arrow=True)
CTA_Y = 1300
url_img, url_m, url_w, url_h = box("homedeluxe.de", F_URL, NAVY, WHITE, padx=24, pady=14)


def render_cta(cv, t):
    p = prog(t, 8.25 - SH, 0.42)
    if p <= 0:
        return
    s = 0.6 + 0.4 * ease_back(p)
    img = cta_img.copy()
    # shine sweep
    sp = prog(t, 9.05 - SH, 0.55)
    if 0 < sp < 1:
        sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
        sx = cta_m - 120 + (cta_w + 240) * ease_io(sp)
        ImageDraw.Draw(sh).polygon([(sx, cta_m), (sx + 50, cta_m), (sx + 10, cta_m + cta_h), (sx - 40, cta_m + cta_h)],
                                   fill=NAVY + (55,))
        boxmask = Image.new("L", img.size, 0)
        ImageDraw.Draw(boxmask).rectangle([cta_m, cta_m, cta_m + cta_w - 1, cta_m + cta_h - 1], fill=255)
        sh.putalpha(Image.composite(sh.getchannel("A"), Image.new("L", img.size, 0), boxmask))
        img = Image.alpha_composite(img, sh)
    sw, shh = int(img.size[0] * s), int(img.size[1] * s)
    img = img.resize((sw, shh), Image.LANCZOS)
    a = img.getchannel("A").point(lambda v: int(v * clamp(p * 2.5)))
    img.putalpha(a)
    cx, cy = W / 2, CTA_Y + cta_h / 2
    cv.alpha_composite(img, (int(cx - sw / 2), int(cy - shh / 2)))
    # url
    pu = ease_out(prog(t, 8.5 - SH, 0.4))
    if pu > 0:
        u = url_img.copy()
        u.putalpha(u.getchannel("A").point(lambda v: int(v * pu)))
        cv.alpha_composite(u, (int((W - url_w) / 2 - url_m), int(CTA_Y + cta_h + 26 + (1 - pu) * 30 - url_m)))


def render_callout(cv, t):
    """Pulsing dot on the roof + connector line down to the label (scene 2)."""
    if not (2.08 <= t < 3.24):
        return
    q = ease_in(prog(t, 2.96, 0.26))
    alpha = 1 - q
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    x, y = S2_DOT
    pd = prog(t, 2.08, 0.28)
    r = 15 * ease_back(pd)
    # pulse rings
    for k in range(2):
        ph = ((t - 2.2) / 0.9 + k * 0.5) % 1.0 if t > 2.2 else None
        if ph is not None:
            rr = 16 + 60 * ease_out(ph)
            d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=WHITE + (int(220 * (1 - ph) * alpha),), width=4)
    if r > 0:
        d.ellipse([x - r - 7, y - r - 7, x + r + 7, y + r + 7], fill=NAVY + (int(255 * alpha),))
        d.ellipse([x - r, y - r, x + r, y + r], fill=WHITE + (int(255 * alpha),))
    # elbow line: down from dot, then left to label x
    pl = ease_io(prog(t, 2.16, 0.3))
    if pl > 0:
        ly = S2_LBL_Y - 30
        seg1 = ly - (y + 24)
        seg2 = x - (X0 + 30)
        tot = seg1 + seg2
        L = tot * pl
        col = WHITE + (int(255 * alpha),)
        y1 = y + 24 + min(L, seg1)
        d.line([(x, y + 24), (x, y1)], fill=col, width=5)
        if L > seg1:
            d.line([(x, ly), (x - (L - seg1), ly)], fill=col, width=5)
        if pl >= 1:
            d.rectangle([X0 + 22, ly - 8, X0 + 38, ly + 8], fill=col)
    # soft navy shadow under the line for legibility on bright drops
    shadow = lay.copy()
    sa = shadow.getchannel("A").filter(ImageFilter.GaussianBlur(6)).point(lambda v: int(v * 0.5))
    sh = Image.new("RGBA", (W, H), NAVY + (0,))
    sh.putalpha(sa)
    cv.alpha_composite(sh)
    cv.alpha_composite(lay)


# bottom gradient for end card legibility
GRAD = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(GRAD)
for yy in range(900, H):
    a = clamp((yy - 900) / 600) ** 1.4 * 0.62
    gd.line([(0, yy), (W, yy)], fill=NAVY + (int(255 * a),))


def render_grad(cv, t):
    p = ease_io(prog(t, 7.46 - SH, 0.5))
    if p <= 0:
        return
    g = GRAD.copy()
    g.putalpha(g.getchannel("A").point(lambda v: int(v * p)))
    cv.alpha_composite(g)


def render_sweep(cv, t):
    """Diagonal navy/white stripe wipe across each cut."""
    for c in CUTS:
        span = 0.40
        p = (t - (c - span / 2)) / span
        if not (0 <= p <= 1):
            continue
        e = ease_io(p)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(lay)
        skew = 700
        cx = -900 + (W + 1800) * e
        for off, wdt, col in [(0, 260, NAVY + (235,)), (285, 34, WHITE + (235,)), (-60, 22, WHITE + (200,))]:
            x0 = cx + off
            d.polygon([(x0, 0), (x0 + wdt, 0), (x0 + wdt - skew, H), (x0 - skew, H)], fill=col)
        cv.alpha_composite(lay)


for i in range(N):
    t = i / FPS
    cv = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    render_grad(cv, t)
    render_callout(cv, t)
    for e in els:
        e.render(cv, t)
    render_cta(cv, t)
    render_sweep(cv, t)
    cv.save(os.path.join(OUT, f"o_{i:04d}.png"), compress_level=1)
print("frames", N)
