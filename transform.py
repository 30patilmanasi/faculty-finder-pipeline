import json

def transform_data(input_file='faculty_data.json'):
    """
    Transformation: Extracts entities and handles null values.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return []

    cleaned_list = []
    for item in raw_data:
        # Separate the "Bio" and "Specialization" sections as required
        bio = item.get('biography', '').strip()
        spec = item.get('specialization', '').strip()
        
        # Data Management: Handle "null" values and HTML noise
        transformed_item = {
            'name': item.get('name').strip() if item.get('name') else None,
            'education': item.get('education').strip() if item.get('education') else None,
            'email': item.get('email').strip() if item.get('email') else None,
            'phone': item.get('phone').strip() if item.get('phone') else None,
            'address': item.get('address').strip() if item.get('address') else None,
            'profile_url': item.get('profile_url'),
            # Requirements: Bio and Spec get specific 'not available' text if missing
            'biography': bio if bio else "Data is not available",
            'specialization': spec if spec else "Data is not available"
        }
        cleaned_list.append(transformed_item)
        
    return cleaned_list