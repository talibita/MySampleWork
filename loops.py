'''password=input("Please enter your password:\n")
while password!="Oracle#123":
    
    print("You entered a wrong password")
    password = input("Please try again: ")
print("Welcome to your account")'''

username=input("Please enter your username:\n")
invalid="!@#$%^&*"
for letter in username:
    if letter in invalid:
        print("This character is not allowed", letter)


#Uses a for loop to count vowels in a word and displays the number of vowels in the word entered by the user.
vowels="aeiou"
constants="bcdfghjklmnpqrstvwxyz"
word=input("Enter a word of your choice")
vowel_num=0
for letter in word:
    if letter in vowels:
        vowel_num+=1
    elif letter in constants:
        vowel_num+=0
print("There are ", vowel_num, "in the word")        
print(type(2+7))