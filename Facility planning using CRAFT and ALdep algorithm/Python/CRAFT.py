import numpy as np
import pandas as pd

def calculate_cost(layout, flow_matrix, distance_matrix):
    total_cost = 0
    for i in range(len(layout)):
        for j in range(len(layout)):
            total_cost += flow_matrix[layout[i]][layout[j]] * distance_matrix[i][j]
    return total_cost

def craft_algorithm(initial_layout, flow_matrix, distance_matrix, department_sizes, adjacent_departments):
    # Create a dictionary to map department names to indices
    layout_dict = {dept: i for i, dept in enumerate(initial_layout)}
    
    # Convert the layout to indices
    current_layout = [layout_dict[dept] for dept in initial_layout]
    
    current_cost = calculate_cost(current_layout, flow_matrix, distance_matrix)
    print(f"Initial cost: {current_cost}")
    
    # List to store the swaps
    swaps = []
    
    while True:
        for i in range(len(current_layout)):
            for j in range(i+1, len(current_layout)):
                # Only consider swapping departments of the same size or adjacent departments
                if department_sizes[initial_layout[i]] == department_sizes[initial_layout[j]] or initial_layout[j] in adjacent_departments[initial_layout[i]]:
                    # Swap two departments
                    new_layout = current_layout[:]
                    new_layout[i], new_layout[j] = new_layout[j], new_layout[i]
                    
                    # Calculate the new cost
                    new_cost = calculate_cost(new_layout, flow_matrix, distance_matrix)
                    
                    # If the new cost is less than the current cost, update the layout and cost
                    if new_cost < current_cost:
                        current_layout = new_layout
                        current_cost = new_cost
                        
                        # Record the swap
                        swaps.append((initial_layout[i], initial_layout[j]))
                        
                        # Update the adjacency list
                        for k in range(len(adjacent_departments[initial_layout[i]])):
                            if adjacent_departments[initial_layout[i]][k] == initial_layout[j]:
                                adjacent_departments[initial_layout[i]][k] = initial_layout[i]
                        for k in range(len(adjacent_departments[initial_layout[j]])):
                            if adjacent_departments[initial_layout[j]][k] == initial_layout[i]:
                                adjacent_departments[initial_layout[j]][k] = initial_layout[j]
                        break
            else:
                continue
            break
        else:
            # If no improvement was found in the entire loop, return the current layout and the swaps
            print(f"Optimal cost: {current_cost}")
            return [initial_layout[i] for i in current_layout], swaps  # Convert indices back to department names

# Calculation
initial_layout = ['Dep1', 'Dep2', 'Dep3', 'Dep4', 'Dep5', 'Dep6', 'Dep7', 'Dep8', 'Dep9', 'Dep10', 'Dep11', 'Dep12', 'Dep13']
department_sizes = {'Dep1': 160, 'Dep2': 160, 'Dep3': 160, 'Dep4': 110, 'Dep5': 100, 'Dep6': 60, 'Dep7': 50, 'Dep8': 600, 'Dep9': 340, 'Dep10': 180, 'Dep11': 80, 'Dep12': 170, 'Dep13': 170}
adjacent_departments = {
    'Dep1': ['Dep13', 'Dep9', 'Dep5', 'Dep6'],
    'Dep2': ['Dep5', 'Dep6', 'Dep3', 'Dep8'],
    'Dep3': ['Dep2', 'Dep8', 'Dep7', 'Dep4'],
    'Dep4': ['Dep3', 'Dep7', 'Dep8'],
    'Dep5': ['Dep6', 'Dep1', 'Dep8', 'Dep2'],
    'Dep6': ['Dep1', 'Dep5', 'Dep2'],
    'Dep7': ['Dep3', 'Dep4', 'Dep8'],
    'Dep8': ['Dep9', 'Dep7', 'Dep4', 'Dep3', 'Dep2', 'Dep5'],
    'Dep9': ['Dep8', 'Dep10', 'Dep13', 'Dep1'],
    'Dep10': ['Dep11', 'Dep9'],
    'Dep11': ['Dep10'],
    'Dep12': ['Dep10', 'Dep13'],
    'Dep13': ['Dep1', 'Dep9', 'Dep12']
}
flow_matrix = [
    [0, 0, 0, 0, 183, 68,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 183, 68,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 183, 68,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 183, 68,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0, 730, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0, 272, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0,   0, 218, 45, 10, 137, 137, 456],
    [0, 0, 0, 0,   0,  0,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0,   0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,   0,  0,   0, 0, 0, 0, 0, 0, 0]
]
distance_matrix = [
    [0, 6.4, 9.6, 19.45, 12.4, 17.8, 29.95, 54.9318, 47.346, 53.6474, 56.7481, 6.55, 3.2],
    [6.4, 0, 3.2, 13.05, 12.4, 17.8, 23.55, 48.5318, 53.746, 60.0474, 63.1481, 12.95, 9.6],
    [9.6, 3.2, 0, 9.85, 15.6, 21, 20.35, 45.496, 56.946, 63.2474, 66.3481, 16.15, 12.8],
    [19.45, 13.05, 9.85, 0, 25.45, 17.55, 23.8, 55.346, 66.796, 73.0974, 76.1981, 26, 22.65],
    [12.4, 12.4, 15.6, 25.45, 0, 23.8, 17.55, 42.5318, 41.346, 47.6474, 50.7481, 18.95, 15.6],
    [17.8, 17.8, 21, 17.55, 23.8, 0, 41.35, 66.3318, 65.146, 71.4474, 74.5481, 24.35, 21],
    [29.95, 23.55, 20.35, 23.8, 17.55, 41.35, 0, 31.546, 42.996, 49.2974, 52.3981, 36.5, 33.15],
    [54.9318, 48.5318, 45.496, 55.346, 42.5318, 66.3318, 31.546, 0, 11.45, 17.7514, 20.8521, 61.4818, 58.1318],
    [47.346, 53.746, 56.946, 66.796, 41.346, 65.146, 42.996, 11.45, 0, 6.3014, 9.4021, 50.0318, 46.6818],
    [53.6474, 60.0474, 63.2474, 73.0974, 47.6474, 71.4474, 49.2974, 17.7514, 6.3014, 0, 3.1007, 47.0974, 50.4474],
    [56.7481, 63.1481, 66.3481, 76.1981, 50.7481, 74.5481, 52.3981, 20.8521, 9.4021, 3.1007, 0, 50.1981, 53.5481],
    [6.55, 12.95, 16.15, 26, 18.95, 24.35, 36.5, 61.4818, 50.0318, 47.0974, 50.1981, 0, 3.35],
    [3.2, 9.6, 12.8, 22.65, 15.6, 21, 33.15, 58.1318, 46.6818, 50.4474, 53.5481, 3.35, 0]
]

print("Initial layout:", initial_layout)
optimal_layout, swaps = craft_algorithm(initial_layout, flow_matrix, distance_matrix, department_sizes, adjacent_departments)
print("Swaps made:")
for swap in swaps:
    print(swap)
print("Final layout:", optimal_layout)
