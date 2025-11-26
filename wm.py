class Cloth:
    def __init__(self,name,is_clean = False):
        self.name = name
        self.is_clean = is_clean
    def clean(self):
        self.is_clean = True
 
class WashingMachine:
    def __init__(self,max_capacity=5):
        self.max_capacity = max_capacity
        self.clothes = []
    def add_cloth(self,cloth):
        if (len(self.clothes)>=self.max_capacity):
            print("washing machine it is full")
            return False
        self.clothes.append(cloth)
        print(f"{cloth.name} added to washing machine")
        return True
    def start_wash(self):
        if not self.clothes:
            print("no clothes to wash")
            return
        for cloth in self.clothes:
            cloth.clean()
        print("washing completed")
    def remove_all_clothes(self):
        if not self.clothes:
            print("no clothes to remove")
            return[]
        cleaned = self.clothes.copy()
        self.clothes.clear()#清空列表
        print(f"all clothes removed")
        return cleaned
 
class Person:
    def __init__(self,name):
        self.name = name
    def wash_clothes(self,machine,clothes_list):
        for cloth in clothes_list:
            machine.add_cloth(cloth)
        machine.start_wash()
        cleaned_clothes = machine.remove_all_clothes()
        return cleaned_clothes

if __name__ == "__main__":
    alice = Person("Alice")
    washing_machine = WashingMachine()
    clothes = [Cloth("shirt"),Cloth("pants"),Cloth("dress")]
    cleaned = alice.wash_clothes(washing_machine,clothes)