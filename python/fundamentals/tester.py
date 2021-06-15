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
        self.new_ingredient = 
        self.quantity = quantity

    def howmany(self, recipe):
        """returns the integer n, representing the maximum number 
        of persons for which we can cook the given recipe"""
        # YOUR CODE HERE
        
    def cook(self, n, recipe):
        """cooks `n` servings of `recipe`, subtracting from the cupboard 
        the ingredients used to cook them.  If more of an ingredient is 
        required than is available, it should raise the `ValueError` 
        exception _and leave the Cupboard unchanged_"""
        # YOUR CODE HERE