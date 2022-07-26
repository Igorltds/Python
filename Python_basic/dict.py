class Carro():
    def __init__(self):
        self.carro={                #Dict
            "marca":"honda",
            "modelo":"hrv", 
            "cor":"prata"
            }
    def print_all_keys(self):               #Keys
        print("\nKeys: ")
        for x in self.carro:
            print(x)

    def print_all_values(self):             #Values
        print("\nValues: ")
        for x in self.carro.values():
            print(x)
    
    def print_all_items(self):              #Items
        print("\nItems: ")
        for x in self.carro.items():
            print(x)
    
    def print_all_items_clean(self):            #Clean Items
        print("\nItems clean: ")
        for a, b in self.carro.items():
            print(a, b)

carro_001 = Carro()
carro_001.print_all_keys()
carro_001.print_all_values()
carro_001.print_all_items()
carro_001.print_all_items_clean()

