# that crazy thing where a method variable persists in memory

'''
Dictionaries and lists have unique properties when used as keyword arguments.

If the function is called without redefining the dictionary or list, then
a unique persistent instance of that dictionary or list will be referenced. This
same instance will be used in subsequent calls of the method that do not
redefine the dictionary or list.

If the function is called and the dictionary or list is redefined, then a separate
effemeral instance of that dictionary or list will be referenced.

This does not hold true for other datatypes.

The variable reference (y in the example below) cannot be called outside of the
scope of the function
'''

def f1(x, y=[]):
    y.append(x)
    print(y)

def f2(x, y={}):
    y[x] = x*x
    print(y)

if __name__  == '__main__':
    # list example
    f1('0')
    f1('z', y=['a', 'b'])
    f1('1')

    # dictionary example
    f2(2)
    f2(2, y={'a': 0, 'b': 1})
    f2(3)
