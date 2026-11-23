# The World in One Day — Monday, 23 November 2026

Entry for make.fun's "Sum up 23 November's world news in one image"
bounty ($100, top 50 share it). A newspaper front page drawn entirely
with code (Pillow, no photos, no network).

## The six stories

- **Lead — COP31 collapses, Antalya:** UN climate talks ended Sunday with
  no agreement — the longest COP on record. The draft Antalya Pact never
  mentioned fossil fuels. Next try: COP32 in Addis Ababa, Nov 2027.
- **Strait of Hormuz:** at least three tankers struck Fri–Sat; two more
  on fire Sunday after hitting naval mines.
- **Dymer, north of Kyiv:** a Russian drone hit a five-storey apartment
  block — 2 killed, 11 missing, including two children.
- **Benghazi:** suspected Ukrainian sea drones hit the Russian corvette
  Merkury at the naval base.
- **Cikande, Banten:** a candy factory fire — dozens still missing;
  search resumes Monday. (No death toll is printed: sources disagree and
  police say it is unconfirmed.)
- **Mercury:** BepiColombo entered orbit around Mercury — only the second
  mission ever to do so.

## Files

- `draw.py` — the Pillow generator (stdlib + Pillow only, deterministic).
- `entry.png` — the 1024×1024 image it writes.
- `main.ts` — the entry program: copies `entry.png` to `/output/entry.png`
  after checking its PNG magic.

## Run

```sh
python3 draw.py            # regenerates entry.png (byte-identical)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Sources: Reuters, AP, CNN, Al Jazeera, BBC.
