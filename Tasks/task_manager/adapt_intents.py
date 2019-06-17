from adapt.intent import IntentBuilder

add_keywords = [ # list of key words
    'create',
    'add',
    'new',
    'make'
]

todo_keywords = [
    'todo',
    'todos',
    'task',
    'tasks',
    'chore',
    'chores',
    'errand',
    'errands',
    'assignment',
    'assignments'
]

todo_regex_keywords = ['{} (?P<Todo>.*)'.format(keyword)
                       for keyword in todo_keywords]

add_todo_intent = IntentBuilder('AddTodoIntent')\
    .require('AddKeyword')\
    .require('TodoKeyword')\
    .require('Todo')\
    .build()


entities = {  # making a dic for entities
  'AddKeyword': add_keywords,
  'TodoKeyword': todo_keywords
}
multi_regex_entities = [todo_regex_keywords]

intents = [add_todo_intent]  # adding intent to a new list


