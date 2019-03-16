import random

# doing some calculations on this number
new_fave = ((1 + 1) * 2) ** 5 + 123456
print(new_fave)

# check if new_fave is divisible by 5

if (new_fave % 5 == 0):
    print("Is new fave number divisible by 5? True")
else:
    print("Is new fave number divisible by 5? False")

# doing the same calculations as above on this number
new_fave_2 = ((42 + 42)* 2) ** 5 + 123456
print(new_fave_2)

# check if new_fave_2 is divisible by 5

if (new_fave_2 % 5 == 0):
    print("Is new fave number #2 divisible by 5? True")
else:
    print("Is new fave number #2 divisible by 5? False")

rand_num = random.randint(0,3)
fave_word ="helloworld"+rand_num*"Bob"
print(fave_word)

rand_num = random.randint(0,3)
fave_word_2='csc108world'+rand_num*"Bob"
print(fave_word_2)

rand_num = random.randint(0,3)
fave_word_3 ='catzworld'+rand_num*"Bob"
print(fave_word_3)
