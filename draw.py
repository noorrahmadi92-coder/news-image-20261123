#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news front page (1024x1024 PNG).

Deterministic: no randomness, no network, no timestamps. Pillow only.
Run: python3 draw.py  -> writes entry.png beside this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

PAPER = (247, 243, 232)
INK = (26, 26, 26)
NAVY = (24, 38, 64)
NAVY_D = (16, 26, 46)
GOLD = (201, 162, 75)
GOLD_L = (232, 196, 110)
RED = (178, 34, 34)
TEAL = (18, 92, 96)
RUST = (176, 92, 32)
CREAM = (250, 246, 236)
GREY = (90, 90, 88)
RULE = (150, 140, 120)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    """Draw wrapped text; returns y just below the last line."""
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hline(draw, x0, x1, y, fill, width=1):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def label(draw, x, y, text, color, size=21):
    """Small caps section label with a short rule after it."""
    fnt = font(SANS_B, size)
    draw.text((x, y), text, font=fnt, fill=color)
    w = draw.textlength(text, font=fnt)
    hline(draw, x + w + 10, x + w + 46, y + size // 2 + 1, color, 3)
    return y + size + 6


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 118], fill=NAVY)
d.rectangle([0, 118, W, 124], fill=GOLD)
d.text((28, 14), "THE WORLD IN ONE DAY", font=font(SANS_B, 24),
       fill=GOLD_L)
d.text((28, 40), "WORLD NEWS", font=font(SERIF, 58), fill=(250, 248, 240))
d.text((28, 96), "Monday, 23 November 2026",
       font=font(SANS_B, 22), fill=GOLD_L)
d.text((W - 28, 22), "SIX STORIES", font=font(SANS_B, 30),
       fill=(250, 248, 240), anchor="ra")
d.text((W - 28, 56), "that defined the day", font=font(SANS, 22),
       fill=(210, 210, 205), anchor="ra")
d.text((W - 28, 94), "ANTALYA  •  HORMUZ  •  KYIV",
       font=font(SANS_B, 17), fill=GOLD_L, anchor="ra")

# ------------------------------------------------------------- hero: COP31
HX, HY, HW, HH = 28, 140, 968, 330
d.rectangle([HX, HY, HX + HW, HY + HH], outline=INK, width=2)
# conference hall: dark teal wall, floor, rows of empty delegate chairs
d.rectangle([HX + 2, HY + 2, HX + HW - 2, HY + 168], fill=(30, 62, 70))
d.rectangle([HX + 2, HY + 168, HX + HW - 2, HY + HH - 2], fill=(58, 74, 66))
for i, cx in enumerate(range(HX + 60, HX + HW - 60, 92)):
    # chair back + seat, alternating muted colours, all empty
    col = (96, 116, 118) if i % 2 == 0 else (120, 110, 88)
    d.rounded_rectangle([cx, HY + 96, cx + 56, HY + 168],
                        radius=8, fill=col, outline=(20, 34, 38), width=2)
    d.rectangle([cx + 8, HY + 132, cx + 48, HY + 168], fill=(70, 84, 86))
# podium + broken pact document
d.rectangle([HX + HW // 2 - 130, HY + 60, HX + HW // 2 + 130, HY + 168],
            fill=(74, 58, 44), outline=(40, 30, 22), width=2)
d.polygon([(HX + HW // 2 - 118, HY + 96), (HX + HW // 2 - 88, HY + 62),
           (HX + HW // 2 + 20, HY + 62), (HX + HW // 2 + 118, HY + 96),
           (HX + HW // 2 + 88, HY + 118), (HX + HW // 2 - 88, HY + 118)],
          fill=(244, 240, 228), outline=(120, 110, 96))
d.line([(HX + HW // 2 - 88, HY + 62), (HX + HW // 2 - 20, HY + 96),
        (HX + HW // 2 + 40, HY + 74), (HX + HW // 2 + 88, HY + 118)],
       fill=(140, 30, 30), width=4)
for lx in range(HX + HW // 2 - 96, HX + HW // 2 + 100, 26):
    d.line([(lx, HY + 104), (lx + 12, HY + 104)], fill=(150, 142, 126),
           width=2)
# red NO DEAL stamp, rotated — inside the hall band, above the caption
stamp = Image.new("RGBA", (300, 110), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([6, 6, 294, 104], outline=(178, 34, 34), width=7)
sd.text((150, 55), "NO DEAL", font=font(SANS_B, 56), fill=(178, 34, 34),
        anchor="mm")
stamp = stamp.rotate(8, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (HX + HW - 320, HY + 16), stamp)
d = ImageDraw.Draw(img)
# hero caption block under the hall scene
d.rectangle([HX, HY + 172, HX + HW, HY + HH], fill=CREAM)
label(d, HX + 18, HY + 184, "LEAD STORY  •  COP31, ANTALYA", RED, 21)
d.text((HX + 18, HY + 214), "COP31 collapses — no deal on climate",
       font=font(SERIF, 40), fill=INK)
text_block(d, HX + 18, HY + 262,
           "UN climate talks ended Sunday with no agreement at all — the "
           "longest COP on record. The draft Antalya Pact never mentioned "
           "fossil fuels. Next try: COP32 in Addis Ababa, Nov 2027.",
           font(SANS, 21), INK, HW - 36, leading=27)

# ------------------------------------------------- second row: two panels
RY, RH = 486, 252
PW = 474
# --- left: Hormuz tankers (image band 88px, text below has room)
LX, LW = 28, PW
d.rectangle([LX, RY, LX + LW, RY + RH], outline=INK, width=2)
d.rectangle([LX + 2, RY + 2, LX + LW - 2, RY + 90], fill=(14, 34, 52))
# sea + tanker silhouettes + flames
d.rectangle([LX + 2, RY + 60, LX + LW - 2, RY + 90], fill=(24, 58, 78))
for tx, tw, th in [(LX + 40, 150, 30), (LX + 250, 170, 34)]:
    d.rectangle([tx, RY + 90 - th - 14, tx + tw, RY + 90 - 14],
                fill=(12, 12, 14))
    d.rectangle([tx + tw - 34, RY + 90 - th - 36, tx + tw - 18,
                 RY + 90 - th - 14], fill=(12, 12, 14))
    d.rectangle([tx + 8, RY + 90 - th - 22, tx + tw - 8, RY + 90 - 14],
                fill=(52, 44, 34))
# flames and smoke over the second tanker
for fx, fy, r in [(LX + 300, RY + 32, 13), (LX + 330, RY + 22, 16),
                  (LX + 362, RY + 34, 11)]:
    d.ellipse([fx - r, fy - r, fx + r, fy + r], fill=(232, 132, 30))
    d.ellipse([fx - r // 2, fy - r // 2, fx + r // 2, fy + r // 2],
              fill=(250, 200, 60))
for sx, sy, r in [(LX + 310, RY + 10, 10), (LX + 348, RY + 6, 12),
                  (LX + 384, RY + 12, 8)]:
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(120, 118, 112))
d.rectangle([LX, RY + 92, LX + LW, RY + RH], fill=CREAM)
label(d, LX + 16, RY + 102, "ENERGY  •  STRAIT OF HORMUZ", RUST, 19)
d.text((LX + 16, RY + 128), "Tankers hit in the\nStrait of Hormuz",
       font=font(SERIF, 30), fill=INK)
text_block(d, LX + 16, RY + 202,
           "At least three struck Fri–Sat; two more on fire Sunday.",
           font(SANS, 18), INK, LW - 32, leading=21)

# --- right: Dymer drone strike
RX = 522
d.rectangle([RX, RY, RX + PW, RY + RH], outline=INK, width=2)
d.rectangle([RX + 2, RY + 2, RX + PW - 2, RY + 90], fill=(18, 22, 40))
# night sky, apartment block, drone, searchlight
d.rectangle([RX + 60, RY + 26, RX + 180, RY + 90], fill=(52, 56, 66))
for wy in range(RY + 34, RY + 82, 16):
    for wx in range(RX + 72, RX + 168, 26):
        d.rectangle([wx, wy, wx + 12, wy + 9], fill=(240, 200, 90))
d.rectangle([RX + 96, RY + 52, RX + 144, RY + 90], fill=(16, 16, 20))
d.polygon([(RX + 300, RY + 22), (RX + 340, RY + 34), (RX + 300, RY + 46),
           (RX + 318, RY + 34)], fill=(200, 200, 200))
d.ellipse([RX + 352, RY + 28, RX + 360, RY + 36], fill=(250, 120, 40))
d.polygon([(RX + 120, RY + 90), (RX + 200, RY + 22), (RX + 280, RY + 90)],
          fill=(240, 210, 110))
d.rectangle([RX, RY + 92, RX + PW, RY + RH], fill=CREAM)
label(d, RX + 16, RY + 102, "UKRAINE  •  DYMER, NORTH OF KYIV", TEAL, 19)
d.text((RX + 16, RY + 128), "Drone hits flats\nnear Kyiv",
       font=font(SERIF, 30), fill=INK)
text_block(d, RX + 16, RY + 202,
           "2 killed, 11 missing — incl. two children — in Dymer.",
           font(SANS, 18), INK, PW - 32, leading=21)

# ------------------------------------------------ bottom strip: three cards
BY, BH, BW, GAP = 754, 204, 312, 16


def bottom_card(x, band, accent, tag, headline, body, draw_art):
    d.rectangle([x, BY, x + BW, BY + BH], outline=INK, width=2)
    d.rectangle([x + 2, BY + 2, x + BW - 2, BY + 66], fill=band)
    draw_art(x)
    d.rectangle([x, BY + 68, x + BW, BY + BH], fill=CREAM)
    label(d, x + 14, BY + 78, tag, accent, 17)
    text_block(d, x + 14, BY + 104, headline, font(SERIF, 24), INK,
               BW - 28, leading=28)
    text_block(d, x + 14, BY + 104 + 56, body, font(SANS, 17), INK,
               BW - 28, leading=21)


def art_benghazi(x):
    # dark sea, grey corvette, small sea drone + white splash
    d.rectangle([x + 2, BY + 46, x + BW - 2, BY + 66], fill=(30, 70, 96))
    d.rectangle([x + 60, BY + 30, x + 250, BY + 48], fill=(70, 74, 80))
    d.rectangle([x + 120, BY + 16, x + 150, BY + 30], fill=(70, 74, 80))
    d.rectangle([x + 150, BY + 16, x + 152, BY + 22], fill=(70, 74, 80))
    d.ellipse([x + 262, BY + 40, x + 292, BY + 58], fill=(240, 246, 250))
    d.ellipse([x + 272, BY + 34, x + 282, BY + 44], fill=(40, 44, 50))


def art_cikande(x):
    # factory block, orange flames, grey smoke
    d.rectangle([x + 40, BY + 28, x + 180, BY + 66], fill=(96, 88, 80))
    d.rectangle([x + 190, BY + 14, x + 210, BY + 66], fill=(96, 88, 80))
    for fx, fy, r in [(x + 70, BY + 22, 12), (x + 100, BY + 14, 15),
                      (x + 132, BY + 24, 11)]:
        d.ellipse([fx - r, fy - r, fx + r, fy + r], fill=(232, 132, 30))
        d.ellipse([fx - r // 2, fy - r // 2, fx + r // 2, fy + r // 2],
                  fill=(250, 200, 60))
    for sx, sy, r in [(x + 230, BY + 18, 11), (x + 258, BY + 10, 13)]:
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(130, 128, 122))


def art_mercury(x):
    # cratered Mercury + small probe with solar panels
    d.ellipse([x + 30, BY + 4, x + 110, BY + 64], fill=(198, 142, 86))
    for cx, cy, r in [(x + 52, BY + 22, 7), (x + 78, BY + 40, 9),
                      (x + 60, BY + 48, 5), (x + 88, BY + 18, 5)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(168, 110, 62))
    d.rectangle([x + 190, BY + 26, x + 230, BY + 42], fill=(30, 60, 90))
    d.rectangle([x + 150, BY + 32, x + 190, BY + 36], fill=(70, 110, 160))
    d.rectangle([x + 230, BY + 32, x + 270, BY + 36], fill=(70, 110, 160))
    d.ellipse([x + 236, BY + 20, x + 244, BY + 28], fill=(250, 200, 60))


bottom_card(28, (16, 30, 48), (30, 70, 120), "LIBYA  •  BENGHAZI",
            "Sea drones hit Russian warship",
            "Corvette Merkury struck at naval base; UN urges a probe.",
            art_benghazi)
bottom_card(28 + BW + GAP, (52, 30, 24), RUST, "INDONESIA  •  CIKANDE",
            "Candy factory fire in Banten",
            "Dozens still missing; search resumes Monday.",
            art_cikande)
bottom_card(28 + 2 * (BW + GAP), (20, 24, 44), (90, 60, 140),
            "SPACE  •  MERCURY",
            "BepiColombo reaches Mercury orbit",
            "Only the second mission ever to orbit Mercury.",
            art_mercury)

# ------------------------------------------------------------------ footer
hline(d, 28, W - 28, 976, RULE, 2)
d.text((28, 986), "Sources: Reuters, AP, CNN, Al Jazeera, BBC  •  23 November 2026",
       font=font(SANS, 18), fill=GREY)
d.text((W - 28, 986), "make.fun  •  news-image-20261123",
       font=font(SANS, 18), fill=GREY, anchor="ra")

img.save(OUT, "PNG")
print("wrote", OUT, os.path.getsize(OUT), "bytes")
