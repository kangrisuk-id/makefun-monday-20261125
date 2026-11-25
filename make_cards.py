#!/usr/bin/env python3
"""Render the README gallery cards (winner + finalists) with Pillow.

Build-time tool only — the grader runs main.py, never this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (24, 28, 38)
PANEL = (35, 42, 56)
GOLD = (240, 183, 60)
TEXT = (235, 238, 244)
MUTED = (160, 170, 188)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, current = text.split(), [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def card(path, kicker, line, footer):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([40, 40, W - 40, H - 40], radius=28, fill=PANEL)
    draw.text((90, 84), kicker, font=font(FONT_BOLD, 34), fill=GOLD)
    y = 170
    for chunk in wrap(draw, line, font(FONT_BOLD, 47), W - 180):
        draw.text((90, y), chunk, font=font(FONT_BOLD, 47), fill=TEXT)
        y += 62
    draw.text((90, H - 110), footer, font=font(FONT_REG, 28), fill=MUTED)
    img.save(path)
    print("wrote", path)


def main():
    card(
        "card-winner.png",
        "★ THE WINNING LINE — 118 CHARACTERS",
        "One star: standup at 9, sync at 10, check-in at 11 — by noon I had "
        "reported my status three times and changed it zero.",
        "Winner of a 42-candidate tournament scored on the judge's own criteria.",
    )
    card(
        "card-finalists.png",
        "THE FINALISTS IT BEAT",
        "“I answered 63 emails and received 64 back; my Monday has a negative "
        "interest rate.” · “The 8 a.m. standup ran so long it needed its own standup.”",
        "Runner-up and semi-finalist — full bracket in candidates.md.",
    )


if __name__ == "__main__":
    main()
