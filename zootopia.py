import json

def load_data(filepath):
    with open(filepath, 'r') as fileobj:
        data = json.load(fileobj)
    return data

def read_data(data):
    for info in data:
        try:
            name, taxonomy, locations, characteristics = info.values()
            print(f"Name: {name}")
            print(f"Diet: {characteristics['diet']}")
            print(f"Location: {locations[0]}")
            print(f"Type: {characteristics['type']}")
        except KeyError as k:
            print("Error - Key not found: ", k)
        print()

        # print(info)
        # print(taxonomy)
        # print(locations)
        # print(characteristics)
    return




def main():
    animals = load_data('animals_data.json')
    read_data(animals)

if __name__ == "__main__":
    main()
