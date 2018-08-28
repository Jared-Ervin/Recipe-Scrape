class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.data = {
            "name": name,
            "properties": {},
            "ingredients": self.ingredients
        }

    def insert_image(self, image):
        """
        Inserts a string containg a path to an image into
        the recipe's properties.
        """
        self.image: str = image
        if isinstance(image, (str)):
            self.data["properties"]["image"] = image
        else:
            print("Invalid image location")

    def insert_description(self, description):
        """
        Inserts a string containing the description of the recipe into
        the recipe's properties
        """
        self.description: str = description
        if isinstance(description, (str)):
            self.data["properties"]["description"] = description
        else:
            print("Invalid description")

    def insert_prep(self, prep):
        """
        Inserts a float containg the preperation time of
        the recipe into the recipe's properties.
        """
        self.prep: float = prep
        if isinstance(prep, (float)):
            self.data["properties"]["prep"] = prep
        else:
            print("Invalid prep time")

    def insert_cook(self, cook):
        """
        Inserts a float containing the cook time of the recipe into the
        recipe's properties.
        """
        self.cook: float = cook
        if isinstance(cook, (float)):
            self.data["properties"]["cook"] = cook
        else:
            print("Invalid cook time")

    def add_ingredient(self, ingredient):
        """
        Accepts either a single ingredient in the form of
        a string or a list containing multiple ingredients and appends
        it to the recipe's list of ingredients.
        """
        if isinstance(ingredient, (str)):
            self.ingredients.append(ingredient)
        elif isinstance(ingredient, (list)):
            for x in ingredient:
                self.ingredients.append(x)
        else:
            print("Invalid ingredient type")

    def add_properties(self, proplist):
        """
        Accepts a list of properties in the order
        (image, description, prep-time, cook-time)
        and updates the recipe's properties
        """
        self.insert_image(proplist[0])
        self.insert_description(proplist[1])
        self.insert_prep(proplist[2])
        self.insert_cook(proplist[3])

    def populate(self, proplist=None, ingredientlist=None, remap=None):
        """
        Accepts a list of properties and a list of ingredients
        in the form (image, description, prep-time, cook-time),
        (ingredient 1, ingredient 2, etc.).

        Alternativley accepts a dictonary in for mapping to the class
        """
        if isinstance(proplist, (list)) and isinstance(ingredientlist, (list)):
            self.add_properties(proplist)
            self.add_ingredient(ingredientlist)
        elif isinstance(remap, (dict)):
            self.data["name"] = remap["name"]
            self.data["properties"] = remap["properties"]
            self.data["ingredients"] = remap["ingredients"]
