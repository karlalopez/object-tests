""" Test file for objects.py.

    When objects.py is complete, this file should completely pass.

    The tests are contained between the # ---  --- # blocks. Code outside
    these blocks is just helper code to run the tests.
"""
import traceback

from objects import *


def check_test(func):
    """ This is a decorator that simply prints out whether the function
        it calls succeeded or not. You don't need to edit this.
    """
    def func_wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print ":) {} passed".format(func.__name__)
        except AssertionError:
            traceback.print_exc()
            print ":( {} failed".format(func.__name__)
    return func_wrapper


# --- THE ACTUAL TESTS FOLLOW --- #

@check_test
def test_object_creation():
    dessert = Dessert(price=10)
    assert dessert.price == 10
    assert dessert.calories is None

    dessert = Dessert(price=10, calories=500)
    assert dessert.price == 10
    assert dessert.calories == 500

    try:
        # Should not create the dessert if price is not supplied.
        price_missing = Dessert()
        successful = True
    except:
        successful = False
    assert not successful


@check_test
def test_object_methods():
    dessert = Dessert(calories=100, price=5)
    value = dessert.calories_per_dollar()
    assert value == 20

    # If we didn't supply calories, the calories_per_dollar should return None
    dessert = Dessert(price=10)
    value = dessert.calories_per_dollar()
    assert value is None


@check_test
def test_object_subclasses():
    # All cakes should cost 5 dollars and have 200 calories
    cake = Cake(kind='red velvet')
    assert cake.price == 5
    assert cake.calories == 200

    assert cake.is_a_cake()

    dessert = Dessert(price=10)
    assert not dessert.is_a_cake()


@check_test
def test_object_relationships():
    # EDIT THIS TEST
    # Look at the Menu class in objects.py.
    # Edit this test to create a Menu with a list of items, and
    # test that the desserts() method does what it is supposed to.
    # NOTE: To test that it really works, you probably want to create a Menu
    # with a list that includes things that *aren't* desserts, like integers.

    assert False  # Take this line out, it forces the test to fail

    # Create a cakes() method that does the same thing.
    # This code is the test for cakes():

    dessert1 = Dessert(price=10)
    dessert2 = Dessert(price=12)
    dessert3 = Dessert(price=13)
    cake1 = Cake(kind='sponge')
    cake2 = Cake(kind='birthday')
    my_desserts = [dessert1, dessert2, dessert3, cake1, cake2]
    my_menu = Menu(my_desserts)
    cakes = my_menu.cakes()
    # There should only be two items in cakes!
    assert len(cakes) == 2
    # The cakes should be sponge and birthday
    assert sorted([c.kind for c in cakes]) == ['birthday', 'sponge']


# --- END OF ACTUAL TESTS --- #

for item in dir():
    """ Loop through all the defined items we know about (functions, etc).
        If the name starts with test_, assume it's a test function and run it!
    """
    if item.startswith('test_'):
        globals()[item]()
