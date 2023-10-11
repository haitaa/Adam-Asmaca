my_string = "James Hetfield"
my_letter = my_string[4]

my_new_string = "QuentinTarantino"
my_new_letter = my_new_string[5:9]

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"
my_last_string_new = my_last_string[::-1]

my_list = [1, 2, "a"]
my_dict = {1, 2, "a"}
my_tuple = (1, 2, "a")

my_list1 = [1, 4, [2, 3, "a"]]
a = my_list1[2][2]

my_dictionary = {"k1": 2, "kk": [4, {"kkk": "b"}]}
b = my_dictionary["kk"][1]["kkk"]

my_list_to_be_set = [11, 12, 22, 33, 11, 22, 45, 32, 21, 22, 33, 45]
my_set = set(my_list_to_be_set)

my_list = [1, 2, 3, 4, 5]

for number in my_list:
    if number % 2 == 0:
        print("Çift " + str(number))
    else:
        print("Tek " + str(number))