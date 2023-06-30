class WordCounter:

    def __init__(self, sentence ):
        self.sentence = sentence
        self.word_counter = None
        self.shortest_word = None
        self.longest_word = None
    
    def count_words(self):
        words = self.sentence.split()
        self.word_counter = len(words)
        self.shortest_word = min(words, key = len)
        self.longest_word = max(words, key = len)

    
    def get_word_count(self):
         if self.word_counter is None:
            self.count_words()
        
            return self.word_counter

    def get_shortest_word(self):
        if self.shortest_word is None:
             self.count_words()
        return len(self.shortest_word)

    def get_longest_word(self):
         if self.longest_word is None:
             self.count_words() 
         return len(self.longest_word)


 






   