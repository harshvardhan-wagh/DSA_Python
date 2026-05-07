def reverseArray(arr):
    print(f"reverseArray called with: {arr}")  # Let's see what's happening

    # Base case: If the array is empty or has one element, it's already reversed
    if len(arr) <= 1:
        print(f"Base case reached, returning: {arr}")
        return arr
    else:
        # Recursive step:
        # 1. Take the first element
        first = arr[0]
        print(f"First element: {first}")

        # 2. Recursively reverse the rest of the array
        rest_of_array = arr[1:]
        print(f"Calling reverseArray with the rest: {rest_of_array}")
        rest_reversed = reverseArray(rest_of_array)
        print(f"Returned from recursive call with: {rest_reversed}")

        # 3. Append the first element to the end of the reversed rest
        result = rest_reversed + [first]
        print(f"Combining {rest_reversed} + [{first}] to get: {result}")
        return result

# Example usage:
my_array = [1, 2, 3, 4, 5]
reversed_array = reverseArray(my_array)
print(f"Final reversed array: {reversed_array}")