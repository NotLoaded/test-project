

# Information about myself and what I do: difined ind my_() and about_me_()

my_name = "Clemens Eckhardt"
my_age = 22
my_birthdate = 20-2-2000
about_me_job = "Computer Science Student"
about_me_workplace = "Highschool"
about_me_current_home = "Mobridge, South Dakota"


# Information about the Appartment and what I like about it.

appartment_name = "3 Room Appartment"
appartment_pro = "that it has a big living room area and space for home office working"
appartment_address = "xyz"


# Information about the Appartment Landlord

appartment_landlord_name = "Meier"
appartment_landlord_gender_male = True
appartment_landlord_gender = "null"



# Change appartment-landlord_gender to "Mr." if true and "Mrs." if false, from apppartment_landlord_gender_male.

if appartment_landlord_gender_male:
    appartment_landlord_gender = "Mr."

else:
    appartment_landlord_gender = "Mrs."



# Prints out the application.

print("Dear", appartment_landlord_gender, appartment_landlord_name + ".")
print("My Name is", my_name, "and I'm a", my_age, "Years old,", about_me_workplace, about_me_job, "from", about_me_current_home, ".")
print("I'm applying for the", appartment_name, "in", appartment_address, "." + "\r\nWhat I really like about this Appartment is that", appartment_pro + ".")
print("I'm looking forward to hearing from you.")
print("Your's", my_name + ".")