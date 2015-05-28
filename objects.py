""" Objects models file.

    Edit the class definitions to make the tests pass.
"""


class Dessert(object):

    def __init__():
        # Edit me!
        # You need to be able to initialize a Dessert object with arguments:
        # price - required
        # calories - optional

        # This should set the object's price and calories, accessible by
        # .price and .calories respectively.
        pass

    # Add a calories_per_dollar method that returns the calories per dollar
    # for the dessert.

    # Define a method is_a_cake on Dessert that returns False


class Cake(Dessert):

    def __init__():
        # Edit me!
        # Cakes all cost the same amount and have the same calories, so their
        # price and calories can be set at the class-level, not during init.
        # However, we need to be able to tell cakes apart. Accept argument:
        # kind - required

        pass

    # Define a method is_a_cake on Cake that returns True
    # (This will override the one on Dessert)


class Menu(object):

    def __init__(self, items):
        self.items = items

    def desserts(self):
        # Return only the items in self.items which are desserts
        desserts = []
        for item in self.items:
            if isinstance(item, Dessert):
                desserts.append(item)
        return desserts
