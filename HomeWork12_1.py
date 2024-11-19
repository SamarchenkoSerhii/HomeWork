import codecs 
def delete_html_tags(html_file, result_file='cleaned.txt'): 
      with codecs.open(html_file, 'r', 'utf-8') as file: 
           html = file.read()
