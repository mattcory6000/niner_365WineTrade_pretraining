import pypdf
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

# --- 1. Extract Links and Titles from PDF ---
def extract_pdf_map(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    links = []
    
    for page in reader.pages:
        # Get text for titles
        text = page.extract_text()
        lines = text.split('\n')
        
        # Get annotations for full URIs
        page_uris = []
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if "/A" in obj and "/URI" in obj["/A"]:
                    page_uris.append(obj["/A"]["/URI"])
        
        # Heuristic: Match text lines that look like URLs to the list of URIs
        # We assume they appear in the same order.
        uri_index = 0
        
        for i, line in enumerate(lines):
            if "learn.microsoft.com" in line:
                # This line is a visible URL (possibly truncated)
                # The title is likely the previous line
                if i > 0:
                    title = lines[i-1].strip()
                    if title.endswith("..."):
                        title = title[:-3]
                    
                    # Get the corresponding full URI
                    if uri_index < len(page_uris):
                        full_uri = page_uris[uri_index]
                        uri_index += 1
                        
                        # Normalize
                        parsed = urlparse(full_uri)
                        clean_url = urlunparse(parsed._replace(query="", fragment="")).rstrip('/')
                        
                        links.append({'title': title, 'url': clean_url, 'original_url': full_uri})
                    else:
                        print(f"WARNING: More text links than annotations on page? Text: {line}")
                        
    return links

# --- 2. Process HTML Files ---
def process_html_files(docs_dir, pdf_links):
    # Manual mapping for tricky titles (HTML Title -> PDF URL Part or Title Part)
    manual_map = {
        "Bin Setup and Management": "configure-bins-location",
        "Inventory Adjustments and Counts": "adjust-inventory",
        "Sales Order Processing": "create-sales-documents", 
        "Purchase Order Processing": "create-purchase-documents", 
        "Outlook Integration for Business Central": "email-integration",
        "User Management and Security": "users-security",
        "Data Analysis and List Views": "analyze-list-data",
        "Email Integration and Document Sending": "set-up-email",
        "Warehouse Management Fundamentals": "get-started-warehouse-management",
        "Trade Master Data": "trade-master-data",
        "Sales Quotes and Orders": "create-sales-documents",
        "Purchase Quotes and Orders": "create-purchase-documents",
        "Receiving and Invoicing": "receive-invoice",
        "Sales Prices and Discounts": "sales-price-lists",
        "Item Management": "create-items",
        "General Journal Templates": "general-journal-templates",
        "Chart of Accounts": "chart-accounts",
        "Dimensions": "dimensions",
        "Posting Groups": "posting-groups",
        "Bank Reconciliation": "bank-reconciliation",
        "Cash Receipts and Payments": "enter-payments",
        "General Ledger Allocations": "general-ledger-allocations",
        "Power BI Basics": "get-started-with-power-bi",
        "View Reports": "end-user-report-open",
        "Payment Processing and Application": "enter-payments",
        "General Journal Setup and Configuration": "general-journal-templates"
    }

    unused_pdf_links = {l['url'] for l in pdf_links}
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                modified = False
                
                # Find all learn.microsoft.com links
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if "learn.microsoft.com" in href:
                        
                        # Normalize href for comparison
                        parsed_href = urlparse(href)
                        clean_href = urlunparse(parsed_href._replace(query="", fragment="")).rstrip('/')
                        
                        # 1. Styling
                        classes = a.get('class', [])
                        if 'btn' not in classes:
                            classes.append('btn')
                        if 'btn-sm' not in classes:
                            classes.append('btn-sm')
                        if 'btn-primary' not in classes:
                            classes.append('btn-primary')
                        a['class'] = classes
                        modified = True
                        
                        # 2. Fix Generic, Truncated, OR Incorrect Specific Links
                        # We want to ensure the link matches the PDF if possible.
                        
                        # Check if current link is in PDF (normalized)
                        is_in_pdf = False
                        for pdf_link in pdf_links:
                            if pdf_link['url'] == clean_href:
                                is_in_pdf = True
                                break
                        
                        # If it's generic, truncated, OR not in the PDF, try to find a match
                        is_truncated = href.endswith("...") or href.endswith("…") or href.endswith("…/")
                        is_generic = "browse/?products" in href or "training/browse" in href
                        
                        if is_generic or is_truncated or not is_in_pdf:
                            # Try to find context
                            # Look for parent module-card
                            card = a.find_parent(class_='module-card')
                            if card:
                                h3 = card.find('h3')
                                if h3:
                                    context_title = h3.get_text().strip()
                                    
                                    # Try Manual Map first
                                    best_match = None
                                    for key, val in manual_map.items():
                                        if key in context_title: # Loose match
                                            # Find the PDF link that contains this value
                                            for link in pdf_links:
                                                if val in link['url']:
                                                    best_match = link
                                                    break
                                        if best_match: break
                                    
                                    # If no manual match, try fuzzy match
                                    if not best_match:
                                        highest_score = 0
                                        for link in pdf_links:
                                            # Simple word overlap
                                            pdf_words = set(re.findall(r'\w+', link['title'].lower()))
                                            html_words = set(re.findall(r'\w+', context_title.lower()))
                                            # Remove common words
                                            stop_words = {'and', 'in', 'for', 'the', 'to', 'of', 'business', 'central', 'dynamics', '365'}
                                            pdf_words -= stop_words
                                            html_words -= stop_words
                                            
                                            overlap = len(pdf_words.intersection(html_words))
                                            if overlap > highest_score:
                                                highest_score = overlap
                                                best_match = link
                                        
                                        if highest_score < 2: # Strict threshold (2 words)
                                            best_match = None

                                    if best_match:
                                        # Only replace if it's different
                                        if best_match['original_url'] != href:
                                            print(f"Replacing link in {file} for '{context_title}'\n   Old: {href}\n   New: {best_match['original_url']}")
                                            a['href'] = best_match['original_url']
                                            modified = True
                                            if best_match['url'] in unused_pdf_links:
                                                unused_pdf_links.remove(best_match['url'])
                                    else:
                                        if is_generic or is_truncated:
                                            print(f"WARNING: Could not find match for '{context_title}' in {file}")
                            else:
                                if is_generic or is_truncated:
                                    print(f"WARNING: Generic/Broken link found outside module-card in {file}: {href}")
                        else:
                            # It is in PDF, mark as used
                            if clean_href in unused_pdf_links:
                                unused_pdf_links.remove(clean_href)

                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup))

    print("\n--- Unused PDF Links ---")
    for url in unused_pdf_links:
        title = next((l['title'] for l in pdf_links if l['url'] == url), "Unknown")
        print(f"{title}: {url}")

if __name__ == "__main__":
    pdf_path = "Microsoft Learn for New Clients copy.pdf"
    docs_dir = "docs"
    
    print("Extracting PDF links...")
    pdf_links = extract_pdf_map(pdf_path)
    print(f"Found {len(pdf_links)} links in PDF.")
    
    print("Processing HTML files...")
    process_html_files(docs_dir, pdf_links)
