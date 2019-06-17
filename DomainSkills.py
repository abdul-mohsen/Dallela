from padatious import IntentContainer

container = IntentContainer('intent_cache')

container.load_intent('rigLocator', 'rigLocator.intent')
container.load_intent('activeJobs', 'activeJobs.intent')
container.train()

print(container.calc_intent('What is the closest rig in 5 km ?'))
print(container.calc_intent('What is the active jobs ?'))
print(container.calc_intent('What is the active rigs ?'))

print(container.calc_intent('What is the number of active jobs ?'))
print(container.calc_intent('What is the asdfsadf of active rigs ?'))
