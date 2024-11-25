# Story
- Your friend recently started an e-commerce business where people can buy little animals like reptilians, snakes, and snails. You have created a basic webshop for the startup.

- Before any purchase the customers need to create an account. Unfortunately, 10% of the users give invalid email addresses on the form, and they cannot be reached again. It's your job to fix this problem, and write a basic email validator for the registration page.


*"A valid email address looks like this: username@do.ma.in. The first part is called username, the second part (after the '@') is the domain. A valid address must follow these rules:

There is exactly one '@' character in it.
Neither the username nor the domain can be empty or start with a . character.
There is at least one . character in the domain, and the top-level domain (the last part of it) must be at least two characters long."*

# Tasks
#### 1. At least one '@'
The validator should give an error when there are no '@' characters in the email address.

- Writing the email hello.worldcom, the program prints An email address has to contain a '@' character!.

#### 2. Only one '@'
The validator should give an error when there are more then one '@' characters are in the email address.

- Writing the email he@@llo@@worldcom, the program prints An email address cannot contain more than one '@' characters!"

#### 3. Username is not empty
The validator should give an error when the username is empty.

- Writing the email @@world.com, the program prints The username before the '@' character cannot be empty!

#### 4. Domain is not empty
The validator should give an error when the domain is empty.

- Writing the email hello@, the program prints The domain after the '@' character cannot be empty!

#### 5. At least one '.'
The validator should give an error when there are no . characters in the email address.

- Writing the email hello@@worldcom, the program prints An email address has to contain at least one '.' character!

#### 6. At least one '.' in domain
The validator should give an error when there are no . characters in the domain.

- Writing the email hell.o@@worldcom, the program prints The domain has to contain at least one '.' character!

#### 7. Top-level domain is not empty
The validator should give an error when the domain ends with a . character.

- Writing the email hello@@worldcom., the program prints The top-level domain cannot be empty!

#### 8. TLD is at least two characters long
The validator should give an error when the last part of the domain is less than two characters long.

- Writing the email hello@@worldco.m, the program prints The top-level domain has to be at least two characters long!

#### 9. Valid username
The validator should give an error when the username starts with a . character.

- Writing the email .hello@@world.com, the program prints The username cannot start with a '.' character!

#### 10. Valid server name
The validator should give an error when the first part of the domain is empty.

- Writing the email he.llo@.world.com, the program prints The domain cannot start with a '.' character!

#### 11. Valid email address
The validator should recognize a valid email address.

- Writing the email hello@world.com, the program prints Valid email address :)

# Hints

- Use the given count and position values to create the error conditions. You won't need any other values for the solution.

- You won't need it here as the values are given, but in other situations you would have to search the internet for expressions like python count number of characters in a string or python find last occurrence in a string, and adapt the found code snippets to your needs.

- The position of the last character is length_of_email - 1.

- The positions of neighboring characters differ by 1.

- Be sure to structure your conditions in a logical way (e.g. do not check for a valid server name before confirming that there is at least a `` and a . present).

# Background materials

- Conditional Statements in Python:

https://realpython.com/python-conditional-statements/

- Strings:

https://www.w3schools.com/python/python_strings.asp