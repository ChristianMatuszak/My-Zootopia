import json

try:
    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_content = file.read()
except FileNotFoundError:
    print("Error: The template file 'animals_template.html' was not found.")
    exit(1)
except Exception as e:
    print(f"Error reading template file: {e}")
    exit(1)

try:
    with open("animals.json", "r", encoding="utf-8") as file:
        animals_data = json.load(file)
except FileNotFoundError:
    print("Error: The data file 'animals.json' was not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please check the format of 'animals.json'.")
    exit(1)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)


def serialize_animal(animal):
    """Serialize a single animal into an HTML list item with separate fields."""
    name = animal['name']
    diet = animal['characteristics']['diet']
    location = animal['locations'][0]
    type_ = animal['characteristics'].get('type')
    lifespan = animal['characteristics'].get('lifespan')
    color = animal['characteristics'].get('color')
    scientific_name = animal['taxonomy'].get('scientific_name')

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <br/>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="animal-details">\n'
    output += f'      <li class="animal-detail"><strong>Diet:</strong> {diet}</li>\n'
    output += f'      <li class="animal-detail"><strong>Location:</strong> {location}</li>\n'
    if type_:
        output += f'      <li class="animal-detail"><strong>Type:</strong> {type_}</li>\n'
    if lifespan:
        output += f'      <li class="animal-detail"><strong>Lifespan:</strong> {lifespan}</li>\n'
    if color:
        output += f'      <li class="animal-detail"><strong>Color:</strong> {color}</li>\n'
    if scientific_name:
        output += f'      <li class="animal-detail"><strong>Scientific Name:</strong> {scientific_name}</li>\n'
    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'

    return output

def main():

    animals_output = ""
    for animal in animals_data:
        animals_output += serialize_animal(animal)

    updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    try:
        with open("animals.html", "w", encoding="utf-8") as file:
            file.write(updated_html_content)
        print("animals.html has been created successfully.")
    except Exception as e:
        print(f"Error writing to 'animals.html': {e}")
        exit(1)


if __name__ == "__main__":
    main()