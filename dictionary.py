dictionary_file = open("dic.txt", "r")
words = {}
#Sprachen
ger = \
    {
    0:"Geben Sie die gesuchte Übersetzung ein: ",
    1:"Leere Anfragen sind unfair, die kann ich leider nicht akzeptieren ;-)",
    2:"Dieses Wort ist uns nicht bekannt. Bitte auf Groß/Kleinbuchstaben achten!"
    }
eng = \
    {
    0:"Please type in your desired translation: ",
    1:"Please give me something to work with. I can't work like this ;-)",
    2:"We don't know that word. Please check for upper/lower case words!"
    }
lang = eng


#reading an catalogue words from dic.txt
def read_file():
    for line in dictionary_file:
        line = line.strip()
        classification = line.split(" ")
        words[classification[0]] = classification[1]
        words[classification[1]] = classification[0]
        

    dictionary_file.close()
    user_input()

#user input
def user_input():
    user_input.user_search = (input(lang[0]))
    result_check()

#check if word is in dictionary_file
def result_check():
    if (user_input.user_search in words):
        print (user_input.user_search,"=",words[user_input.user_search])
    elif (user_input.user_search == ""):
        print (lang[1])
        user_input()
    elif (user_input.user_search not in words):
        print (lang[2])
        user_input()


read_file()
