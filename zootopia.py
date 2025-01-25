import json

'''
Read animal info data from animals_data.json
Create string with animal info
Add string to animals_template.html
'''

def load_data(filepath):
    '''
    Loads the data from animals_data.json
    Returns data as list of dictionaries
    '''
    try:
        with open(filepath, 'r') as fileobj:
            data = json.load(fileobj)
        return data
    except FileNotFoundError as f:
        print(f"Error (File not found): {f}")


def read_animal_info(data):
    '''
    Read the animal info from animals_data.json
    Returns a string animal_infos
    '''
    animal_info = ""
    for info in data:
        try:
            name, taxonomy, locations, characteristics = info.values()
            animal_info += f"\n"
            animal_info += f'<li class="cards__item">\n'
            animal_info += f'<div class="card__title">{name}</div>\n'
            animal_info += f'<p class="card__text">\n'
            animal_info += f'<strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
            animal_info += f'<strong>Location:</strong> {locations[0]}<br/>\n'
            animal_info += f'<strong>Type:</strong>{characteristics["type"]}l<br/>\n'
            animal_info += f'</p>\n'
            animal_info += "</li>\n"
        except KeyError as k:
            animal_info += f'</p>\n'
            animal_info += "</li>\n"
            continue
    return animal_info

def read_template(path):
    '''  Reads and Returns the text html animals_template.html. '''
    try:
        with open(path, 'r') as fileobj:
            template = fileobj.read()
        return template
    except FileNotFoundError as f:
        print(f"Error (File not found: {f}")
        return

def animals_data_html(to_replace, template, animal_info):
    '''  '''
    try:
        content_1 = template[: template.find(to_replace)]
        content_2 = template[template.find(to_replace) + len(to_replace) :]
        html_string = content_1 + animal_info + content_2
        return html_string
    except IndexError as i:
        print(f"Error (Indexing): {i}")
        return

def write_html_content(new_path, content):
    ''' '''
    try:
        with open(new_path, 'w') as fileobj:
            fileobj.write(content)
            return f"Content was successfully added to html file ({new_path}). "
    except FileNotFoundError as f:
        print(f"Error (File not found): ", f)
        return



def main():

    new_files_name = 'animals.html'

    ''' Relevant paths and text to be replaced: '''
    path_animal_data = 'animals_data.json'
    template_path = 'animals_template.html'

    ''' Load necessary data. '''
    data = load_data(path_animal_data)
    html_template = read_template(template_path)
    animal_info = read_animal_info(data)

    ''' Generate Result Text and write into html-file. '''
    new_html = animals_data_html('__REPLACE_ANIMALS_INFO__', html_template, animal_info)
    write_html_content(new_files_name, new_html)


if __name__ == "__main__":
    main()
