class Recipe(object):
    
    def __init__(self, **kwargs):
        """Initializes a recipe, as in Recipe(onions=200, salt=10)"""
        # *kwargs is a dictionary of name=value, and we use it to initialize
        # the dictionary self.ingredients. 
        for v in kwargs.values():
            assert v > 0
        self.ingredients = dict(kwargs)
        
    def __repr__(self):
        """Used to print a Recipe."""
        return str(self.ingredients)

class Cupboard(object):
    def __init__(self, **kwargs):
        for v in kwargs.values():
            assert v >= 0
        self.ingredients = dict(kwargs)
        
    def __repr__(self):
        return str(self.ingredients)
    
    def buy(self, new_ingredient, quantity):
        """adds to the cupboard the given quantity of the new ingredient"""
        # YOUR CODE HERE
        # 1. check if new_ingredient is in the cupboard
        # 2. If it is, we update the value
        # 3. If it isn't, then we add the key and the value
        if new_ingredient in self.ingredients:
            self.ingredients[new_ingredient] += quantity
        else:
            self.ingredients[new_ingredient] = quantity

    def howmany(self, recipe):
        """returns the integer n, representing the maximum number 
        of persons for which we can cook the given recipe"""
        # YOUR CODE HERE
        numbers = []
        
        for ingredient, quantity in recipe.ingredients.items():
            if ingredient in self.ingredients:
                number = self.ingredients[ingredient] // quantity
                numbers.append(number)
            else:
                return 0
        return min(numbers)

        
    def cook(self, n, recipe):
        """cooks `n` servings of `recipe`, subtracting from the cupboard 
        the ingredients used to cook them.  If more of an ingredient is 
        required than is available, it should raise the `ValueError` 
        exception _and leave the Cupboard unchanged_"""
        # YOUR CODE HERE
        howmany = self.howmany(recipe)
        if howmany < n:
            raise ValueError
        for ingredient, quantity in recipe.ingredients.items():
            self.ingredients[ingredient] -= n * quantity


c = Cupboard(onion=100, celery=100)
c.buy('onion', 50)

assert c.ingredients['celery'] == 100
assert c.ingredients['onion'] == 150

c = Cupboard(onion=100, celery=100, rice=500, oil=400)
r = Recipe(onion=15, celery=18, oil=25)
c.cook(2, r)
assert c.ingredients["onion"] == 70
assert c.ingredients["celery"] == 64
assert c.ingredients["rice"] == 500
assert c.ingredients["oil"] == 350