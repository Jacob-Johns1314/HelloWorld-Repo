def calculate_tax(income, status):
    # Define tax brackets and rates
    tax_brackets = {
        "single": [(11000, 0.10), (44725, 0.12), (95375, 0.22)],
        "married": [(22000, 0.10), (89450, 0.12), (190750, 0.22)]
    }
    
    # Check if marital status is valid
    if status.lower() not in tax_brackets:
        return "Invalid marital status. Please enter 'single' or 'married'."
    
    brackets = tax_brackets[status.lower()]
    
    if income > brackets[-1][0]:
        return "Income exceeds supported tax brackets. Please refer to the full tax table."
    
    # Calculate tax owed
    tax_owed = 0
    previous_limit = 0
    for limit, rate in brackets:
        if income > limit:
            tax_owed += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax_owed += (income - previous_limit) * rate
            break
    
    return f"Tax owed: ${tax_owed:.2f}"

# Get user input
income = float(input("Enter your earned income: "))
status = input("Enter your marital status (single/married): ")

# Output tax owed
print(calculate_tax(income, status))
