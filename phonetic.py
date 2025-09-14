
def prepText(paragraph):
    words = []
    #make every letter lowercase
    paragraph = paragraph.lower()
    for letter in paragraph:
        #for every letter in the paragraph, ensure that it is within the range of lowercase alphabetic characters. except spaces
        if not ord("a") <= ord(letter) <= ord("a")+25 and not ord(letter) == ord(" "):
            #effectively delete any non alphabetic character
            paragraph = paragraph.replace(letter, "")
    #split the paragraph at every space point
    words = paragraph.split(" ")
    #ensure no empty strings slip by to ruin the rest of the code
    while "" in words:
        words.remove("")
    return words


def createDict(list):
    dict = {}
    #create an empty list as a value for all lowercase letters as keys
    for x in range(26):
        dict[chr(ord("a")+x)] = []
    #use a temperory list to extract the current list and then append the word into it
    #i was not able to figure out a way to do it in one line
    for word in list:
        tempList = dict[word[0]]
        tempList.append(word)
    return dict

def main():
    #text input from user
    text = input("Input your paragraph:\n")
    print()
    wordsList = prepText(text)
    dict = createDict(wordsList)
    #print every key:value pair in dict
    for key in dict:
        print(f"{key}:{dict[key]}")

if __name__ == "__main__":
    main()