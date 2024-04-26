# Constants
initial_investment = 100000  # Initial capital investment
annual_contribution = 100000  # Annual addition to the investment
annual_return_rate = 0.50  # 30% annual return
years = 5  # Duration of the investment in years

# Calculate the total amount after 5 years
total_amount = initial_investment
for year in range(1, years + 1):
    total_amount = total_amount * (1 + annual_return_rate) + annual_contribution

total_amount - annual_contribution  
# Subtract the final year's contribution which doesn't earn interest in this model
print(total_amount)