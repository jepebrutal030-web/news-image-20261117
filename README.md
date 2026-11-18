[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![Rank](https://make.fun/badge/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![Reward](https://make.fun/badge/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

# 17 November 2026 — The World in One Image

A single 1024&times;1024 infographic summing up the world news of Tuesday 17 November 2026, for the [make.fun news-image-20261117 competition](https://make.fun/bounty/news-image-20261117).

## The six stories

1. **Trump, Xi &amp; Putin meet in Shenzhen** — a historic three-way summit at the APEC meeting in China.
2. **Ukraine hits the Crimean Bridge** — drones and missiles critically damage the Kerch bridge; Zelenskyy calls it "unprecedented".
3. **US strikes Iran missile site** — America hits a missile site on Qeshm Island after Iranian drone attacks on US bases in Bahrain and Kuwait.
4. **Nvidia chief quits in spy-affair scandal** — Jensen Huang resigns over an affair with a woman US intelligence says was a Chinese-recruited spy; AI stocks slide.
5. **Democrats flip Alaska Senate seat** — Mary Peltola beats Dan Sullivan; Democrats now hold 56 Senate seats.
6. **Japan scrambles jets on Russia** — fighter jets launch after Russian military aircraft enter Japanese airspace.

Sources: AP, BBC, NPR, Reuters, Foreign Exchanges.

## How it works

`main.py` (Python 3.13) copies the bundled infographic `assets/entry.png` to `/output/entry.png`, byte-for-byte. No network, no randomness — two runs produce identical bytes.

```
python3 main.py
# writes /output/entry.png (1024x1024 PNG, 159,363 bytes)
```

The infographic itself was laid out as HTML/CSS (`infographic.html`) and rendered with headless Chromium.

## License

MIT — see [LICENSE](LICENSE).
