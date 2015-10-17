from random import choice

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

customers_and_preferences = {}
def find_preferences():
    preferences = {}
    for type, question in questions.iteritems():
        print question
        preferences[type] = raw_input().lower() in ["y", "yes"]
        print "\n"
    return preferences

def make_drink(preferences):
    drink = []
    for ingredient_type, liked in preferences.iteritems():
        if not liked:
            continue

        drink.append(ingredients[ingredient_type])
        
    return drink


def main():
	customer_count = int(raw_input("Enter the number of customers"))
	for i in range(1,customer_count):
		print i
		print "\n"
		customer = raw_input("Enter your name : \n")
		preferences = find_preferences()
		customers_and_preferences[customer] = make_drink(preferences)
    
main()
print customers_and_preferences