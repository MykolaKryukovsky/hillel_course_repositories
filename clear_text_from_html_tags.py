import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
        with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
        cleaned_text = re.sub(r'<[^>]+>', '', html)
        cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
        with open(result_file, 'w', encoding='utf-8') as file:
            for line in cleaned_lines:
                file.write(line + '\n')

delete_html_tags('draft.html')