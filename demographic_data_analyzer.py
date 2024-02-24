"""This module analyzes data from a csv file to answer questions"""
import pandas as pd

# Reading the data from the csv file
data = pd.read_csv('adult.data.csv', sep=',')

# Counting the number of people by race
race = data['race'].value_counts()
print("This is the racial distribution of the study:")
print(race)
print("By percentages:")
print((data['race'].value_counts(normalize=True) * 100).round(1))

print("----------------------------------------------------------")

# Average age of the men rounded to the nearest tenth
sex = data[data['sex'] == 'Male']
print("The average age of the men in the study was {}".format(sex['age'].mean().round(1)))

print("----------------------------------------------------------")

# Percentage of people with BSc degrees
bsc = (data['education'].value_counts(normalize=True) * 100).round(1)
print("The percentage of people with BSc degrees was {}%".format(bsc['Bachelors']))

print("----------------------------------------------------------")

# Percentage of people with advanced degrees that make more than 50k
advanced = data[(data['education'] == 'Bachelors') | (data['education'] == 'Masters') | (data['education'] == 'Doctorate')]
salary = ((advanced['salary']).value_counts(normalize=True) * 100).round(1)
print("The percentage of people with advanced degrees who earn above 50K as salary was {}%".format(salary['>50K']))

print("----------------------------------------------------------")

# Percentage of people without advanced education that make more than 50k
not_advanced = data[(data['education'] != 'Bachelors') & (data['education'] != 'Masters') & (data['education'] != 'Doctorate')]
their_salary = ((not_advanced['salary']).value_counts(normalize=True) * 100).round(1)
print("The percentage of people without advanced degrees who earn above 50K was {}%".format(their_salary['>50K']))

print("----------------------------------------------------------")

# The minimum & maximum number of hours a person works per week
hours = data['hours-per-week']
print("The minimum hours worked is {} hour".format(hours.min(), hours.idxmin()))
print("The maximum hours worked is {} hours".format(hours.max(), hours.idxmax()))

print("----------------------------------------------------------")

# Percentage of people working the minimum number of weeks earning above 50k
min_hours_people = data[data['hours-per-week'] == data['hours-per-week'].min()]
percent_min_hours_people = ((min_hours_people['salary']).value_counts(normalize=True) * 100).round(1)
print("The percentage of people working the minimum number of hours per week and still earning above 50K was {}%".format(percent_min_hours_people.min()))

print("----------------------------------------------------------")

# Country with the highest earners and their percentage
highest_earners = data[data['salary'] == '>50K']
filtered = highest_earners[highest_earners['native-country'] != '?']
highest_earners_country = filtered['native-country']
percentage_highest_earners_country = ((highest_earners_country.value_counts(normalize=True) * 100).round(1))
print("The country with the highest percentage of highest earners was {} with {}%".format(percentage_highest_earners_country.idxmax(), percentage_highest_earners_country.max()))

print("----------------------------------------------------------")

# Most popular occupation for those who earn above 50k in India
new_filter = highest_earners[highest_earners['native-country'] == 'India']
occupation = new_filter['occupation'].value_counts()
print("The most popular occupation for people in India who earn above 50K was {}".format(occupation.idxmax()))