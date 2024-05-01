import random

class RecipeMaker():
    
    def __init__(self):
        self.recipes = {} 
        self.load_recipes()  
    
    def load_recipes(self):
        try:
            with open("recipes.txt", "r") as file:
                for line in file:
                    name, ingredients = line.strip().split(":")
                    self.recipes[name] = ingredients.split(", ")
        except FileNotFoundError:
            print("Recipes file not found. Creating a new one.")
    
    def save_recipes(self):
        with open("recipes.txt", "w") as file:
            for name, ingredients in self.recipes.items():
                file.write(f"{name}:{', '.join(ingredients)}\n")
    
    def view(self):
        print("Viewing Recipes:")
        for recipe_name, ingredients in self.recipes.items():
            print(f"{recipe_name}: {', '.join(ingredients)}")
    
    def add_recipe(self, name, ingredients):
        self.recipes[name] = ingredients
        self.save_recipes() #Saves recipe to text file 
        print(f"Recipe '{name}' added successfully!")
    
    def update_recipe(self, name, new_ingredients):
        if name in self.recipes:
            self.recipes[name] = new_ingredients
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
    
    def add_macros(self):
        """This method adds macros to recipes."""
        # Implementation for adding macros
        
    def update_macros(self):
        """This method updates macros."""
        # Implementation for updating macros
        
    def delete_macros(self):
        """This method deletes macros."""
        # Implementation for deleting macros
    
    def random_recipe(self):
        """This method selects a random recipe from the RecipeMaker instance."""
        if self.recipes:
            random_recipe_name = random.choice(list(self.recipes.keys()))
            print(f"Random Recipe: {random_recipe_name}: {', '.join(self.recipes[random_recipe_name])}")
        else:
            print("No recipes available!")

# Display page when program is launched
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

# Convert choice to integer
choice = int(choice)

if choice == 1:
    recipe_maker.view()
elif choice == 2:
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    recipe_maker.add_recipe(name, ingredients)
elif choice == 3:
    name = input("Enter recipe name to update: ")
    new_ingredients = input("Enter new ingredients (comma-separated): ").split(",")
    recipe_maker.update_recipe(name, new_ingredients)
elif choice == 4:
    name = input("Enter recipe name to delete: ")
    recipe_maker.delete_recipe(name)
elif choice == 5:
    recipe_maker.add_macros()
elif choice == 6:
    recipe_maker.update_macros()
elif choice == 7:
    recipe_maker.delete_macros()
elif choice == 8:
    recipe_maker.random_recipe()
else:
    print("Invalid choice!")



