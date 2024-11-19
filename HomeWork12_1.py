import re
def delete_html_tags(input_file, output_file='cleaned.txt'):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        cleaned_text = re.sub(r'<[^>]*>', '', html_content)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
        
    except FileNotFoundError:
        print(f"file '{input_file}'not found.")
    except Exception as e:
        print(f"error: {e}")

delete_html_tags('draft.html', 'cleaned.txt')
