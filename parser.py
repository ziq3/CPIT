import os
import re
import cloudscraper

def make_file(filename: str, content: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def parse_problem(LINK, path=None, input_ext=".in") -> None:
    # Ensure LINK has a valid scheme
    if not (LINK.startswith("http://") or LINK.startswith("https://")):
        LINK = "https://" + LINK
    if path is None:
        # use current working directory
        path = os.getcwd() + os.sep
    try:
        # Extract name from URL (currently unused)
        name = ""
        for i in range(len(LINK)-1, -1, -1):
            if LINK[i] == '/':
                break
            name += LINK[i]
        # Use cloudscraper to bypass potential Cloudflare blocks
        scraper = cloudscraper.create_scraper()
        f = scraper.get(LINK)
        all_starts = [m.start() for m in re.finditer("<pre>", f.text)]
        all_ends = [m.start() for m in re.finditer("</pre>", f.text)]
        # ...rest of the code...
    except Exception as e:
        print(e)
