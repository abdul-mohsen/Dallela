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

print (todo_regex_keywords)