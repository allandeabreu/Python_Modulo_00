def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    new_word = seed_type.capitalize()
    if unit == "packets":
        print(new_word, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(new_word, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(new_word, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
