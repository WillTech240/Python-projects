def numbers(*args):
    print(args)
def My_Love_Love_Letter():
    Name1 = input("Enter Senders name: ")
    Name2 = input("Enter Receivers name: ")
    message = input("Enter your message: ")
    print(f'From {Name1}, {message} {Name2}')

My_Love_Love_Letter()
numbers(*range(1, 101) )  
