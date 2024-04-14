import math

def calculate_magnitude(solutions):
    """Calculate the Euclidean magnitude of solutions."""
    return math.sqrt(sum(x**2 for x in solutions))

def sort_entries_ascending(entries):
    """Sort entries dictionary by ascending magnitude of solutions."""
    entries_list = list(entries.items())

    def sort_key(entry):
        # Directly access the solutions array without unpacking
        solutions = entry[1]['solutions']
        return calculate_magnitude(solutions)

    # Sort the list by magnitude
    entries_list.sort(key=sort_key)

    # Convert sorted list back to dictionary
    sorted_entries = {entry[0]: entry[1] for entry in entries_list}
    return sorted_entries

def sort_entries_descending(entries):
    """Sort entries dictionary by descending magnitude of solutions."""
    entries_list = list(entries.items())

    entries_list.sort(key=lambda entry: calculate_magnitude(entry[1]['solutions']), reverse=True)
    sorted_entries = {entry[0]: entry[1] for entry in entries_list}
    return sorted_entries