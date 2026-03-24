#!/usr/bin/env python3
"""Build the personal website by rendering cv-data.yaml into the HTML template."""
import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent

    with open(root / "cv-data.yaml") as f:
        data = yaml.safe_load(f)

    env = Environment(loader=FileSystemLoader(root / "site-template"))
    template = env.get_template("index.html.j2")

    output_dir = root / "build"
    output_dir.mkdir(exist_ok=True)

    rendered = template.render(**data)
    (output_dir / "index.html").write_text(rendered)
    print(f"Rendered index.html ({len(rendered)} bytes) -> {output_dir / 'index.html'}")


if __name__ == "__main__":
    main()
