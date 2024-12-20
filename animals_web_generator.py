import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """ Serializes a single animal object to HTML """
    output = '    <li class="cards__item">\n'

    if 'name' in animal:
        output += f"        <div class=\"card__title\">{animal['name']}</div>\n"

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output += f"        Diet: {animal['characteristics']['diet']}<br/>\n"

    if 'locations' in animal and animal['locations']:
        output += f"        Location: {animal['locations'][0]}<br/>\n"

    if 'type' in animal:
        output += f"        Type: {animal['type']}<br/>\n"

    output += '    </li>\n'
    return output


# Load the data using your function
animals_data = load_data('animals_data.json')

output = '<ul class="cards">\n'  # Start der Karten-Liste

# Iterate through the animals
for animal in animals_data:
    output += serialize_animal(animal)

output += '</ul>'  # Ende der Karten-Liste

print(output)
