#Task

# Given the meal price (base cost of a meal),
# tip percent (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being added as tax) for a meal,
# find and print the meal's total cost. Round the result to the nearest integer.

def solve(meal_cost, tip_percent, tax_percent):
    tip = tip_percent / 100 * meal_cost
    tax = tax_percent / 100 * meal_cost
    total_cost = meal_cost + tip + tax
    print(round(total_cost));

