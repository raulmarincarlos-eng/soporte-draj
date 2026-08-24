import re
with open('spline_page.html', encoding='utf-16le') as f:
    content = f.read()
match = re.search(r'https://[^\"\'\s>]+\.splinecode', content)
if match:
    print(match.group(0))
else:
    print("NOT FOUND")
