#My First Python Program

'''
Hailey Kist
9/6/2024

I will calculate ages of different species based on user_age
'''

user_age=19
dog_years=user_age*7 
dog_months=dog_years/12
dog_days=dog_years/365
#This calculates the user's age in dog years, months, and days
print("Enter your age:", user_age)
print("Your age in dog years is", dog_years, "years,", dog_months, "months,", "and", dog_days, "days.")

cat_years=user_age/9
cat_months=user_age/12
cat_days=user_age/365
#This calculates the user's age in cat years
print("Your age in cat years is", cat_years, "years,", cat_months, "months,","and", cat_days, "days.")

horse_years= ((((user_age**2)-47)/7)+12)*3
horse_months=user_age/12
horse_days=user_age/365
#This calculates the user's age in horse years
print("Your age in horse years is", horse_years, "in horse years,", horse_months, "months,", "and", horse_days, "days.")

