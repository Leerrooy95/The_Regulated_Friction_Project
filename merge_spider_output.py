#!/usr/bin/env python3
"""
merge_spider_output.py
======================
Merges new spider output with existing historical Federal Register data.

The spider's -o flag appends a new JSON array to the file, creating an
invalid multi-array JSON file. This script:
  1. Reads all JSON arrays from the file
  2. Combines them into a single dataset
  3. Removes duplicates (by Document_Number)
  4. Sorts by date (newest first)
  5. Writes back as a single valid JSON array

Usage:
  python3 merge_spider_output.py <json_file_path>
"""

import json
import sys
from pathlib import Path


def merge_spider_output(file_path: Path) -> None:
    """Merge multiple JSON arrays in a spider output file into one."""
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    # Read the entire file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split by array boundaries - handle various whitespace patterns
    # Try multiple common patterns for robustness
    import re
    # Split on ][ with optional whitespace
    parts = re.split(r'\]\s*\[', content)
    
    all_items = []
    
    for i, part in enumerate(parts):
        # Fix array boundaries
        if i == 0:
            # First part: might already start with [, or needs it
            json_str = part if part.strip().startswith('[') else '[' + part
        else:
            # Middle/end parts: add [ at start
            json_str = '[' + part
        
        # Ensure it ends with ]
        if not json_str.strip().endswith(']'):
            # Simply append ] if missing (after trimming)
            json_str = json_str.rstrip() + ']'
        
        # Parse this array
        try:
            items = json.loads(json_str)
            all_items.extend(items)
            print(f"Loaded array {i+1}: {len(items)} items")
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse array {i+1}: {e}")
            continue
    
    print(f"\nTotal items before deduplication: {len(all_items)}")
    
    # Remove duplicates by Document_Number (keep the first occurrence)
    seen = set()
    unique_items = []
    
    for item in all_items:
        doc_num = item.get("Document_Number")
        if doc_num and doc_num not in seen:
            seen.add(doc_num)
            unique_items.append(item)
    
    print(f"Total items after deduplication: {len(unique_items)}")
    
    # Sort by date (newest first)
    unique_items.sort(key=lambda x: x.get("Date", ""), reverse=True)
    
    # Write back as a single array
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(unique_items, f, indent=4, ensure_ascii=False)
    
    print(f"\n✓ Successfully merged and saved {len(unique_items)} items to {file_path}")
    
    # Print date range
    if unique_items:
        dates = [item.get("Date") for item in unique_items if item.get("Date")]
        if dates:
            print(f"  Date range: {min(dates)} to {max(dates)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 merge_spider_output.py <json_file_path>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    merge_spider_output(file_path)
