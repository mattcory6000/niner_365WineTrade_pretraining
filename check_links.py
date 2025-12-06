import os
import re
import urllib.request
from urllib.parse import urlparse, urljoin
from pathlib import Path
import concurrent.futures

DOCS_DIR = os.path.abspath("docs")

def get_html_files(directory):
    return [str(p) for p in Path(directory).rglob("*.html")]

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find href and src attributes
    links = re.findall(r'(?:href|src)=["\'](.*?)["\']', content)
    return links

def check_link(file_path, link):
    # Ignore anchors and mailto
    if link.startswith('#') or link.startswith('mailto:'):
        return None

    # External links
    if link.startswith('http://') or link.startswith('https://'):
        try:
            req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.getcode() >= 400:
                    return f"EXTERNAL ERROR {response.getcode()}: {link} in {os.path.basename(file_path)}"
        except Exception as e:
            return f"EXTERNAL ERROR {e}: {link} in {os.path.basename(file_path)}"
        return None

    # Internal links
    # Handle absolute paths (relative to root, though unlikely in this static site structure)
    if link.startswith('/'):
        # Assuming / refers to docs root for this check, but usually it's relative
        target_path = os.path.join(DOCS_DIR, link.lstrip('/'))
    else:
        # Relative paths
        target_path = os.path.join(os.path.dirname(file_path), link)
    
    # Remove anchor from target path if present
    if '#' in target_path:
        target_path = target_path.split('#')[0]

    if not os.path.exists(target_path):
        return f"INTERNAL ERROR: {link} not found in {os.path.basename(file_path)}"
    
    return None

def main():
    print(f"Scanning {DOCS_DIR}...")
    html_files = get_html_files(DOCS_DIR)
    print(f"Found {len(html_files)} HTML files.")

    errors = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_link = {}
        for file_path in html_files:
            links = extract_links(file_path)
            for link in links:
                future_to_link[executor.submit(check_link, file_path, link)] = link

        for future in concurrent.futures.as_completed(future_to_link):
            result = future.result()
            if result:
                errors.append(result)

    if errors:
        print("\nFound broken links:")
        for error in errors:
            print(error)
    else:
        print("\nNo broken links found!")

if __name__ == "__main__":
    main()
