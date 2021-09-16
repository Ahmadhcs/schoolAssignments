class AlphabetRange:
    def __init__(self, *args):
        self.args = args
        if len(self.args) ==3:
            print(self.args[0]+ "-"+self.args[1]+", "+ str(self.args[2]))
            self.start = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]

        elif len(self.args) ==2:
            print(self.args[0]+ "-"+self.args[1]+", "+ "1")
            self.start = self.args[0]
            self.end = self.args[1]
            self.step = 1
        else:
            print("A" + "-" + self.args[0] + ", " + "1")
            self.start = "A"
            self.step = 1
            self.end = self.args[0]
        self.current = ord(self.end) - ord(self.start)
        self.starting = ord(self.start)



    def __iter__(self):
        return self

    def __next__(self):
        ret = self.starting

        if self.current <= 0:
            raise StopIteration

        if self.step != 1:
            self.current -= self.step
            self.starting += self.step
            return chr(ret)

        self.current -=1
        self.starting +=1


        return chr(ret)






if __name__ == '__main__':
    letters = AlphabetRange('K')
    #print(letters)
    for letter in letters:
       print(letter)

   # letters = AlphabetRange('E', 'B')
   # print(letters)
   # for letter in letters:
      #  print(letter)


