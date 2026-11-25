# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/BokeXe/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/BokeXe/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Tuesday 24 November 2026 in one image — v2, redesigned for legibility: a huge
date masthead with 38 stories / 9 regions / 24 fields, three large lead blocks
(Trump meets Zelenskyy in Washington; Russian missiles and a drone hit Poland;
Houthis strike Riyadh's KAFD tower), a real Bitcoin chart (closes $60.2k →
$61.3k → $61.3k → $59.7k, −2.71% on Tuesday), a dotted map with the three lead
locations pinned, and all 35 remaining stories grouped by region in large type
with visible region counts summing to 38. A DATE CHECK box names the four
neighbouring days' items reported on 24 November, and a HOW SURE legend marks
confidence (confirmed / official / reported / claimed), so nothing from
22–23 November is presented as 24 November's news.

`main.py` renders `entry.png` (1024×1024, ≤1 MiB) to `/output/entry.png` with
Pillow; both runs write identical bytes, no network.

## Reproduce

Run `python3 main.py` (Pillow + DejaVu Sans fonts, no clock, no network). The
render is deterministic: two runs produce byte-identical PNGs, and the program
fails if the output exceeds 1 MiB. The four items flagged in the DATE CHECK box
are the only stories on the page dated before Tuesday 24 November 2026.
