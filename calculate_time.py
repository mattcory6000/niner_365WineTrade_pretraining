import os
from bs4 import BeautifulSoup
import re

def parse_duration(duration_str):
    """Parses a duration string like '1 hour 30 minutes' into total minutes."""
    total_minutes = 0
    
    # Extract hours
    hours_match = re.search(r'(\d+)\s+hour', duration_str)
    if hours_match:
        total_minutes += int(hours_match.group(1)) * 60
        
    # Extract minutes
    minutes_match = re.search(r'(\d+)\s+minute', duration_str)
    if minutes_match:
        total_minutes += int(minutes_match.group(1))
        
    return total_minutes

def format_duration(total_minutes):
    """Formats total minutes into 'X hours Y minutes'."""
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        
    if not parts:
        return "0 minutes"
        
    return " ".join(parts)

def calculate_group_time(docs_dir, filenames):
    total_minutes = 0
    print(f"Processing group: {filenames}")
    
    for filename in filenames:
        filepath = os.path.join(docs_dir, filename)
        if not os.path.exists(filepath):
            print(f"WARNING: File not found: {filename}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        # Find all clock icons
        clock_icons = soup.find_all('i', class_='bi-clock')
        
        for icon in clock_icons:
            # The time is in the next sibling span
            time_span = icon.find_next_sibling('span')
            if time_span:
                duration_str = time_span.get_text().strip()
                minutes = parse_duration(duration_str)
                # print(f"  {filename}: Found '{duration_str}' -> {minutes} min")
                total_minutes += minutes
                
    return total_minutes

if __name__ == "__main__":
    docs_dir = "docs"
    
    rounds_files = [
        "round1-getting-started.html",
        "round2-core-skills.html",
        "round3-foundational.html"
    ]
    
    roles_files = [
        "role-admin.html",
        "role-finance.html",
        "role-trade.html",
        "role-warehouse.html",
        "role-powerbi.html"
    ]
    
    print("--- Calculating Times ---\n")
    
    rounds_minutes = calculate_group_time(docs_dir, rounds_files)
    print(f"\nTotal time for Rounds I, II, and III: {format_duration(rounds_minutes)} ({rounds_minutes} mins)")
    
    print("-" * 30)
    
    roles_minutes = calculate_group_time(docs_dir, roles_files)
    print(f"\nTotal time for all remaining modules: {format_duration(roles_minutes)} ({roles_minutes} mins)")
