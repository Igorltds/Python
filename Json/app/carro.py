from json import dumps, loads

class Carro():
    def __init__(self, marca, modelo, cor):
        self.carro_dic={"marca":marca,
                        "modelo":modelo,
                        "cor":cor}
        self.carro_json=dumps(self.carro_dic) # Convertendo para Json #string
        self.carro_dic=loads(self.carro_json) # Convertendo para dicionário #string
 
    def print_all_keys(self):               #Keys
        print("\nKeys: ")
        for x in self.carro_dic:
            print(x)

    def print_all_values(self):             #Values
        print("\nValues: ")
        for x in self.carro_dic.values():
            print(x)
    
    def print_all_items(self):              #Items
        print("\nItems: ")
        for x in self.carro_dic.items():
            print(x)
    
    def print_all_items_clean(self):            #Clean Items
        print("\nItems clean: ")
        for a, b in self.carro_dic.items():
            print(a, b)




def main1():
    main = Carro("honda", "hrv", "prata")

        # Prints
    main.print_all_keys()
    main.print_all_values()
    main.print_all_items()
    main.print_all_items_clean()