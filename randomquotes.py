
	
def quote_generator():
	import random
	quotes = ["If life were predictable, it would cease to be life, and be without flavor. — Eleanor Roosevelt",
	"Life is like riding a bicycle. To keep your balance, you must keep moving. — Albert Einstein","Nothing can dim the light that shines from within. — Maya Angelou", "The big lesson in life is never be scared of anyone or anything. — Frank Sinatra",
	"You get in life what you have the courage to ask for. — Oprah Winfrey",
	"What the superior man seeks is in himself; what the small man seeks is in others. Confucius",
	"Let go, or be dragged. ", 
	"Good is not enough. You’ve got to be great. — Simon Cowell", 
	"Rise above the storm, and you will find the sunshine. — Mario Fernandez",
	"You only live once, but if you do it right, once is enough. — Mae West"]
	randomQuote = quotes[random.randrange(0,len(quotes))]
	print("\n\n\t\t**********************************************************************************************\n")
	print("\t\t" + randomQuote)
	print("\n\n\t\t**********************************************************************************************\n\n\n")

def welcome():
	print("\t\t\t\tWelcome to Random Love Quotes generator")
	print("\t\t\t\t***********************************************")
	print("\t\t\t\tEnter 1 to generate a quote or 0 to exit\n\n")
	userInput= input("\t\t\t\t\t\tEnter 1 or 0\n\n")
	if userInput=='1':
		quote_generator()
		welcome()
	elif userInput=='0':
		exit()
	else:
		print("\t\t\t\tEnter 1 or 0\n\n\n")
		welcome()
		
welcome()

