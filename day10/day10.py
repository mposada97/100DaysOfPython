n1 = float(input("Whats the first number? "))
def calculator(n1):
    operator = input("+ \n- \n* \n/ \nType Operator: ").strip()
    n2 = float(input("Whats the second number? "))
    operation = str(n1) + ' ' + operator + ' ' + str(n2)
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 / n2
    else:
        result = "ERROR"
    return result, operation
while True:
    result = calculator(n1) 
    n1 = result[0]
    operation = result[1]
    print(f"{operation} = {n1}")
    whats_next = input("Type 'yes' to continue calculating with the result, type 'no' for a new calculation, or type 'exit' to exit:").lower()
    if whats_next == 'no':
        n1 = float(input("Whats the first number? "))
    elif whats_next == 'exit':
        break