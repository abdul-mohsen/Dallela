from adapt.engine import IntentDeterminationEngine
from Tasks.task_manager.adapt_intents import entities, multi_regex_entities, intents
from Tasks.task_manager import Handler

engine = IntentDeterminationEngine()


# Register entities on engine
for entity, keywords in entities.items():
    for keyword in keywords:
        engine.register_entity(keyword, entity)

for entity in multi_regex_entities:
    for regex in entity:
        engine.register_regex_entity(regex)

# Register intents on engine
for intent in intents:
    engine.register_intent_parser(intent)


text1= 'Add task get milk from store'
text2= 'create assignment buy mic for john'


for intent in engine.determine_intent(text1):
	print (intent)

for intent in engine.determine_intent(text2):
	print (intent)


def f1():
	print(' i am connecting todo')

h1 = Handler.Handler(intents[0], f1)


h1.compute()  #
