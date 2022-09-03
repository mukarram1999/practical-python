# pcost.py
#
# Exercise 1.27
total_cost = 0.0;
with open("Data/portfolio.csv", "rt") as f:
    header = next(f)
    for line in f:
        row = line.split(",")
        cost = int(row[1]) * float(row[2])
        total_cost = total_cost + cost
print("Total cost is ", total_cost)
