def math_operations(a, b):
    """
    This function takes two numbers as input and returns their sum and product.
    It uses lambda functions to perform the calculations.
    """
    # Lambda function to calculate the sum
    sum_result = (lambda x, y: x + y)(a, b)
    
    # Lambda function to calculate the product
    product_result = (lambda x, y: x * y)(a, b)
    
    return sum_result, product_result

def main():
    # Get input from the user and convert to integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Call math_operations with user inputs
    sum_result, product_result = math_operations(num1, num2)
    
    # Print the results
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

# Call the main function
if __name__ == "__main__":
    main()
