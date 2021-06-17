#Chatbot using python please read the readme.md for more info.


# import pyfiglet module
import pyfiglet
import chatterbot
# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response

# Inport ListTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
#importing for theatrics
import time
import os

# Create object of ChatBot class
bot = ChatBot('Chatter')

bot = ChatBot(
    'Chatter',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    response_selection_method=get_most_frequent_response,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.UnitConversion',
    {
        "import_path": "chatterbot.logic.BestMatch",
        "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
        "default_response": 'I am sorry, but I do not understand.',
        "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
        "response_selection_method": "chatterbot.response_selection.get_first_response",
        'maximum_similarity_threshold': 0.90
    }
    ]
        
    
)

# Create a new trainer for the chatbot
trainer2 = ChatterBotCorpusTrainer(bot)

# Train based on the english corpus
trainer2.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer2.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer2.train("chatterbot.corpus.english.conversations")

print("connecting with sqlite...")
print("generating responses...")
print("ai modal trained with data..")

if os.name == 'posix':
    _ = os.system('clear')
else:
    # for windows platfrom
    _ = os.system('cls')

#starting
print("starting.../")
time.sleep(1)

# theatrics
result = pyfiglet.figlet_format("ChatterBot", font = "slant"  )
print(result)

name=input("Enter Your Name: ")
print("Welcome to the ChatterBot! this is liza how can i help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)


