import csv, sys
from tabulate import tabulate

pizzas = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        pizzas.append(row)

headers = ["]
print(tabulate(pizzas, tablefmt="grid"))
print(pizzas[0])