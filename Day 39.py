def gray_to_binary(gray_str):
    """""
    Function to convert a Gray Code to its equivalent Binary Code.
    :param gray_str: The input Gray Code string.
    :return: The converted Binary Code string.|
    """""
    binary_code = gray_str[0]

    for i in range(1, len(gray_str)):
        binary_bit = str(int(binary_code[i - 1]) ^ int(gray_str[i]))
        binary_code += binary_bit # Append the calculated bit
    return binary_code

if __name__ == "__main__":
    gray_input = input("Enter a Gray Code to convert into Binary Code: ")

    if all(bit in '01' for bit in gray_input):
        result = gray_to_binary(gray_input)

        print(f"Gray Code: {gray_input}")
        print(f"Corresponding Binary Code: {result}")
    else:
        print("Invalid input. Please enter a valid Gray Code consisting only of 0's and 1's.")