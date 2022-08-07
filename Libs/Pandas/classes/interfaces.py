class Interface():
    def l(self, value=30):
        print(value*'-')

    def t(self, text, value=25):
        self.l(value*3)
        print(f'{self.space(value)}{text}{self.space(value)}')
        self.l(value*3)

    def space(self, value):
        return ' '*value
