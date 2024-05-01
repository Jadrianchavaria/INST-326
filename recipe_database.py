import random
class RecipeMaker():
    
    def __init__(self):
        self.recipes = {} 
        pass
    
    def view(self):
        """
        This method prints all recipes stored in the RecipeMaker instance along with their ingredients.

    Args:
        self: The RecipeMaker instance itself.

        """
        print("Viewing Recipes:")
        for recipe_name, ingredients in self.recipes.items():
            print(f"{recipe_name}: {', '.join(ingredients)}")
        pass
    
    def add_recipe(self, name, ingredients):
        """This method adds a new recipe to the RecipeMaker instance with the 
        specified name and ingredients.

        Args:
            name (str): The name of the recipe to be added.
            ingredients (list of str): The list of ingredients for the recipe. 
        """
        self.recipes[name] = ingredients
        print(f"Recipe '{name}' added successfully!")
        #make text file with all recipies 
        #method will open file 
        #open file, 'w', create tuple with all recipies
        pass
    
    def update_recipie(self, name, new_ingredients):
        """_summary_

        Args:
            name (_type_): _description_
            new_ingredients (_type_): _description_
        """
        if name in self.recipes:
            self.recipes[name] = new_ingredients
            print(f"Recipe '{name}' updated successfully!")
        else:
            print(f"Recipe '{name}' not found!")
        #calls file and adds recipies 
        pass
    
    def delete_recipe(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe '{name}' deleted successfully!")
        else:
            print(f"Recipe '{name}' not found!")
        pass
    
    def add_macros(self):
        """_summary_
        """
        #make text file with macros
        #method will open file 
        #open file, 'w', create tuple with all recipies
        pass
    
    def update_macros(self):
        """_summary_
        """
        pass
    
    def delete_macros(self):
        """_summary_
        """
        pass
    
    def random_recipie(self):
        if self.recipes:
            random_recipe_name = random.choice(list(self.recipes.keys()))
            print(f"Random Recipe: {random_recipe_name}: {', '.join(self.recipes[random_recipe_name])}")
        else:
            print("No recipes available!")
        pass

# Display page when program is launched (rough draft - feel free to change)
recipe_maker = RecipeMaker()  

print("\n\t\t\tWelcome to Recipe Maker\t\t\t\n")
print("\tRecipe Maker is a database created to archive recipes.")
print("\tPlease input the number that corresponds to the action\n\n")
print("\t\t\t\t  1: View Recipes\n")
print("\t\t2: Add Recipe \t\t\t\t5: Add Macros\n")
print("\t\t3: Update Recipe \t\t\t6: Update Macros\n")
print("\t\t4: Delete Recipe \t\t\t7: Delete Macros\n")
print("\t\t\t\t8: Pick Random Recipe\n")

# Getting user input 

choice = input("Enter your choice: ")
choice = int(choice)

if choice == 1:
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


