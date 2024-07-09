from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if (min > max or quantity < 1 or min < 1 or max > 1000):
        return []

    all_possible_numbers = list(range(min, max + 1))

    if quantity > len(all_possible_numbers):
        return []

    selected_numbers = []

    for _ in range(quantity):
        index = randint(0, len(all_possible_numbers) - 1)
        selected_number = all_possible_numbers.pop(index)
        selected_numbers.append(selected_number)

    return sorted(selected_numbers)

