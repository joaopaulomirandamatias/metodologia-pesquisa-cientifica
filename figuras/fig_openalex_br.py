#!/usr/bin/env python3
"""Figura por API aberta: artigos com autoria de instituição brasileira por ano (OpenAlex)."""
import json, urllib.request
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
url = ("https://api.openalex.org/works?filter=authorships.institutions.country_code:BR,"
       "publication_year:2015-2025,type:article&group_by=publication_year&mailto=SEU@EMAIL")
d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "fig (mailto:SEU@EMAIL)"})))
rows = sorted((int(g["key"]), g["count"]) for g in d["group_by"]); print(rows)
fig, ax = plt.subplots(figsize=(7.2, 3.1)); ax.bar([y for y, _ in rows], [n/1000 for _, n in rows])
ax.set_ylabel("artigos (milhares)"); fig.savefig("fig_openalex_br.svg")
