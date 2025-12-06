import os
from bs4 import BeautifulSoup

def remove_wine_notes(docs_dir):
    print(f"Scanning {docs_dir} for 365WineTrade Notes...")
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                # Find all wine-callout divs
                notes = soup.find_all('div', class_='wine-callout')
                
                if notes:
                    print(f"Removing {len(notes)} note(s) from {file}")
                    for note in notes:
                        note.decompose()
                        
                    # Save changes
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                else:
                    # print(f"No notes found in {file}")
                    pass

if __name__ == "__main__":
    docs_dir = "docs"
    remove_wine_notes(docs_dir)
    print("\nDone removing notes.")
