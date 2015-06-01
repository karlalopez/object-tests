""" Objects models file.

    Edit the class definitions to make the tests pass.
"""


class Dessert(object):
    def __init__(self,price,calories=None):
        # Edit me!
        # You need to be able to initialize a Dessert object with arguments:
        # price - required
        # calories - optional
        self.price = price
        self.calories = calories
        # This should set the object's price and calories, accessible by
        # .price and .calories respectively.

    # Add a calories_per_dollar method that returns the calories per dollar
    # for the dessert.
    def calories_per_dollar(self):
        if self.calories == None:
            return None
        else:
            ratio = self.calories/self.price
            return ratio
    # Define a method is_a_cake on Dessert that returns False
    def is_a_cake(self):
        return False




class Cake(Dessert):
    def __init__(self,kind):
        # Edit me!
        # Cakes all cost the same amount and have the same calories, so their
        # price and calories can be set at the class-level, not during init.
        # However, we need to be able to tell cakes apart. Accept argument:
        # kind - required
        self.kind = kind
        price = 5
        calories = 200
        super(Cake,self).__init__(price,calories)
    # Define a method is_a_cake on Cake that returns True
    # (This will override the one on Dessert)
    def is_a_cake(self):
        return True



class Menu(object):
    def __init__(self, items):
        self.items = items

    def desserts(self):
        # Return only the items in self.items which are desserts
        desserts = []
        for item in self.items:
            if isinstance(item, Dessert): ## I don't really understand what's going on here, Jennie
                desserts.append(item)
        return desserts

    def cakes(self):
        # Return only the items in self.items which are cakes
        cakes = []
        for item in self.items:
            if isinstance(item, Cake):
                cakes.append(item)
        return cakes
