def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return (value1 + value2)
        case '-':
            return (value1 - value2)
        case '*':
            return (value1 * value2)
        case '/':
            return (value1 / value2)
​
​
def main():
    operator, value1, value2 = "", "", ""
    while (bool):
        operator = input("Enter a math operator (i.e.: +, -, *, /):")
        value1 = input("Enter a positive integer: ")
        value2 = input("Enter a positive integer: ")
        if ( operator not in ['+','-','*','/'] ):
            if ( value1 <= 0 ):
                if ( value2 <= 0 ):
                    bool = false
                else:
                    bool = true
    myResult = basic_op(operator, value1, value2)
    print(f"MyResult is: {myResult}")
​
if __name__ == "__main__":
    import sys
    sys.exit(main())