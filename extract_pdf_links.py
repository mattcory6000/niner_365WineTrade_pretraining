import pypdf

def extract_links(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    links = []
    for page_num, page in enumerate(reader.pages):
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if "/A" in obj and "/URI" in obj["/A"]:
                    uri = obj["/A"]["/URI"]
                    # Try to get text context if possible, but pypdf doesn't map annots to text easily.
                    # We'll just list the URI and page number for now.
                    # To get text, we might need to extract text and look for the URI or use a more complex method.
                    # However, the user said "The linked text and descriptions should make it easy to understand how they match the links on our website."
                    # Let's try to just get the URI first.
                    links.append({"page": page_num + 1, "uri": uri})
    return links

# Since getting text associated with the link is hard with just pypdf's basic usage,
# let's try to just dump the text of the page and see if we can correlate.
# Or better, just print the URIs and I will manually map them if there aren't too many.
# But the user said "For every Microsoft Learn link in our HTML files, find the corresponding link in this PDF".
# So I need to know what the link IS in the PDF to match it.

if __name__ == "__main__":
    pdf_path = "Microsoft Learn for New Clients copy.pdf"
    try:
        links = extract_links(pdf_path)
        print(f"Found {len(links)} links:")
        for l in links:
            print(f"Page {l['page']}: {l['uri']}")
            
        # Also print full text to help context matching
        print("\n--- PDF TEXT CONTENT ---")
        reader = pypdf.PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            print(f"\n--- Page {i+1} ---")
            print(page.extract_text())
            
    except Exception as e:
        print(f"Error: {e}")
