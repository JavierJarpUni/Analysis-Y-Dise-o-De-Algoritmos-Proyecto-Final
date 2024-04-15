import math

def calculate_magnitude(solutions):
    return math.sqrt(sum(x**2 for x in solutions))

def find_index_of_min(entries_list, start_index, min_index):
    if start_index == len(entries_list):
        return min_index
    if calculate_magnitude(entries_list[start_index][1]['solutions']) < \
       calculate_magnitude(entries_list[min_index][1]['solutions']):
        min_index = start_index
    return find_index_of_min(entries_list, start_index + 1, min_index)

def sort_entries_ascending_recursive(entries_list, index=0):
    if index < len(entries_list) - 1:
        min_index = find_index_of_min(entries_list, index, index)
        if min_index != index:
            entries_list[index], entries_list[min_index] = entries_list[min_index], entries_list[index]
        sort_entries_ascending_recursive(entries_list, index + 1)

def find_index_of_max(entries_list, start_index, max_index):
    if start_index == len(entries_list):
        return max_index
    if calculate_magnitude(entries_list[start_index][1]['solutions']) > \
       calculate_magnitude(entries_list[max_index][1]['solutions']):
        max_index = start_index
    return find_index_of_max(entries_list, start_index + 1, max_index)

def sort_entries_descending_recursive(entries_list, index=0):
    if index < len(entries_list) - 1:
        max_index = find_index_of_max(entries_list, index, index)
        if max_index != index:
            entries_list[index], entries_list[max_index] = entries_list[max_index], entries_list[index]
        sort_entries_descending_recursive(entries_list, index + 1)
        
