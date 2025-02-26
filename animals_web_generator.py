import json

with open("animals_template.html", "r") as file:
    template_content = file.read()


with open("animals_data.json", "r") as file:
    animals_data = json.load(file)

animals_output = ""
for animal in animals_data:
    name = animal['name']
    diet = animal['characteristics']['diet']
    location = animal['locations'][0]
    type_ = animal['characteristics'].get('type')

    animals_output += '<li class="cards__item">'
    animals_output += f"{name}<br/>"
    animals_output += f"Diet: {diet}<br/>"
    animals_output += f"Location: {location}<br/>"
    if type_:
        animals_output += f"Type: {type_}<br/>"
    animals_output += "</li>\n"

updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

with open("animals.html", "w") as file:
    file.write(updated_html_content)

print("animals.html has been created successfully.")