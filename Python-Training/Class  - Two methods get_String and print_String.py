class upper:
    def __init__(self):
        self.strn = ''
    def get_String(self):
        self.strn = input('Enter your String : ')
        print('Your string before conversion : {}'.format(self.strn))
    def print_String(self):
        print('Your string before conversion : {}'.format(self.strn.upper()))

str1 = upper()
str1.get_String()
str1.print_String()