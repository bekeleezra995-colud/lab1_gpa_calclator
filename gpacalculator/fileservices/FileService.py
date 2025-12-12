import os
# from .exceptions import PersistenceError, FileCorruptionError # Removed

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def ensure_data_dir():
    """Ensures the data directory exists."""
    if not os.path.exists(DATA_DIR):
        try:
            os.makedirs(DATA_DIR)
        except OSError as e:
            # Re-raise with context
            raise OSError(f"Failed to create data directory: {e}")

def read_table(filename):
    """Reads a Markdown-style table file and returns a list of dictionaries."""
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)
    data = []
    
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            lines = f.readlines()
            
        if not lines:
            return []
            
        # Parse Headers
        header_line = lines[0].strip()
        if not header_line.startswith('|'):
            raise ValueError(f"Invalid table format in {filename}: Header missing or malformed.")
        
        raw_headers = header_line.split('|')
        headers = [h.strip() for h in raw_headers if h.strip()]
        
        if not headers:
            return [] # Empty table?

        # Parse Data
        start_index = 1
        if len(lines) > 1 and set(lines[1].strip()) <= {'|', '-', ' '}:
                start_index = 2

        for line_num, line in enumerate(lines[start_index:], start=start_index+1):
            line = line.strip()
            if not line or not line.startswith('|'):
                continue
            
            raw_values = line.split('|')
            values = []
            for v in raw_values:
                values.append(v.strip())
            
            if len(values) >= 2 and values[0] == "" and values[-1] == "":
                    values = values[1:-1]
            
            row = {}
            for i, h in enumerate(headers):
                val = values[i] if i < len(values) else ""
                row[h] = val
            data.append(row)
                
    except OSError as e:
        raise OSError(f"Error reading file {filename}: {e}")
    except ValueError as e:
        raise ValueError(f"Data corruption in {filename}: {e}")
    except Exception as e:
        raise OSError(f"Unexpected error reading {filename}: {e}")
         
    return data

def write_table(filename, data, fieldnames):
    """Writes a list of dictionaries to a Markdown-style table file."""
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)
    
    if not fieldnames:
        return 

    # Calculate column widths
    widths = {f: len(f) for f in fieldnames}
    for row in data:
        for f in fieldnames:
            val = str(row.get(f, ''))
            widths[f] = max(widths[f], len(val))
    
    # Add padding
    final_widths = {f: widths[f] + 2 for f in fieldnames}
    
    try:
        with open(filepath, mode='w', encoding='utf-8') as f:
            # Header
            header_parts = []
            for fld in fieldnames:
                cell_text = f" {fld} "
                header_parts.append(cell_text.ljust(final_widths[fld]))
            
            f.write("|" + "|".join(header_parts) + "|\n")
            
            # Separator
            sep_parts = []
            for fld in fieldnames:
                sep_parts.append("-" * final_widths[fld])
            f.write("|" + "|".join(sep_parts) + "|\n")
            
            # Data
            for row in data:
                row_parts = []
                for fld in fieldnames:
                    val = str(row.get(fld, ''))
                    cell_text = f" {val} "
                    row_parts.append(cell_text.ljust(final_widths[fld]))
                f.write("|" + "|".join(row_parts) + "|\n")
    except OSError as e:
        raise OSError(f"Error writing to file {filename}: {e}")

# Alias for compatibility if needed, but we will update calls
read_csv = read_table
write_csv = write_table
