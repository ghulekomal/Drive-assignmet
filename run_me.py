import main as x
x.create_dictionary("Komal", 25)
# to create a key and value calling create function

# we can access these using multiple threads like
x.create_dictionary("Komal", 70, 3600)
# here also we are providing kel value and time-to-live in seconds

x.read_dictionary("Komal")
# it returns the value of the respective key in Jasonobject format 'key_name:value', from read_dictonary function

x.read_dictionary("Komal")
# it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

x.create_dictionary("sastra", 50)
#Here we are providing key and value but enter key Komal is alredy present so it will return a error
#we can do modify_dictionary or can delete key and can carete it gain

x.modify_dictionary("Komal", 55)
# it replaces the old value with new

x.delete_dictionary("Komal")
# it deletes the respective key and its value from the database(memory is also freed)
x.read_dictionary("Komal")