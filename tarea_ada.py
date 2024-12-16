import os
import json

class RecipeManager:
    def __init__(self, data_dir="recetas"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def add_recipe(self, name, ingredients, steps):
        """Add a new recipe."""
        recipe = {
            "name": name,
            "ingredients": ingredients,
            "steps": steps,
        }
        filepath = os.path.join(self.data_dir, f"{name}.json")
        with open(filepath, 'w') as file:
            json.dump(recipe, file, indent=4)
        print(f"Receta '{name}' guardada exitosamente.")

    def view_recipe(self, name):
        """View a recipe by name."""
        filepath = os.path.join(self.data_dir, f"{name}.json")
        if not os.path.exists(filepath):
            print(f"La receta '{name}' no existe.")
            return
        with open(filepath, 'r') as file:
            recipe = json.load(file)
            print(json.dumps(recipe, indent=4))

    def delete_recipe(self, name):
        """Delete a recipe by name."""
        filepath = os.path.join(self.data_dir, f"{name}.json")
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Receta '{name}' eliminada.")
        else:
            print(f"La receta '{name}' no existe.")

    def list_recipes(self):
        """List all recipes."""
        recipes = [f[:-5] for f in os.listdir(self.data_dir) if f.endswith(".json")]
        if recipes:
            print("Recetas disponibles:")
            for recipe in recipes:
                print(f"- {recipe}")
        else:
            print("No hay recetas disponibles.")

    def generate_shopping_list(self, selected_recipes):
        """Generate a shopping list based on selected recipes."""
        shopping_list = {}
        for recipe_name in selected_recipes:
            filepath = os.path.join(self.data_dir, f"{recipe_name}.json")
            if os.path.exists(filepath):
                with open(filepath, 'r') as file:
                    recipe = json.load(file)
                    for ingredient in recipe['ingredients']:
                        name = ingredient['name']
                        quantity = ingredient['quantity']
                        if name in shopping_list:
                            shopping_list[name] += quantity
                        else:
                            shopping_list[name] = quantity
            else:
                print(f"Receta '{recipe_name}' no encontrada.")

        print("Lista de compras generada:")
        for item, quantity in shopping_list.items():
            print(f"- {item}: {quantity}")

# Programa principal
def main():
    manager = RecipeManager()

    while True:
        print("\nGestor de Recetas")
        print("1. Agregar receta")
        print("2. Ver receta")
        print("3. Eliminar receta")
        print("4. Listar recetas")
        print("5. Generar lista de compras")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            name = input("Nombre de la receta: ")
            ingredients = []
            print("Ingrese los ingredientes (deje el nombre vacío para terminar):")
            while True:
                ingredient_name = input("Ingrediente: ")
                if not ingredient_name:
                    break
                # Solicitar la cantidad sin unidades
                try:
                    quantity = float(input(f"Cantidad de {ingredient_name} (solo números, sin unidades): "))
                    # Pedir la unidad como un campo separado
                    unit = input(f"Unidad de {ingredient_name} (ejemplo: kg, g, ml, etc.): ")
                    ingredients.append({"name": ingredient_name, "quantity": quantity, "unit": unit})
                except ValueError:
                    print("Error: ingrese un número válido para la cantidad.")
            steps = input("Pasos de preparación: ")
            manager.add_recipe(name, ingredients, steps)
        elif option == "2":
            name = input("Nombre de la receta a ver: ")
            manager.view_recipe(name)
        elif option == "3":
            name = input("Nombre de la receta a eliminar: ")
            manager.delete_recipe(name)
        elif option == "4":
            manager.list_recipes()
        elif option == "5":
            print("Ingrese los nombres de las recetas para la lista de compras (separadas por comas):")
            selected_recipes = input().split(',')
            selected_recipes = [recipe.strip() for recipe in selected_recipes]
            manager.generate_shopping_list(selected_recipes)
        elif option == "6":
            print("Saliendo del gestor de recetas.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
