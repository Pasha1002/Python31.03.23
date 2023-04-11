
word_list = input("Enter the words through the space: ").split()

word_list.sort(key=len)

print("The words are sorted by increasing length: ")
print(word_list)