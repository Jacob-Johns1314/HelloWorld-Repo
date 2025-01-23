# Name: Jacob Johnson

# Human age converted to dog years
def calculate_dog_years(human_age):
    """Converts human age to dog years."""
    dog_years = human_age * 7
    return convert_to_years_months_days(dog_years)

# Human age converted to cat years
def calculate_cat_years(human_age):
    """Converts human age to cat years."""
    cat_years = human_age / 9
    return convert_to_years_months_days(cat_years)

# Human age converted to horse years
def calculate_horse_years(human_age):
    """Converts human age to horse years using the given formula."""
    horse_years = 3 * ((human_age ** 2 - 47) / 7 + 12)
    return convert_to_years_months_days(horse_years)

# Function to convert fractional years into years, months, and days
def convert_to_years_months_days(age_in_years):
    """Converts fractional years into years, months, and days."""
    years = int(age_in_years)  # Whole years
    months = int((age_in_years - years) * 12)  # Remaining months
    days = int(((age_in_years - years) * 12 - months) * 30)  # Remaining days
    return years, months, days

# Request input from the user
human_age = float(input("Enter human age in years: "))

# Calculate and display age in dog years
dog_years, dog_months, dog_days = calculate_dog_years(human_age)
print(f"Your age in dog years: {dog_years} years, {dog_months} months, {dog_days} days")

# Calculate and display age in cat years
cat_years, cat_months, cat_days = calculate_cat_years(human_age)
print(f"Your age in cat years: {cat_years} years, {cat_months} months, {cat_days} days")

# Calculate and display age in horse years
horse_years, horse_months, horse_days = calculate_horse_years(human_age)
print(f"Your age in horse years: {horse_years} years, {horse_months} months, {horse_days} days")
