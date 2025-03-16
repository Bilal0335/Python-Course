JOKE = """Here is a joke for you! 
Panaversity GPT - Sophia is heading out to the grocery store. 
A programmer tells her: get a liter of milk, and if they have eggs, get 12. 
Sophia returns with 13 liters of milk. 
The programmer asks why and Sophia replies: 'because they had eggs'."""

PROMPT = "What do you want? "
SORRY = "Sorry I only tell jokes"

def bot_chat():
  user_input = input(PROMPT)
  if 'joke' in user_input:
    print(JOKE)
  else:
    print(SORRY)

bot_chat()