from json import load, dump

# usar arquivo json
# inserindo e pegando dados em um json

#json.loads e json.dumps são para string

class Veiculo():
    def __init__(self, locale):
        self.locale = f"{locale}/veiculos.json"
        self.veiculos = {}
        self.check_file()

    def check_file(self):
        try:
            with open(self.locale, "r", encoding='utf-8') as file_json:
                self.veiculos = load(file_json)
        except: 
            with open(self.locale, "w", encoding='utf-8') as file_json:
                file_json.write("{\n\n}")
            self.check_file()

    def update_json(self):
        with open(self.locale, "w", encoding='utf-8') as json_file:
            dump(self.veiculos, json_file)
    
    def add_car(self, key, value):
        self.veiculos[key] = { "marca":f"{value[0]}"
                            ,"modelo":f"{value[1]}"
                            ,"cor":f"{value[2]}"}

    def add_cars(self, news_cars):
        for key, value in news_cars.items():
            self.add_car(key, value)
            
    def status(self, var=''):
        print(f"\n {10*'-'} Status {var}")
        for x in self.veiculos.items():
            print(x)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
    


