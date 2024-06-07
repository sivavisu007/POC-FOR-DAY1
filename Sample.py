#Create a string for helps to find the vowels
letter = "aeiou"
#Created a string to find a how vowels are there?
s = input("Enter the sentence to find the vowels:")
#Changing the total to caseless comparison
s = s.casefold()
#using {}.fromkeys() to make a dictionary with each vowels key and values
count = {}.fromkeys(letter, 0)
#print(count) # if i print the input vowels it will return the all vowels as zero, so we dont print in this place.
# using for loop to count the vowels
for char in s:
    if char in count:
        count[char] +=1
        #print(count)
print(count)
