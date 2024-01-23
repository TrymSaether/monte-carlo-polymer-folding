def hello_world(self):
    return(self(str(hello_world.__name__.split('_')).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ').replace('_', ' ').title() + '!'))


hello_world(print)