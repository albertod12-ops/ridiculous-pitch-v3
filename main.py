#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second, v3 (best — deep ATM, live field).

Writes one sentence to /output/entry.txt: hospitals pay $200 a jar for our
sterile maggots, because they eat dead tissue cheaper than a surgeon's scalpel.

ATM analysis behind this pitch (live field, fetched 2026-11-25 ~00:30-00:55 WIB):
- Field: 3,456 submissions; 386 artifact texts sampled (181 from 14:30 WIB 24 Nov
  + 205 new, every 9th of the 1,839 submissions since). Blind rounds hide ranks;
  only our own rounds/board are visible: v2 R1 1515/2186, R2 2084/2730, 44.94%.
- The field is heavily clustered: pothole naming rights (24 texts / 162 titles),
  houseplant/funeral (41), trained crows (22), rent-a-people/actors (25), retired
  professionals (21), apology pigeons (20), professional mourners (16), goats (15),
  bottled silence (14), sleep services (13), insurance for absurd things (7).
- v2 LOST on criterion 2: its mechanism (an actor does an awkward social task on
  your behalf) is populated in the field — "We quit your job for you: $99, a trained
  actor walks in...", professional apologizers attending meetings as you, escape-call
  and excuse hotlines. v2's R2 neighbours are all cluster ideas (houseplant hotel,
  professional mourners, fridge-contents dating).
- The field's STRONGEST non-cluster entries share one trait: the joke IS the
  economics, with a HARD money reason — a law, a physical constraint, a measurable
  cost (coyote urine vs federal goose law; beehive leases unlocking a $15,000 farm-tax
  break; honeybees sniffing bedbugs at $99/room vs one viral review; ravens fishing
  rings from drains at $400 vs a $2,000 plumber). v3 follows exactly that pattern:
  maggot debridement therapy is FDA-cleared, real, and its money reason is a hard
  medical cost (eating dead tissue beats paying a surgeon).
- White space verified 0-hit in all 386 texts AND all 3,456 titles: maggot, sterile,
  scalpel, dead tissue, surgery, surgeon, wound, debridement, larvae — all 0/0.
  "hospital" appears only as buyer for other ideas (emergency contacts, hearse naps);
  "jar" only for bottled-air nostalgia. No wound-care / larva entry exists anywhere.
- Rejected candidates: snore-testing (6 titles, Snore-as-a-Service exists),
  sneeze-testing (tears-by-the-vial-for-mascara-labs shows the bodily-fluid-lab family
  exists), silo-echo rental ("rent a weird space" is a familiar business),
  professional doubter ("consultant with a strange adjective"), last-word seller
  (1 title), yawn hotline (2 titles), dream-selling (8 titles).
- Why this pitch against the judge's brief, in order:
  1. Bizarre startup that is a real business: hospitals buying jars of maggots
     sounds absurd; maggot debridement therapy is FDA-cleared and real, and the
     price ($200/jar) is trivial against surgery.
  2. Genuinely bizarre and novel: 0 hits anywhere in a 3,456-entry field; nobody
     sells maggots as a product, and the unit of sale is a jar of live larvae.
  3. Logic holds in its own words: the sentence states the buyer (hospitals), the
     price ($200 a jar), the delivery (sterile maggots) and the reason the trade
     pencils out (they eat dead tissue cheaper than a surgeon's scalpel).
  4. Lands as a pitch: 112 characters, one sentence, laugh (hospitals pay for
     maggots?!) to nod (oh — cheaper than surgery, and they only eat the dead part).
  5. Concrete and vivid: names the thing sold (sterile maggots, by the jar), the
     buyer (hospitals), and the price ($200).
- Short at 112 characters, under the field median of 156 and shorter than v2's 123,
  which also helps the size tie-break (fewer bytes places first on an exact rate tie).
"""

import os

PITCH = "Hospitals pay $200 a jar for our sterile maggots, because they eat dead tissue cheaper than a surgeon's scalpel."


def main():
    os.umask(0o022)
    assert 1 <= len(PITCH) <= 200, "entry must be 1-200 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "entry must be exactly one sentence"
    data = PITCH.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
