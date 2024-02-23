def join_array_remove_duplicate(arrayA, arrayB):
    combined_array = arrayA + arrayB

    # Remove duplicate values while preserving the order
    unique_array = []
    for item in combined_array:
        if item not in unique_array:
            unique_array.append(item)

    return unique_array

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
