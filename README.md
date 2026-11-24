# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/BokeXe/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/BokeXe/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Tuesday 24 November 2026 in one image — a modern digital news dashboard with
38 date-checked stories across 9 regions and 24 fields: an ink header band with
the date chip, six big-number stat cards, rounded region pills, a UTC timeline,
three flat-vector lead panels (Trump meets Zelenskyy in Washington; Russian
missiles and a drone hit Poland; Houthis strike Riyadh's tallest tower), a
12-card grid with a real Bitcoin area chart (closes $60.2k → $61.3k → $61.3k →
$59.7k, −2.71% on Tuesday), a dotted world map with numbered pins, and a full
numbered story index. Every story is tagged by source and confidence
(confirmed / reported / claimed), and the page carries a DATE CHECK box that
names the four neighbouring days' items reported on 24 November, so nothing
from 22–23 November is presented as 24 November's news.

`main.py` copies `entry.png` (1024×1024, ≤1 MiB) to `/output/entry.png`; both runs
write identical bytes, no network.

## Reproduce

`entry.png` is generated deterministically by `../prep/news24/build.py` (Pillow,
DejaVu/Noto Sans fonts, no clock, no network). Re-running it produces the same
bytes; `main.py` refuses to finish if the copied file's size differs from the
source. The four items flagged in the DATE CHECK box are the only stories on
the page dated before Tuesday 24 November 2026.
