email = input("Your email address: ")

# "hello.worldcom"    => An email address has to contain a '@' character!
# "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
# "@world.com"        => The username before the '@' character cannot be empty!
# "hello@"            => The domain after the '@' character cannot be empty!
# "hello@worldcom"    => An email address has to contain at least one '.' character!
# "hell.o@worldcom"   => The domain has to contain at least one '.' character!
# "he.llo@worldcom."  => The top-level domain cannot be empty!
# "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
# ".hello@world.com"  => The username cannot start with a '.' character!
# "he.llo@.world.com" => The domain cannot start with a '.' character!
# "hello@world.com"   => Valid email address :)


length_of_email = len(email)
number_of_at_characters = email.count("@")
number_of_dot_characters = email.count(".")
position_of_at = email.find("@")

position_of_first_dot = email.find(".")
position_of_last_dot = email.rfind(".")
position_of_first_dot_after_the_at = email.find(".", position_of_at)


error_message_no_at = "An email address has to contain a '@' character!"
error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
error_message_no_dot = "An email address has to contain at least one '.' character!"
error_message_no_username = "The username before the '@' character cannot be empty!"
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
error_message_no_server_name = "The domain cannot start with a '.' character!"
error_message_no_tld = "The top-level domain cannot be empty!"
error_message_short_tld = "The top-level domain has to be at least two characters long!"
error_message_no_domain = "The domain after the '@' character cannot be empty!"
error_message_invalid_username = "The username cannot start with a '.' character!"

ok_message = "Valid email address :)"
is_valid = True

# csak egy "@"
if number_of_at_characters == 0:
    print(error_message_no_at)
    is_valid = False
elif number_of_at_characters > 1:
    print(error_message_too_many_at)
    is_valid = False

# felhasználónév nem üres
elif position_of_at == 0:
    print(error_message_no_username)
    is_valid = False

# domain nem üres
elif position_of_at == length_of_email - 1:
    print(error_message_no_domain)
    is_valid = False

# felhasználónév nem kezdődik '.' -tal
elif email[0] == ".":
    print(error_message_invalid_username)
    is_valid = False

# domain nem kezdődik '.' -tal
elif email[position_of_at + 1] == ".":
    print(error_message_no_server_name)
    is_valid = False

# van-e '.' az email-ben
elif number_of_dot_characters == 0:
    print(error_message_no_dot)
    is_valid = False

# domainban van-e '.'
elif position_of_first_dot_after_the_at == -1:
    print(error_message_no_dot_in_domain)
    is_valid = False

# domain nem végződik '.' -tal
elif email[-1] == ".":
    print(error_message_no_tld)
    is_valid = False

# TLD legalább 2 karakter hosszú
elif len(email[position_of_last_dot + 1:]) < 2:
    print(error_message_short_tld)
    is_valid = False

# érvényes email cím
if is_valid:
    print(ok_message)