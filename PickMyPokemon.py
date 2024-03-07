import random

# This code was authored by: Kyle Shanahan
# The following python script prompts the user four questions and then determines their pokemon pick.

def choose_pokemon(color, food, size, personality):
    # Dictionary mapping possible answers to Pokémon
    pokemon_choices = {
        ("red", "blue", "yellow"): ["Charmander", "Squirtle", "Bulbasaur"],
        ("pizza", "burger", "pasta"): ["Pikachu", "Jigglypuff", "Snorlax"],
        ("big", "large", "huge"): ["Onix", "Dragonite", "Snorlax"],
        ("pretty", "cute", "adorable"): ["Eevee", "Jigglypuff", "Vulpix"],
        ("fierce", "strong", "powerful"): ["Charizard", "Machamp", "Gyarados"]
    }

    # Match user's answers to possible Pokémon
    possible_pokemon = pokemon_choices.get((color.lower(), food.lower(), size.lower(), personality.lower()))

    # If there's a match, choose a random Pokémon from the possible choices
    if possible_pokemon:
        return random.choice(possible_pokemon)
    else:
        return "Sorry, couldn't find a Pokémon matching your answers."

def main():
    print("Welcome to the Pokémon selector!")
    color = input("What is your favorite color? ")
    food = input("What is your favorite food? ")
    size = input("Do you prefer big or small things? ")
    personality = input("Do you consider yourself more pretty or fierce? ")

    # Output the chosen Pokémon
    pokemon = choose_pokemon(color, food, size, personality)
    print("Based on your answers, your Pokémon is:", pokemon)

if __name__ == "__main__":
    main()
