# Write your code here

def num_months():
    num_months = 0
    annual_salary = float(input("Enter your annual salary in $ "))
    portion_saved = float(input("Enter percentage of your salary to save, as a decimal "))
    total_cost = float(input("Enter the total cost of your dream home in $ "))
    portion_down_payment = float(input("Enter percentage of downpayment as a decimal (default is 25%) ") or 0.25)
    total_down_payment = total_cost * portion_down_payment
    r = float(input("Enter the expected annual rate of return as a decimal (default is 4%) ") or 0.04)
    current_savings = 0
    monthly_salary = annual_salary/12
    interest_earned = current_savings*r/12
    
    while current_savings < total_down_payment:
        current_savings += (monthly_salary * portion_saved) + interest_earned
        num_months += 1
        print("Your annual Salary: ", annual_salary)
        print(f"Your salary percentage saved: {int(portion_saved*100)}%")
        print(f"Your expected annual rate of return: {int(r*100)}%")
        print(f"Your down payment is: {int(portion_down_payment*100)}%")
        print("Cost of your dream home:", total_cost)
        print("You have to save for", num_months, "months! Now get saving!!!")
num_months()    
