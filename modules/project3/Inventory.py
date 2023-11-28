class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_bike(self, brand, model, quantity):
        if brand not in self.inventory:
            self.inventory[brand] = {}
        if model not in self.inventory[brand]:
            self.inventory[brand][model] = quantity
        else:
            self.inventory[brand][model] += quantity

    def purchase_bike(self, brand, model):
        if brand in self.inventory and model in self.inventory[brand] and self.inventory[brand][model] > 0:
            self.inventory[brand][model] -= 1
            return True
        return False

    def get_available_quantity(self, brand, model):
        if brand in self.inventory and model in self.inventory[brand]:
            return self.inventory[brand][model]
        return 0

    def get_available_models(self, brand):
        if brand in self.inventory:
            return list(self.inventory[brand].keys())
        return []

    def get_available_brands(self):
        return list(self.inventory.keys())
