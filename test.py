def hello_world(self):
    print(str(hello_world.__name__.split('_')).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ').replace('_', ' ').title() + '!')


hello_world(print)