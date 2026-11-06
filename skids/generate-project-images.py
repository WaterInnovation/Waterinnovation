#!/usr/bin/env python3
"""Build projects-images.json for the Water Innovation Systems static site.

Run this script from the website's root folder, where the `skids` folder lives:
    python generate-project-images.py

The generated JSON contains relative paths, so it works on GitHub Pages and
ordinary static hosting (including Globehost). Re-run after adding/removing photos.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
PROJECT_FOLDERS = {
    "adani": Path("skids/Adani Power Limited/"),
    "ecologic": Path("skids/Eco Logic/"),
    "mspl": Path("skids/MSPL/"),
    "stringbio": Path("skids/StringBio/"),
    "unithem": Path("skids/Unithem Engineering Goa/"),
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}

manifest = {}
for project_id, relative_folder in PROJECT_FOLDERS.items():
    folder = ROOT / relative_folder
    if folder.is_dir():
        files = sorted(
            (p.relative_to(ROOT).as_posix() for p in folder.rglob("*")
             if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS),
            key=str.casefold,
        )
    else:
        print(f"WARNING: folder not found: {relative_folder.as_posix()}")
        files = []
    manifest[project_id] = files
    print(f"{project_id}: {len(files)} image(s)")

output = ROOT / "projects-images.json"
output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"\nCreated: {output}")
