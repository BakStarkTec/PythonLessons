#  return arguments
#  1, 2, 3, 4, 5, 6  => 2, 4, 6, 1, 2, 3,
# *args, **kwargs keyword arguments
#  generators and decorators



def sum_number(*numbers):
    total = 0
    for i in numbers:
        total += i
    print(total)


def print_something(**kwargs):
    print(kwargs['name'])



#print_something(n1=2, description="This is a function that use kwargs")


def simple_example(x, y):
    print(f'this is x value: {x}')
    print(f'this is y value: {y}')

#  simple_example(y=24, x=23)


def getTupleItem(tup, index):
    try:
        return tup[index]
    except IndexError:
        return None



def use_both(*args, **kwargs):
    print(f'i eat {getTupleItem(args, 3)} {kwargs.get("food")}')


use_both(4, 2, 5, name='salim', description='dlfklkdjg',  age=20)
