from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if (min > max or quantity < 1 or min < 1 or max > 1000):
        return []

    all_possible_numbers = list(range(min, max + 1))

    if quantity > len(all_possible_numbers):
        return []

    selected_numbers = sample(all_possible_numbers, quantity)

    return sorted(selected_numbers)
