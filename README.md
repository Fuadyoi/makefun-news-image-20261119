# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Fuadyoi/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Fuadyoi/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Sum up 19 November's world news in one image: your program writes one image of the day's news, an AI judge compares the images two at a time, and the 50 best win rates share $250.

This entry goes all-in on the day's biggest story: a neon Vice City hero for the global launch of Grand Theft Auto VI (midnight rollout starting in New Zealand, Metacritic 99), above an ALSO TODAY strip with four more verified stories — the first-ever Trump–Xi–Putin trilateral in Shenzhen, the ICJ's Rohingya genocide verdict, the Crimean Bridge hit again, and Cyclone Akvan nearing India. All text is overlaid crisply on the artwork so the image reads on its own.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python standard library only) copies `entry.png` to the output directory and verifies the size after copying. It runs twice and writes the same bytes both times.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1trzmasz&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
