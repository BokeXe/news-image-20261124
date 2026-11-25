#!/usr/bin/env python3
"""news-image-20261124 v2: render Tuesday 24 November 2026 in one image.

Deterministic Pillow render: fixed data, fixed fonts, no clock, no network.
Writes entry.png (1024x1024) into MAKEFUN_OUTPUT_DIR or /output.
Design goal: masthead date + three lead headlines readable at ~300px;
all 38 stories kept, grouped by region in large type.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
INK = (15, 23, 42)
PAPER = (248, 250, 252)
CARD = (255, 255, 255)
LINE = (226, 232, 240)
MUT = (100, 116, 139)
BLUE = (37, 99, 235)
AMBER = (245, 158, 11)
RED = (220, 38, 38)
GREEN = (5, 150, 105)
TEAL = (13, 148, 136)
PURPLE = (124, 58, 237)
WHITE = (255, 255, 255)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


LEADS = [
    ("DIPLOMACY", BLUE, "Trump meets Zelenskyy in Washington",
     ["Peace terms, minerals deal,", "NATO-style security guarantees.", "Kyiv targets a January deal."]),
    ("WAR", RED, "Russian missiles + drone hit Poland",
     ["NATO airspace breached; Warsaw", "summons Moscow's ambassador.", "Strikes across Ukraine kill 8."]),
    ("WAR", RED, "Houthis strike KAFD tower, Riyadh",
     ["Saudi-led coalition calls it a", "terror attack on finance district.", "Houthis advance near Aden."]),
]

REGIONS = [
    ("NORTH AMERICA", 6, BLUE, [
        "Nvidia rally lifts Nasdaq +7%",
        "Trump adds 10% tariff on China",
        "US probe targets 16 trade partners",
        "Senators move to cut Iran war funds",
        "Bitcoin slips below $60,000",
    ]),
    ("LATIN AMERICA", 3, TEAL, [
        "Mexico hands 29 cartel inmates to US",
        "Brazil shares fall on Lula package",
        "Argentina may scrap PASO primaries",
    ]),
    ("WESTERN EUROPE", 5, PURPLE, [
        "Czechs beat Canada 2-0, Davis Cup",
        "EU leaders weigh Ukraine funding",
        "German support for Ukraine aid falls",
        "UK sanctions Myanmar after ICJ ruling",
        "After COP31: world at +1.46°C",
    ]),
    ("EASTERN EUROPE", 6, RED, [
        "Ukraine hits Kerch Bridge again",
        "Pentagon delays Patriot missiles",
        "Hungary PM backs Ukraine EU bid",
        "Finland weighs tank barriers",
        "Zaporizhzhia strike kills 2, wounds 22",
    ]),
    ("MIDDLE EAST", 5, AMBER, [
        "Gaza strikes kill Hamas security chief",
        "US sanctions Iran shadow banks",
        "Iran orders Hormuz shut further*",
        "Palestinians agree Gaza disarm plan",
    ]),
    ("AFRICA", 2, GREEN, [
        "175 migrants missing off Senegal",
        "Darfur refugees face winter, aid cut",
    ]),
    ("SOUTH ASIA", 3, TEAL, [
        "India 3rd in Asia Power Index",
        "Japan fires missiles in India drill",
        "Pakistani astronaut to Tiangong",
    ]),
    ("EAST ASIA", 5, BLUE, [
        "China extends rare-earth export pause",
        "S. Korea scrambles jets vs Russia",
        "Shanghai party chief probed",
        "China-Singapore yuan financing",
        "Korea-China widen trade deal",
    ]),
    ("SE ASIA + OCEANIA", 3, PURPLE, [
        "VP Gibran resigns in Indonesia",
        "Hanoi restaurant blast kills 6+",
        "Indonesia factory fire: 24 bodies",
    ]),
]

BTC = [("Fri 21", 60216), ("Sat 22", 61271), ("Mon 23", 61271), ("Tue 24", 59748)]

DATE_CHECK = [
    "Mexico's 29-inmate transfer: 23 Nov, reported 24 Nov",
    "US Iran sanctions designated 23 Nov",
    "COP31 collapse was 22 Nov; 24 Nov = fallout only",
    "Indonesia factory fire began 23 Nov; toll updated 24 Nov",
]

HOW_SURE = [
    ("CONFIRMED", GREEN, "multiple reports"),
    ("OFFICIAL", BLUE, "government / agency"),
    ("REPORTED", AMBER, "single dated report"),
    ("CLAIMED*", RED, "asserted, unverified"),
]


def card(d, box, r=14, fill=CARD, outline=LINE):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=1)


def pill(d, x, y, text, color, font, fg=WHITE):
    tw = d.textlength(text, font=font)
    d.rounded_rectangle([x, y, x + tw + 22, y + 24], radius=10, fill=color)
    d.text((x + 11, y + 3), text, font=font, fill=fg)
    return x + tw + 22


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

WORLD = [
    "      ####                                    ",
    "  ###########        ##   ###                 ",
    " #############      ##################        ",
    "  ###########      ####################       ",
    "   #########        ##################        ",
    "    #######          ################         ",
    "     #####            ############    ##      ",
    "     ####              ##########    ####     ",
    "     ###                ########      ###     ",
    "     ##                  ######        #      ",
    "     #                    ####                ",
]


def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 116], fill=INK)
    d.text((28, 14), "TUESDAY, 24 NOVEMBER 2026", font=f(FB, 39), fill=WHITE)
    d.text((28, 66), "THE WORLD IN ONE DAY   ·   38 STORIES   ·   9 REGIONS   ·   24 FIELDS",
           font=f(FB, 17), fill=AMBER)
    d.rounded_rectangle([716, 20, 996, 96], radius=12, fill=(30, 41, 59))
    d.text((732, 28), "BTC  $59,748", font=f(FB, 24), fill=WHITE)
    d.text((732, 60), "-2.71%  ON TUESDAY", font=f(FB, 15), fill=(248, 113, 113))

    # Lead cards
    for i, (kick, color, head, det) in enumerate(LEADS):
        x = 24 + i * 328
        card(d, [x, 128, x + 320, 332])
        d.rounded_rectangle([x, 128, x + 320, 136], radius=4, fill=color)
        pill(d, x + 16, 148, kick, color, f(FB, 12))
        d.text((x + 250, 148), f"LEAD {i + 1}", font=f(FB, 12), fill=MUT)
        y = 182
        for ln in wrap(d, head, f(FB, 23), 288):
            d.text((x + 16, y), ln, font=f(FB, 23), fill=INK)
            y += 28
        y += 6
        for ln in det:
            d.text((x + 16, y), ln, font=f(FR, 13), fill=(71, 85, 105))
            y += 18

    # Region strip
    short = [("N. AMERICA", 6, BLUE), ("LATIN AM.", 3, TEAL), ("W. EUROPE", 5, PURPLE),
             ("E. EUROPE", 6, RED), ("MID EAST", 5, AMBER), ("AFRICA", 2, GREEN),
             ("S. ASIA", 3, TEAL), ("E. ASIA", 5, BLUE), ("SE ASIA", 3, PURPLE)]
    x = 24
    for name, n, color in short:
        x = pill(d, x, 346, f"{name}  {n}", color, f(FB, 12)) + 8
    d.text((24, 376), "All 38 stories below, grouped by region. Counts include the three leads.",
           font=f(FR, 12), fill=MUT)

    # BTC chart card
    card(d, [24, 396, 500, 566])
    d.text((40, 408), "BITCOIN - DAILY CLOSE (USD)", font=f(FB, 14), fill=INK)
    d.text((40, 430), "$59,748", font=f(FB, 24), fill=INK)
    d.text((150, 436), "-2.71% Tue", font=f(FB, 16), fill=RED)
    d.text((262, 438), "back below $60k", font=f(FR, 12), fill=MUT)
    lo, hi = 59000, 62000
    pts = []
    for i, (lab, v) in enumerate(BTC):
        px = 64 + i * 128
        py = 532 - (v - lo) / (hi - lo) * 62
        pts.append((px, py))
    d.polygon(pts + [(pts[-1][0], 532), (pts[0][0], 532)], fill=(219, 234, 254))
    d.line(pts, fill=BLUE, width=3)
    for (px, py), (lab, v) in zip(pts, BTC):
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=BLUE, outline=WHITE, width=2)
        d.text((px - 20, py - 24), f"${v / 1000:.1f}k", font=f(FB, 11), fill=INK)
        d.text((px - 18, 540), lab, font=f(FR, 11), fill=MUT)

    # Map card
    card(d, [512, 396, 1000, 566])
    d.text((528, 408), "WHERE IT HAPPENED", font=f(FB, 14), fill=INK)
    for r, row in enumerate(WORLD):
        for c, ch in enumerate(row):
            if ch == "#":
                gx, gy = 540 + c * 9, 438 + r * 9
                d.ellipse([gx, gy, gx + 4, gy + 4], fill=(148, 163, 184))
    for (px, py, lab, lx, ly) in [(596, 452, "WASHINGTON", 548, 428),
                                  (758, 446, "POLAND", 730, 424),
                                  (806, 470, "RIYADH", 820, 464)]:
        d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED, outline=WHITE, width=2)
        d.text((lx, ly), lab, font=f(FB, 11), fill=INK)
    d.text((528, 540), "Red pins: the three lead stories.", font=f(FR, 11), fill=MUT)

    # Story columns
    cols = [[0, 1, 5, 6], [2, 3, 8], [4, 7]]
    for ci, idxs in enumerate(cols):
        x = 24 + ci * 328
        y = 580
        for ri in idxs:
            name, n, color, stories = REGIONS[ri]
            d.rectangle([x, y + 2, x + 10, y + 14], fill=color)
            d.text((x + 16, y), name, font=f(FB, 14), fill=INK)
            pill(d, x + 268, y - 2, str(n), color, f(FB, 11))
            y += 23
            for s in stories:
                d.ellipse([x + 2, y + 5, x + 7, y + 10], fill=color)
                d.text((x + 14, y), s, font=f(FR, 13), fill=(30, 41, 59))
                y += 16
            y += 6
    # Big numbers box under column 3
    bx, by = 680, 804
    card(d, [bx, by, bx + 320, 908], fill=(15, 23, 42), outline=INK)
    d.text((bx + 16, by + 8), "NUMBERS OF THE DAY", font=f(FB, 12), fill=AMBER)
    nums = [("8", "killed in strikes on Ukraine"), ("175", "migrants missing off Senegal"),
            ("+7%", "Nasdaq on Monday's rally"), ("+1.46°C", "world vs pre-industrial")]
    yy = by + 30
    for big, small in nums:
        d.text((bx + 16, yy), big, font=f(FB, 15), fill=WHITE)
        d.text((bx + 88, yy + 2), small, font=f(FR, 11), fill=(203, 213, 225))
        yy += 19

    # Bottom boxes
    card(d, [24, 916, 640, 1000])
    d.text((40, 924), "DATE CHECK - reported Tue, happened earlier", font=f(FB, 13), fill=INK)
    yy = 946
    for ln in DATE_CHECK:
        d.text((40, yy), "- " + ln, font=f(FR, 11), fill=(71, 85, 105))
        yy += 14
    card(d, [652, 916, 1000, 1000])
    d.text((668, 924), "HOW SURE", font=f(FB, 13), fill=INK)
    yy = 946
    for lab, color, desc in HOW_SURE:
        d.rounded_rectangle([668, yy, 756, yy + 12], radius=6, fill=color)
        d.text((674, yy + 1), lab, font=f(FB, 8), fill=WHITE)
        d.text((766, yy), desc, font=f(FR, 11), fill=(71, 85, 105))
        yy += 14
    return img


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    draw().save(dst, format="PNG", optimize=True)
    size = os.path.getsize(dst)
    assert size <= 1024 * 1024, f"entry.png too large: {size}"
    print("wrote", dst, size, "bytes")


if __name__ == "__main__":
    main()
