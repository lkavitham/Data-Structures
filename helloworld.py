class HelloWorld:
    def __init__(self,mes):
        self.mes=mes
    def display(self):
        print(self.mes)

word=HelloWorld("Hello World")
word.display()

