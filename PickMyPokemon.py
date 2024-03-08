import random

# This code was authored by: Kyle Shanahan
# The following python script prompts the user four questions and then determines their pokemon pick.
# There are four questions asked to the user:
# 1) What is your favorite color? 
# 2) What is your favorite food?
# 3) Do you prefer big or small things?
# 4) Do you consider yourself more pretty or fierce? 

def choose_pokemon(color, food, size, personality):
    # Dictionary mapping possible answers to Pokémon
    pokemon_choices = {
    pokemon_choices = {
        ("green", "leaves", "small", "pretty"): ["Bulbasaur", "Caterpie", "Weedle"],
        ("green", "leaves", "small", "fierce"): ["Bulbasaur", "Caterpie", "Weedle"],
        ("green", "leaves", "big", "pretty"): ["Venusaur", "Butterfree", "Beedrill"],
        ("green", "leaves", "big", "fierce"): ["Venusaur", "Butterfree", "Beedrill"],
        ("red", "fire", "small", "pretty"): ["Charmander", "Vulpix", "Growlithe"],
        ("red", "fire", "small", "fierce"): ["Charmander", "Vulpix", "Growlithe"],
        ("red", "fire", "big", "pretty"): ["Charizard", "Arcanine", "Rapidash"],
        ("red", "fire", "big", "fierce"): ["Charizard", "Arcanine", "Rapidash"],
        ("blue", "water", "small", "pretty"): ["Squirtle", "Poliwag", "Psyduck"],
        ("blue", "water", "small", "fierce"): ["Squirtle", "Poliwag", "Psyduck"],
        ("blue", "water", "big", "pretty"): ["Blastoise", "Poliwhirl", "Slowpoke"],
        ("blue", "water", "big", "fierce"): ["Blastoise", "Poliwhirl", "Slowpoke"],
        ("purple", "flowers", "small", "pretty"): ["Oddish", "Bellsprout", "Paras"],
        ("purple", "flowers", "small", "fierce"): ["Oddish", "Bellsprout", "Paras"],
        ("purple", "flowers", "big", "pretty"): ["Vileplume", "Victreebel", "Gloom"],
        ("purple", "flowers", "big", "fierce"): ["Vileplume", "Victreebel", "Gloom"],
        ("yellow", "sweet", "small", "pretty"): ["Pikachu", "Jigglypuff", "Clefairy"],
        ("yellow", "sweet", "small", "fierce"): ["Pikachu", "Jigglypuff", "Clefairy"],
        ("yellow", "sweet", "big", "pretty"): ["Raichu", "Clefable", "Wigglytuff"],
        ("yellow", "sweet", "big", "fierce"): ["Raichu", "Clefable", "Wigglytuff"],
        ("grey", "rock", "small", "pretty"): ["Geodude", "Onix", "Rhyhorn"],
        ("grey", "rock", "small", "fierce"): ["Geodude", "Onix", "Rhyhorn"],
        ("grey", "rock", "big", "pretty"): ["Graveler", "Golem", "Rhydon"],
        ("grey", "rock", "big", "fierce"): ["Graveler", "Golem", "Rhydon"],
        ("brown", "earth", "small", "pretty"): ["Diglett", "Sandshrew", "Cubone"],
        ("brown", "earth", "small", "fierce"): ["Diglett", "Sandshrew", "Cubone"],
        ("brown", "earth", "big", "pretty"): ["Dugtrio", "Sandslash", "Marowak"],
        ("brown", "earth", "big", "fierce"): ["Dugtrio", "Sandslash", "Marowak"],
        ("pink", "poison", "small", "pretty"): ["Nidoran♀", "Venonat", "Zubat"],
        ("pink", "poison", "small", "fierce"): ["Nidoran♀", "Venonat", "Zubat"],
        ("pink", "poison", "big", "pretty"): ["Nidoqueen", "Venomoth", "Golbat"],
        ("pink", "poison", "big", "fierce"): ["Nidoqueen", "Venomoth", "Golbat"],
        ("grey", "normal", "small", "pretty"): ["Rattata", "Spearow", "Meowth"],
        ("grey", "normal", "small", "fierce"): ["Rattata", "Spearow", "Meowth"],
        ("grey", "normal", "big", "pretty"): ["Raticate", "Fearow", "Persian"],
        ("grey", "normal", "big", "fierce"): ["Raticate", "Fearow", "Persian"],
        ("brown", "fighting", "small", "pretty"): ["Mankey", "Machop", "Hitmonlee"],
        ("brown", "fighting", "small", "fierce"): ["Mankey", "Machop", "Hitmonlee"],
        ("brown", "fighting", "big", "pretty"): ["Primeape", "Machoke", "Hitmonchan"],
        ("brown", "fighting", "big", "fierce"): ["Primeape", "Machoke", "Hitmonchan"],
        ("purple", "psychic", "small", "pretty"): ["Abra", "Drowzee", "Gastly"],
        ("purple", "psychic", "small", "fierce"): ["Abra", "Drowzee", "Gastly"],
        ("purple", "psychic", "big", "pretty"): ["Kadabra", "Hypno", "Haunter"],
        ("purple", "psychic", "big", "fierce"): ["Kadabra", "Hypno", "Haunter"],
        ("black", "ghost", "small", "pretty"): ["Gastly", "Koffing", "Cubone"],
        ("black", "ghost", "small", "fierce"): ["Gastly", "Koffing", "Cubone"],
        ("black", "ghost", "big", "pretty"): ["Haunter", "Weezing", "Marowak"],
        ("black", "ghost", "big", "fierce"): ["Haunter", "Weezing", "Marowak"],
        ("blue", "water", "small", "pretty"): ["Poliwag", "Psyduck", "Tentacool"],
        ("blue", "water", "small", "fierce"): ["Poliwag", "Psyduck", "Tentacool"],
        ("blue", "water", "big", "pretty"): ["Poliwhirl", "Poliwrath", "Tentacruel"],
        ("blue", "water", "big", "fierce"): ["Poliwhirl", "Poliwrath", "Tentacruel"],
        ("grey", "flying", "small", "pretty"): ["Spearow", "Zubat", "Farfetch'd"],
        ("grey", "flying", "small", "fierce"): ["Spearow", "Zubat", "Farfetch'd"],
        ("grey", "flying", "big", "pretty"): ["Fearow", "Golbat", "Doduo"],
        ("grey", "flying", "big", "fierce"): ["Fearow", "Golbat", "Doduo"],
        ("black", "poison", "small", "pretty"): ["Ekans", "Grimer", "Koffing"],
        ("black", "poison", "small", "fierce"): ["Ekans", "Grimer", "Koffing"],
        ("black", "poison", "big", "pretty"): ["Arbok", "Muk", "Weezing"],
        ("black", "poison", "big", "fierce"): ["Arbok", "Muk", "Weezing"],
        ("red", "electric", "small", "pretty"): ["Pikachu", "Voltorb", "Jolteon"],
        ("red", "electric", "small", "fierce"): ["Pikachu", "Voltorb", "Jolteon"],
        ("red", "electric", "big", "pretty"): ["Raichu", "Electrode", "Zapdos"],
        ("red", "electric", "big", "fierce"): ["Raichu", "Electrode", "Zapdos"],
        ("brown", "ground", "small", "pretty"): ["Sandshrew", "Diglett", "Cubone"],
        ("brown", "ground", "small", "fierce"): ["Sandshrew", "Diglett", "Cubone"],
        ("brown", "ground", "big", "pretty"): ["Sandslash", "Dugtrio", "Marowak"],
        ("brown", "ground", "big", "fierce"): ["Sandslash", "Dugtrio", "Marowak"],
        ("pink", "fairy", "small", "pretty"): ["Clefairy", "Jigglypuff", "Clefable"],
        ("pink", "fairy", "small", "fierce"): ["Clefairy", "Jigglypuff", "Clefable"],
        ("pink", "fairy", "big", "pretty"): ["Wigglytuff", "Mr. Mime", "Chansey"],
        ("pink", "fairy", "big", "fierce"): ["Wigglytuff", "Mr. Mime", "Chansey"],
        ("black", "poison", "small", "pretty"): ["Venonat", "Zubat", "Ekans"],
        ("black", "poison", "small", "fierce"): ["Venonat", "Zubat", "Ekans"],
        ("black", "poison", "big", "pretty"): ["Venomoth", "Golbat", "Arbok"],
        ("black", "poison", "big", "fierce"): ["Venomoth", "Golbat", "Arbok"],
        ("purple", "poison", "small", "pretty"): ["Nidoran♀", "Nidorina", "Venonat"],
        ("purple", "poison", "small", "fierce"): ["Nidoran♀", "Nidorina", "Venonat"],
        ("purple", "poison", "big", "pretty"): ["Nidoqueen", "Nidoran♀", "Venomoth"],
        ("purple", "poison", "big", "fierce"): ["Nidoqueen", "Nidoran♀", "Venomoth"],
        ("purple", "poison", "small", "pretty"): ["Nidoran♂", "Nidorino", "Ekans"],
        ("purple", "poison", "small", "fierce"): ["Nidoran♂", "Nidorino", "Ekans"],
        ("purple", "poison", "big", "pretty"): ["Nidoking", "Nidoran♂", "Arbok"],
        ("purple", "poison", "big", "fierce"): ["Nidoking", "Nidoran♂", "Arbok"],
        ("purple", "poison", "small", "pretty"): ["Zubat", "Ekans", "Meowth"],
        ("purple", "poison", "small", "fierce"): ["Zubat", "Ekans", "Meowth"],
        ("purple", "poison", "big", "pretty"): ["Golbat", "Arbok", "Persian"],
        ("purple", "poison", "big", "fierce"): ["Golbat", "Arbok", "Persian"],
        ("grey", "normal", "small", "pretty"): ["Meowth", "Psyduck", "Mankey"],
        ("grey", "normal", "small", "fierce"): ["Meowth", "Psyduck", "Mankey"],
        ("grey", "normal", "big", "pretty"): ["Persian", "Primeape", "Growlithe"],
        ("grey", "normal", "big", "fierce"): ["Persian", "Primeape", "Growlithe"],
        ("green", "leaves", "small", "pretty"): ["Bulbasaur", "Caterpie", "Weedle"],
        ("green", "leaves", "small", "fierce"): ["Bulbasaur", "Caterpie", "Weedle"],
        ("green", "leaves", "big", "pretty"): ["Venusaur", "Butterfree", "Beedrill"],
        ("green", "leaves", "big", "fierce"): ["Venusaur", "Butterfree", "Beedrill"],
        ("red", "fire", "small", "pretty"): ["Charmander", "Vulpix", "Growlithe"],
        ("red", "fire", "small", "fierce"): ["Charmander", "Vulpix", "Growlithe"],
        ("red", "fire", "big", "pretty"): ["Charizard", "Arcanine", "Rapidash"],
        ("red", "fire", "big", "fierce"): ["Charizard", "Arcanine", "Rapidash"],
        ("blue", "water", "small", "pretty"): ["Squirtle", "Poliwag", "Psyduck"],
        ("blue", "water", "small", "fierce"): ["Squirtle", "Poliwag", "Psyduck"],
        ("blue", "water", "big", "pretty"): ["Blastoise", "Poliwhirl", "Slowpoke"],
        ("blue", "water", "big", "fierce"): ["Blastoise", "Poliwhirl", "Slowpoke"],
        ("purple", "flowers", "small", "pretty"): ["Oddish", "Bellsprout", "Paras"],
        ("purple", "flowers", "small", "fierce"): ["Oddish", "Bellsprout", "Paras"],
        ("purple", "flowers", "big", "pretty"): ["Vileplume", "Victreebel", "Gloom"],
        ("purple", "flowers", "big", "fierce"): ["Vileplume", "Victreebel", "Gloom"],
        ("yellow", "sweet", "small", "pretty"): ["Pikachu", "Jigglypuff", "Clefairy"],
        ("yellow", "sweet", "small", "fierce"): ["Pikachu", "Jigglypuff", "Clefairy"],
        ("yellow", "sweet", "big", "pretty"): ["Raichu", "Clefable", "Wigglytuff"],
        ("yellow", "sweet", "big", "fierce"): ["Raichu", "Clefable", "Wigglytuff"],
        ("grey", "rock", "small", "pretty"): ["Geodude", "Onix", "Rhyhorn"],
        ("grey", "rock", "small", "fierce"): ["Geodude", "Onix", "Rhyhorn"],
        ("grey", "rock", "big", "pretty"): ["Graveler", "Golem", "Rhydon"],
        ("grey", "rock", "big", "fierce"): ["Graveler", "Golem", "Rhydon"],
        ("brown", "earth", "small", "pretty"): ["Diglett", "Sandshrew", "Cubone"],
        ("brown", "earth", "small", "fierce"): ["Diglett", "Sandshrew", "Cubone"],
        ("brown", "earth", "big", "pretty"): ["Dugtrio", "Sandslash", "Marowak"],
        ("brown", "earth", "big", "fierce"): ["Dugtrio", "Sandslash", "Marowak"],
        ("pink", "poison", "small", "pretty"): ["Nidoran♀", "Venonat", "Zubat"],
        ("pink", "poison", "small", "fierce"): ["Nidoran♀", "Venonat", "Zubat"],
        ("pink", "poison", "big", "pretty"): ["Nidoqueen", "Venomoth", "Golbat"],
        ("pink", "poison", "big", "fierce"): ["Nidoqueen", "Venomoth", "Golbat"],
        ("grey", "normal", "small", "pretty"): ["Rattata", "Spearow", "Meowth"],
        ("grey", "normal", "small", "fierce"): ["Rattata", "Spearow", "Meowth"],
        ("grey", "normal", "big", "pretty"): ["Raticate", "Fearow", "Persian"],
        ("grey", "normal", "big", "fierce"): ["Raticate", "Fearow", "Persian"],
        ("brown", "fighting", "small", "pretty"): ["Mankey", "Machop", "Hitmonlee"],
        ("brown", "fighting", "small", "fierce"): ["Mankey", "Machop", "Hitmonlee"],
        ("brown", "fighting", "big", "pretty"): ["Primeape", "Machoke", "Hitmonchan"],
        ("brown", "fighting", "big", "fierce"): ["Primeape", "Machoke", "Hitmonchan"],
        ("purple", "psychic", "small", "pretty"): ["Abra", "Drowzee", "Gastly"],
        ("purple", "psychic", "small", "fierce"): ["Abra", "Drowzee", "Gastly"],
        ("purple", "psychic", "big", "pretty"): ["Kadabra", "Hypno", "Haunter"],
        ("purple", "psychic", "big", "fierce"): ["Kadabra", "Hypno", "Haunter"],
        ("black", "ghost", "small", "pretty"): ["Gastly", "Koffing", "Cubone"],
        ("black", "ghost", "small", "fierce"): ["Gastly", "Koffing", "Cubone"],
        ("black", "ghost", "big", "pretty"): ["Haunter", "Weezing", "Marowak"],
        ("black", "ghost", "big", "fierce"): ["Haunter", "Weezing", "Marowak"],
        ("blue", "water", "small", "pretty"): ["Poliwag", "Psyduck", "Tentacool"],
        ("blue", "water", "small", "fierce"): ["Poliwag", "Psyduck", "Tentacool"],
        ("blue", "water", "big", "pretty"): ["Poliwhirl", "Poliwrath", "Tentacruel"],
        ("blue", "water", "big", "fierce"): ["Poliwhirl", "Poliwrath", "Tentacruel"],
        ("grey", "flying", "small", "pretty"): ["Spearow", "Zubat", "Farfetch'd"],
        ("grey", "flying", "small", "fierce"): ["Spearow", "Zubat", "Farfetch'd"],
        ("grey", "flying", "big", "pretty"): ["Fearow", "Golbat", "Doduo"],
        ("grey", "flying", "big", "fierce"): ["Fearow", "Golbat", "Doduo"],
        ("black", "poison", "small", "pretty"): ["Ekans", "Grimer", "Koffing"],
        ("black", "poison", "small", "fierce"): ["Ekans", "Grimer", "Koffing"],
        ("black", "poison", "big", "pretty"): ["Arbok", "Muk", "Weezing"],
        ("black", "poison", "big", "fierce"): ["Arbok", "Muk", "Weezing"],
        ("red", "electric", "small", "pretty"): ["Pikachu", "Voltorb", "Jolteon"],
        ("red", "electric", "small", "fierce"): ["Pikachu", "Voltorb", "Jolteon"],
        ("red", "electric", "big", "pretty"): ["Raichu", "Electrode", "Zapdos"],
        ("red", "electric", "big", "fierce"): ["Raichu", "Electrode", "Zapdos"],
        ("brown", "ground", "small", "pretty"): ["Sandshrew", "Diglett", "Cubone"],
        ("brown", "ground", "small", "fierce"): ["Sandshrew", "Diglett", "Cubone"],
        ("brown", "ground", "big", "pretty"): ["Sandslash", "Dugtrio", "Marowak"],
        ("brown", "ground", "big", "fierce"): ["Sandslash", "Dugtrio", "Marowak"],
        ("pink", "fairy", "small", "pretty"): ["Clefairy", "Jigglypuff", "Clefable"],
        ("pink", "fairy", "small", "fierce"): ["Clefairy", "Jigglypuff", "Clefable"],
        ("pink", "fairy", "big", "pretty"): ["Wigglytuff", "Mr. Mime", "Chansey"],
        ("pink", "fairy", "big", "fierce"): ["Wigglytuff", "Mr. Mime", "Chansey"],
    }

    for color, habitat, size, personality in pokemon_choices.keys():
        print(f"Color: {color}, Habitat: {habitat}, Size: {size}, Personality: {personality}, Pokemon: {pokemon_choices[(color, habitat, size, personality)]}")

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
