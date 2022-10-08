import json

def find_theme(color, data):
    for i in range(len(data)):
        if color == data[i]["name"]:
            d = data.pop(i)
            return d
    return None

with open('colorschemes.json', 'r') as f:
    orig_data = json.loads(f.read())
with open('colorthemes.txt', 'r') as f:
    color_themes = [line.strip() for line in f]
airline_themes={}
with open('airlinethemes.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('base16_'):
            key = line[7:].lower()
            airline_themes[key] = line

new_data = []
for color in color_themes:
    find_data = find_theme(color, orig_data)
    if find_data is not None:
        # if find_data['airline']:
        new_data.append(find_data)
        if find_data['airline'] in airline_themes:
            # if color.lower() in airline_themes:
            airline_themes.pop(find_data['airline'])
    else:
        item = {'name': color, 'light':1, 'dark':1, 'commandBeforeColo': '', 'airline': ''}
        if 'light' in color.lower():
            item['light'] = 1
            item['dark'] = 0
        if 'dark' in color.lower() or 'night' in color.lower():
            item['light'] = 0
            item['dark'] = 1
        if color.lower() in airline_themes:
            item['airline'] = airline_themes.pop(color.lower())
        new_data.append(item)

with open('colorschemes_new.json', 'w+') as f:
    f.write(json.dumps(new_data, indent=2))

with open('colorschemes_remain.json', 'w+') as f:
    f.write(json.dumps(orig_data, indent=2))

with open('airlinethemes_remain.json', 'w+') as f:
    f.write(json.dumps(airline_themes, indent=2))

