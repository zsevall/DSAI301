#zeynep_seval_2024660042_hw1
#Defining variables
h = 15  # height
r = 3   # radius
π = 3   # pi

#1-a Base Area Calculation
S = π * r**2
print("Base Area of Cylinder:", S, "cm2")

#1-b Surface Area Calculation
surface_area = 2 * π * r**2 + 2 * π * r * h
print("Surface Area of cylinder:", surface_area, "cm2")

#1-c Volume of cylinder
volume = π * r**2 * h
print("Volume of Cylinder:", volume, "cm3")

#1-d Calculate length l
# x^0.5 is equivalent to sqrt(x)
length_l = (r**2 + h**2)**0.5
print("The length l is", round(length_l,2), "cm")  #rounded with 2 digits

#2a
index = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gardening Tips</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 20px;
        }
        h1 {
            color: #4CAF50;
        }
        nav {
            text-align: center;
            margin-bottom: 20px;
        }
        nav a {
            margin: 0 10px;
            text-decoration: none;
            color: #4CAF50;
        }
        nav a:hover {
            text-decoration: underline;
        }
        section {
            max-width: 800px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <header>
        <h1>Gardening Tips</h1>
    </header>
    <nav>
        <a href="https://www.example.com/planting-basics">Planting Basics</a>
        <a href="https://www.example.com/soil-preparation">Soil Preparation</a>
        <a href="https://www.example.com/garden-tools">Garden Tools</a>
    </nav>
    <section>
        <h2>Welcome to Gardening Tips</h2>
        <p>Whether you're a seasoned gardener or just starting out, our tips and guides will help you cultivate a beautiful and bountiful garden. Explore the links above to learn more about planting basics, soil preparation, and essential garden tools.</p>
        <p>Happy gardening!</p>
    </section>
</body>
</html>"""

#2b
# Find first link
start_link = index.find('<a href=')
start_quote = index.find('"', start_link)
end_quote = index.find('"', start_quote + 1)
link1 = index[start_quote + 1:end_quote]

# Find second link by slicing the remaining text
index = index[end_quote:]
start_link = index.find('<a href=')
start_quote = index.find('"', start_link)
end_quote = index.find('"', start_quote + 1)
link2 = index[start_quote + 1:end_quote]

# Find third link by slicing again
index = index[end_quote:]
start_link = index.find('<a href=')
start_quote = index.find('"', start_link)
end_quote = index.find('"', start_quote + 1)
link3 = index[start_quote + 1:end_quote]

#2c print all links
print("First link:", link1)
print("Second link:", link2)
print("Third link:", link3)

#3
# Set the price of dream house
home_price = 900000 # 150m2 apt in Etiler given that average home price in 6000$/m2

# Get user input for salary and savings rate
monthly_salary = float(input("Enter your monthly salary in USD: "))
savings_percentage = float(input("Enter the percentage of salary you will save each month (e.g., 20 for 20%): "))

# Calculate monthly savings
monthly_savings = monthly_salary * (savings_percentage / 100)

# Calculate number of months needed and round to nearest integer
months_needed = int(home_price / monthly_savings + 0.5)

# Print the result
print("With a monthly savings of", monthly_savings, "USD, it will take", months_needed, "months to save enough money for the house.")