
import json
from pathlib import Path

# Website root directory.
ROOT = Path(__file__).resolve().parent

PROJECT_FOLDERS = {
    "adani": Path(
        "skids/Adani Power Limited/"
    ),
    "ecologic": Path(
        "skids/Eco Logic/"
    ),
    "mspl": Path(
        "skids/MSPL/"
    ),
    "stringbio": Path(
        "skids/StringBio/"
    ),
    "unithem": Path(
        "skids/Unithem Engineering Goa/"
    ),
}

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"
}

manifest = {}

for project, folder in PROJECT_FOLDERS.items():
    full_folder = ROOT / folder
    images = []

    if full_folder.exists():
        for image in sorted(full_folder.rglob("*")):
            if image.is_file() and image.suffix.lower() in IMAGE_EXTENSIONS:
                # Relative URL from the website root.
                relative_path = image.relative_to(ROOT).as_posix()
                images.append(relative_path)

    manifest[project] = images

    print(f"{project}: {len(images)} images found")

output_file = ROOT / "projects-images.json"

with output_file.open("w", encoding="utf-8") as file:
    json.dump(manifest, file, indent=2, ensure_ascii=False)

print("\nManifest created successfully:")
print(output_file)
