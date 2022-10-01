# can handle zero division using decorator
def Div_by_zero(func):
    def inner(x, y):
        return "Quantity is zero" if y == 0 else func(x, y)

    return inner


@Div_by_zero
def Unitprice(Amount, Quantity):
    return Amount / Quantity


# Main Program
if __name__ == '__main__':
    print(Unitprice(500, 0))
