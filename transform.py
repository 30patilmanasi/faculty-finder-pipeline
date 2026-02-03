import json

def transform_data(input_file='faculty_data.json'):
    """
    Transformation: Extracts entities and handles null values for all fields 
    including newly added academic details.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return []

    cleaned_list = []
    for item in raw_data:
        bio = item.get('biography', '').strip()
        spec = item.get('specialization', '').strip()
        
        # This ensures we handle empty lists or messy whitespace from the scraper
        teach = item.get('teaching', '').strip()
        pubs = item.get('publications', '').strip()
        res = item.get('research', '').strip()
        
        # Data Management: Standardizing all fields
        transformed_item = {
            'name': item.get('name').strip() if item.get('name') else None,
            'education': item.get('education').strip() if item.get('education') else None,
            'email': item.get('email').strip() if item.get('email') else None,
            'phone': item.get('phone').strip() if item.get('phone') else None,
            'address': item.get('address').strip() if item.get('address') else None,
            'profile_url': item.get('profile_url'),
            
            # Text Fields with fallback "Not available" messages
            'biography': bio if bio else "Data is not available",
            'specialization': spec if spec else "Data is not available",
            'teaching': teach if teach else "Data is not available",
            'publications': pubs if pubs else "Data is not available",
            'research': res if res else "Data is not available"
        }
        cleaned_list.append(transformed_item)
        
    return cleaned_list