import pathlib
from tqdm import tqdm
import os
from bs4 import BeautifulSoup

def strip_social(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find and remove the specific nav element
    social_nav = soup.find('nav', {'id': 'nav-social'})
    if social_nav:
        social_nav.decompose()

    # Write the modified HTML back to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def process_all_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                strip_social(filepath)

def strip_js(filename, bad_lines):
    good_lines = []
    with open(filename, "r") as f:
        for line in f:
            is_bad = sum([bad_line in line for bad_line in bad_lines])
            if not is_bad:
                good_lines.append(line)

    text = "".join(good_lines)
    with open(filename, "w") as f:
        f.write(text)

if __name__ == "__main__":
    # Go through _build/html, and remove all extraneous javascript. This is all
    # very silly, but upgrading sphinx-book-theme's version to reject the bad js
    # is very annoying
    files = pathlib.Path("_build/html").glob("*.html")
    for f in tqdm(files):
        strip_js(f, ["thebe.js"])

    # Remove the social nav from all HTML files
    process_all_html_files("_build/html")
