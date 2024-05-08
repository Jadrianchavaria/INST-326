import random
import os

class RecipeMaker():
    RECIPES_FILE = "recipes.txt"
    MACROS_FILE = "macros.txt"

    def __init__(self):
        self.recipes = {}
        self.macros = {}
        self.load_recipes()
        self.load_macros()

    def load_recipes(self):
        try:
            with open(self.RECIPES_FILE, "r") as file:
                for line in file:
                    name, ingredients = line.strip().split(":")
                    self.recipes[name] = ingredients.split(", ")
        except FileNotFoundError:
            print("Recipes file not found. Creating a new one.")

    def save_recipes(self):
        with open(self.RECIPES_FILE, "w") as file:
            for name, ingredients in self.recipes.items():
                file.write(f"{name}:{', '.join(ingredients)}\n")

    def view(self):
        if self.recipes:
            print("Viewing Recipes:")
            for recipe_name, ingredients in self.recipes.items():
                print(f"{recipe_name}: {', '.join(ingredients)}")
        else:
            print("No recipes available!")

    def add_recipe(self, name, ingredients):
        self.recipes[name] = ingredients
        self.save_recipes()
        print(f"Recipe '{name}' added successfully!")

    def update_recipe(self, name, new_ingredients):
        if name in self.recipes:
            self.recipes[name] += new_ingredients
            self.save_recipes()
            print(f"Recipe '{name}' updated successfully!")
        else:
            print(f"Recipe '{name}' not found!")

    def delete_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            self.save_recipes()
            print(f"Recipe '{name}' deleted successfully!")
        else:
            print(f"Recipe '{name}' not found!")

    def random_recipe(self):
        if self.recipes:
            random_recipe_name = random.choice(list(self.recipes.keys()))
            print(f"Random Recipe: {random_recipe_name}: {', '.join(self.recipes[random_recipe_name])}")
        else:
            print("No recipes available!")

    def load_macros(self):
        try:
            with open(self.MACROS_FILE, "r") as file:
                for line in file:
                    name, new_macros = line.strip().split(":")
                    self.macros[name] = new_macros.split(", ")
        except FileNotFoundError:
            print("Macros file not found. Creating a new one.")

    def save_macros(self):
        with open(self.MACROS_FILE, "w") as file:
            for name, new_macros in self.macros.items():
                file.write(f"{name}:{', '.join(new_macros)}\n")

    def view_macros(self):
        if self.macros:
            print("Viewing Macros:")
            for macros_name, new_macros in self.macros.items():
                print(f"{macros_name}: {', '.join(new_macros)}")
        else:
            print("No macros available!")

    def add_macros(self, name, new_macros):
        self.macros[name] = new_macros
        self.save_macros()
        print(f"Macros '{name}' added successfully!")

    def update_macros(self, name, new_macros):
        if name in self.macros:
            self.macros[name] += new_macros
            self.save_macros()
            print(f"Macros '{name}' updated successfully!")
        else:
            print(f"Macros '{name}' not found!")

    def delete_macros(self, name):
        if name in self.macros:
            del self.macros[name]
            self.save_macros()
            print(f"Macros '{name}' deleted successfully!")
        else:
            print(f"Macros '{name}' not found!")


def display_menu():
    print("\n\t\t\tWelcome to Recipe Maker\t\t\t\n")
    print("\tRecipe Maker is a database created to archive recipes and macros.")
    print("\tPlease input the number that corresponds to the action\n\n")
    print("\t\t1: View Recipes \t\t\t5: View Macros\n")
    print("\t\t2: Add Recipe \t\t\t\t6: Add Macros\n")
    print("\t\t3: Update Recipe \t\t\t7: Update Macros\n")
    print("\t\t4: Delete Recipe \t\t\t8: Delete Macros\n")
    print("\t\t\t\t   9: Random Recipe\n")
    print("\t\t\t\t   0: Exit\n")


def main():
    recipe_maker = RecipeMaker()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting Recipe Maker. Goodbye!")
            break

        elif choice == "1":
            recipe_maker.view()
        elif choice == "2":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            recipe_maker.add_recipe(name, ingredients)
        elif choice == "3":
            name = input("Enter recipe name to update: ")
            new_ingredients = input("Enter new ingredients (comma-separated): ").split(",")
            recipe_maker.update_recipe(name, new_ingredients)
        elif choice == "4":
            name = input("Enter recipe name to delete: ")
            recipe_maker.delete_recipe(name)
        elif choice == "5":
            recipe_maker.view_macros()
        elif choice == "6":
            name = input("Enter food item name: ")
            new_macros = input("Enter macros (comma-separated): ").split(",")
            recipe_maker.add_macros(name, new_macros)
        elif choice == "7":
            name = input("Enter food item name to update: ")
            new_macros = input("Enter new macros (comma-separated): ").split(",")
            recipe_maker.update_macros(name, new_macros)
        elif choice == "8":
            name = input("Enter food item name to delete macros: ")
            recipe_maker.delete_macros(name)
        elif choice == "9":
            recipe_maker.random_recipe()
        else:
            print("Invalid choice! Please enter a number between 0 and 9.")


if __name__ == "__main__":
    main()




