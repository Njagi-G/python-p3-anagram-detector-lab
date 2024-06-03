# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word
        self.each_letter = sorted([letter for letter in word])
        # self.each_letter = sorted(word)
        
    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            # if sorted(word) == self.each_letter:
            if sorted([letter for letter in word]) == self.each_letter:
                match_word_list.append(word)
            
        return match_word_list


listen = Anagram("listen")
check_listen = listen.match(["enlists", "google", "inlets", "banana"])
print(check_listen)

deer = Anagram("deer")
check_deer = deer.match(["reach", "yahoo", "reed", "crazy"])
print(check_deer)









    
