import eel
from funciones import gauss_jordan_2x2 as Gauss2x2
from funciones import gauss_jordan_3x3 as Gauss3x3
from ordenamiento import sort_entries_ascending as sort_ascending_2x2
from ordenamiento import sort_entries_descending as sort_descending_2x2

# Start the Eel app
eel.init('web')

entries = {}

def update_entries(entry):
    entry_id = len(entries) + 1  # Generate a new ID for the entry
    entries[entry_id] = entry  # Save the entry with the new ID
    print(entries)


@eel.expose
def solve_two_variable_system(eq1, eq2):
    
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    # Convert the input values to floats and call the 2x2 solver
    solutions = Gauss2x2(eq1, eq2)
    
    # Create an entry for the new solution
    entry = {
        'type': '2x2',
        'equations': [eq1, eq2],
        'solutions': solutions
    }
    update_entries(entry)  # Add the entry to the dictionary
    
    # Send the results back to the HTML file
    eel.display_solutions(solutions)

@eel.expose
def solve_three_variable_system(eq1, eq2, eq3):
    # Convert the input values to floats and create the augmented matrix
    matrix = [
        eq1,
        eq2,
        eq3
    ]
    # Call the 3x3 solver
    solutions = Gauss3x3(matrix[0], matrix[1], matrix[2])
    print(solutions)    
    
    # Create an entry for the new solution
    entry = {
        'type': '3x3',
        'equations': [eq1, eq2, eq3],
        'solutions': solutions
    }
    update_entries(entry)  # Add the entry to the dictionary
    
    # Send the results back to the HTML file
    eel.display_solutions(solutions)

@eel.expose
def get_all_entries():
    # Since we can't send a dictionary with integer keys directly to JavaScript,
    # we convert the entries to a list.
    return list(entries.values())

@eel.expose
def get_entries_by_type(entry_type):
    try:
        all_entries = entries
        filtered_entries = [
    entry for entry_id, entry in entries.items() 
    if isinstance(entry, dict) and entry.get('type') == entry_type
]
    except TypeError as e:
        print(f"An error ocurred: {e}")
        filtered_entries = []
    return filtered_entries

@eel.expose
def sort_entries(order):
    global entries
    if order == 'ascending':
        entries = sort_ascending_2x2(entries)
    elif order == 'descending':
        entries = sort_descending_2x2(entries)
    return entries

@eel.expose
def show_page(page):
    eel.start(page, size=(800, 600), block=False)

eel.start('index.html', size=(800, 1000))  # The starting page should be the index.html