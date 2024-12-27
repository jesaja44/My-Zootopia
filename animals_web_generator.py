import json
import os


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


def generate_html(animals_data):
    """ Generate HTML content from animal data """
    output = '<ul class="cards">\n'
    for animal in animals_data:
        output += serialize_animal(animal)
    output += '</ul>'
    return output


def replace_template_content(template_path, new_content, output_path):
    """ Replace __REPLACE_ANIMALS_INFO__ in template with new content """
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    updated_content = template_content.replace('__REPLACE_ANIMALS_INFO__', new_content)

    with open(output_path, 'w') as output_file:
        output_file.write(updated_content)


def clone_repository():
    """ Clone the GitHub repository """
    import subprocess

    # Replace with your actual repository URL
    repo_url = "https://github.com/jesaja44/My-Zootopia.git"

    try:
        # Remove existing directory if it exists
        if os.path.exists("My-Zootopia"):
            subprocess.run(["rm", "-rf", "My-Zootopia"], check=True)

        # Clone the repository
        subprocess.run(["git", "clone", repo_url], check=True)
        print("Repository successfully cloned!")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")


def main():
    # Step 1: Clone the repository
    clone_repository()

    # Step 2: Load animal data
    animals_data = load_data('animals_data.json')

    # Step 3: Generate HTML content
    html_content = generate_html(animals_data)

    # Step 4: Replace template content and create new HTML file
    replace_template_content(
        'animals_template.html',
        html_content,
        'generated_animals.html'
    )

    print("HTML generation complete!")


# Ensure the script is run directly
if __name__ == "__main__":
    main()