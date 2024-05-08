import pytest 
from recipe_database import RecipeMaker

def test_recipemaker():
    """This is a test function for RecipeMaker
    """

def test_add_recipe(recipe_maker):
    recipe_maker.add_recipe("Pasta", ["pasta", "tomato sauce"])
    assert recipe_maker.recipes == {"Pasta": ["pasta", "tomato sauce"]}

def test_update_recipe(recipe_maker):
    recipe_maker.add_recipe("Pasta", ["pasta", "tomato sauce"])
    recipe_maker.update_recipe("Pasta", ["cheese"])
    assert recipe_maker.recipes == {"Pasta": ["pasta", "tomato sauce", "cheese"]}

def test_delete_recipe(recipe_maker):
    recipe_maker.add_recipe("Pasta", ["pasta", "tomato sauce"])
    recipe_maker.delete_recipe("Pasta")
    assert "Pasta" not in recipe_maker.recipes


def test_view(recipe_maker, capsys):
    recipe_maker.add_recipe("Pasta", ["Pasta", "Tomato Sauce"])

    recipe_maker.view()
    assert "Pasta: Pasta, Tomato Sauce"

def test_random_recipe(recipe_maker, capsys):
    recipe_maker.add_recipe("Pasta", ["Pasta", "Tomato Sauce"])
    recipe_maker.add_recipe("Salad", ["Lettuce", "Tomato", "Cucumber"])

    recipe_maker.random_recipe()
    captured = capsys.readouterr()
    assert captured.out.startswith("Random Recipe:")

def test_load_macros(recipe_maker):
    with open(RecipeMaker.MACROS_FILE, "w") as file:
        file.write("Apple:Carbohydrates, Fiber\nBanana:Carbohydrates, Potassium")

    recipe_maker.load_macros()
    assert recipe_maker.macros == {"Apple": ["Carbohydrates", "Fiber"], "Banana": ["Carbohydrates", "Potassium"]}

def test_save_macros(recipe_maker):
    recipe_maker.macros = {"Apple": ["Carbohydrates", "Fiber"], "Banana": ["Carbohydrates", "Potassium"]}
    
    recipe_maker.save_macros()
    with open(RecipeMaker.MACROS_FILE, "r") as file:
        assert file.read() == "Apple:Carbohydrates, Fiber\nBanana:Carbohydrates, Potassium\n"

def test_view_macros(recipe_maker, capsys):
    recipe_maker.macros = {"Apple": ["Carbohydrates", "Fiber"], "Banana": ["Carbohydrates", "Potassium"]}
    
    recipe_maker.view_macros()
    captured = capsys.readouterr()
    assert "Apple: Carbohydrates, Fiber\nBanana: Carbohydrates, Potassium" in captured.out

def test_add_macros(recipe_maker):
    recipe_maker.add_macros("Orange", ["Vitamin C", "Carbohydrates"])
    assert recipe_maker.macros == {"Orange": ["Vitamin C", "Carbohydrates"]}

def test_update_macros(recipe_maker):
    recipe_maker.macros = {"Apple": ["Carbohydrates", "Fiber"], "Banana": ["Carbohydrates", "Potassium"]}
    recipe_maker.update_macros("Apple", ["Vitamin C"])
    assert recipe_maker.macros == {"Apple": ["Carbohydrates", "Fiber", "Vitamin C"], "Banana": ["Carbohydrates", "Potassium"]}

def test_delete_macros(recipe_maker):
    recipe_maker.macros = {"Apple": ["Carbohydrates", "Fiber"], "Banana": ["Carbohydrates", "Potassium"]}
    recipe_maker.delete_macros("Apple")
    assert recipe_maker.macros == {"Banana": ["Carbohydrates", "Potassium"]}

