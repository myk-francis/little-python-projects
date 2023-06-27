"""Birthday Paradox Simulation, by Michael Francis
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
Tags: short, math, simulation"""

import datetime
import random


def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # the birthdays are in the same year.
        start_of_year = datetime.date(2000, 1, 1)
        random_num_of_days = datetime.timedelta(random.randint(1, 365))
        birthday = start_of_year + random_num_of_days
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for index_a, birthday_a in enumerate(birthdays):
        for index_b, birthday_b in enumerate(birthdays[index_a + 1:]):
            if birthday_a == birthday_b:
                # Return the birthday that occurs more than once.
                return birthday_a


# Display the intro:
print('''Birthday Paradox, by Michael Francis

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('How many birthdays should I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and 0 < int(response) <= 100:
        number_of_birthdays = int(response)
        break

print()

# Generate and display the birthdays:
print('Here are', number_of_birthdays, 'birthdays:')
birthdays = get_birthdays(number_of_birthdays)
for index, birthday in enumerate(birthdays):
    if index != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')

    month_name = MONTHS[birthday.month - 1]
    date_text = '{} {}'.format(month_name, birthday.day)
    print(date_text, end='')

print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')

print()

# Run through 100,000 simulations:
print('Generating', number_of_birthdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')
print('Let\'s run another 10 simulations.')
sim_match = 0  # How many simulations had matching birthdays in them.
for i in range(10):
    # Report on the progress every 10,000 simulations:
    if i % 10 == 0:
        print(i, 'simulations run...')

    birthdays = get_birthdays(number_of_birthdays)

    if get_match(birthdays) != None:
        sim_match = sim_match + 1

    print('100,000 simulations run.')
    # Display simulation results:
    probability = round(sim_match / 100_000 * 100, 2)
    print('Out of 100,000 simulations of',
          number_of_birthdays, 'people, there was a')
    print('matching birthday in that group', sim_match, 'times. This means')
    print('that', sim_match, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')
