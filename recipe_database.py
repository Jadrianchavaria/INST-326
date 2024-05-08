"""This script serves as a recipe database manager for a user. """
import random

class RecipeMaker():
    """RecipeMaker class to manage recipes and macros."""
    
    def __init__(self):
        """ 
        Initializes RecipeMaker object
        Initializes recipe dictionary
        Initializes macros dictionary
        calls load recipe/macros methods
        """
        self.recipes = {} 
        self.load_recipes()
        self.macros = {}
        self.load_macros()  
    
    def load_recipes(self):
        """  
        Creates recipes text file.
        Formats the recipes in the text file.
        Loads recipes from file.
        """
        try:
            with open("recipes.txt", "r") as file:
                for line in file:
                    name, ingredients = line.strip().split(":")
                    self.recipes[name] = ingredients.split(", ")
        except FileNotFoundError:
            print("Recipes file not found. Creating a new one.")
    
    def save_recipes(self):
        """
        Opens text file
        Saves recipes to file.
        Opens text file
        Saves recipes to that file. """
        with open("recipes.txt", "w") as file:
            for name, ingredients in self.recipes.items():
                file.write(f"{name}:{', '.join(ingredients)}\n")
    
    def view(self):
        """Displays all the recipes. 
        """
        print("Viewing Recipes:")
        for recipe_name, ingredients in self.recipes.items():
            print(f"{recipe_name}: {', '.join(ingredients)}")
        pass
    
    def add_recipe(self, name, ingredients):
        """Adds a new recipe to file.

        Args:
            name (str): the name of the recipe 
            ingredients (list): list of ingredients for the recipe. 
        """
        self.recipes[name] = ingredients
        self.save_recipes() 
        print(f"Recipe '{name}' added successfully!")


    def update_recipe(self, name, new_ingredients):
        """Updates an existing recipe by adding new ingredients.
        
        Parameters:
        - name (str): The name of the recipe to update.
        - new_ingredients (list): List of new ingredients to add to the recipe.
        """
        if name in self.recipes:
            self.recipes[name] = new_ingredients
            self.save_recipes()  
            print(f"Recipe '{name}' updated successfully!")
        else:
            print(f"Recipe '{name}' not found!")

    def delete_recipe(self, name):
        """ 
        Deletes a recipe.
        
        Parameters:
        - name (str): The name of the recipe to delete.
        """
        if name in self.recipes:
            del self.recipes[name]
            self.save_recipes()  
            print(f"Recipe '{name}' deleted successfully!")
        else:
            print(f"Recipe '{name}' not found!")

    def random_recipe(self):
        """Generates a random recipe 
        """
        
        if self.recipes:
            random_recipe_name = random.choice(list(self.recipes.keys()))
            print(f"Random Recipe: {random_recipe_name}: {', '.join(self.recipes[random_recipe_name])}")
        else:
            print("No recipes available!")
      

    def load_macros(self):
        """Creates macros text file.
        Formats the macros in the text file.
        Loads macros from file.
        """
        try: 
            with open("macros.txt", r) as file:
                for line in file:
                    name, new_macros = line.strip().split(":")
                    self.macros[name] = new_macros.split(", ")
        except FileNotFoundError:
                print("Macros file not found. Create a new one")

    def save_macros(self):
        """ 
        opens text file
        Saves macros to file.
        """
        with open("macros.txt", "w") as file:
            for name, new_macros in self.macros.itemss():
                file.write(f"{name}:{','}.join(new_macros)\n")

    def view_macros(self):
        """Displays all macros"""

        print("Viewing Macros")
        for macros_name, new_macros in self.macros.items():
            print(f"{macros_name}: {','.join(new_macros)}")
    
    def add_macros(self, name, new_macros):
        """   
        Adds new macros for a food item.
        
        Parameters:
        - name (str): The name of the food item.
        - new_macros (list): List of macros for the food item.
        """
        self.macros[name]= new_macros
        self.save_recipes()
        print(f"Macros '{name}' added successfully!")

    def update_macros(self, name, new_macros):
        """   
        Updates macros for a food item.
        
        Parameters:
        - name (str): The name of the food item.
        - new_macros (list): List of new macros for the food item.
        """
        if name in self.macros:
            self.macros[name] = new_macros 
            self.save_macros()
            print(f"Macros '{name}' updated successfully!")
        else:
            print(f"Macros '{name}' not found!")

    def delete_macros(self, name):
        """  
        Deletes macros for a food item.
        
        Parameters:
        - name (str): The name of the food item.
        """
        if name in self.macros:
            del self.macros[name]
            self.save_macros()
            print(f"Macros '{name}' deleted successfully!")
        else: 
            print(f"Macros '{name}' not found!")

recipe_maker = RecipeMaker()
print("\tRecipe Maker is a database created to archive recipes.")
print("\tPlease input the number that corresponds to the action\n\n")
print("\t\t\t\t  1: View Recipes\n")
print("\t\t2: Add Recipe \t\t\t\t5: Add Macros\n")
print("\t\t3: Update Recipe \t\t\t6: Update Macros\n")
print("\t\t4: Delete Recipe \t\t\t7: Delete Macros\n")
print("\t\t\t\t8: Pick Random Recipe\n")
print("\t\t2: Add Recipe \t\t\t\t5: View Macros\n")
print("\t\t3: Update Recipe \t\t\t6: Add Macros\n")
print("\t\t4: Delete Recipe \t\t\t7: update Macros\n")
print("\t\t8: Delete Macros \t\t\t9: Random Recipe\n")

choice = input("Enter your choice: ")

if choice == 1:
    if choice == '1':
        recipe_maker.view()
elif choice == '2':
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    recipe_maker.add_recipe(name, ingredients)
elif choice == '3':
    name = input("Enter recipe name to update: ")
    new_ingredients = input("Enter new ingredients (comma-separated): ").split(",")
    recipe_maker.update_recipe(name, new_ingredients)
elif choice == '4':
    name = input("Enter recipe name to delete: ")
    recipe_maker.delete_recipe(name)
elif choice == '5':
    recipe_maker.add_macros()
elif choice == '6':
    recipe_maker.update_macros()
elif choice == '7':
    recipe_maker.delete_macros()
elif choice == '8':
    recipe_maker.random_recipe()
else:
    print("Invalid choice!")
  





 
   

   
    
  


 



