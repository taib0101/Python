# Convert list to string 
charachters: list = ['M', 'a', 'd', 'a', 'm', 'I', 'a', 'm', 'A', 'd', 'a', 'm']
sentence: str = "".join(charachters)
print("converted list to sentence : ", sentence)


# Convert string to list
sentence: str = "MadamIamAdam"
charachters: list = sentence.split()
print("Converted string to list : ", charachters)

# for seperation on each character 
charachters: list = list(sentence)
print("Converted string to list : ", charachters)
