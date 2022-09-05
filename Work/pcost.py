# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_cost = 0.0;
    with open(filename, "rt") as f:
        header = next(f)
        for line in f:
            row = line.split(",")
            cost = int(row[1]) * float(row[2])
            total_cost = total_cost + cost
    print("Total cost:", total_cost)

cost = portfolio_cost("Work/Data/portfolio.csv")
print("Total cost:", cost)