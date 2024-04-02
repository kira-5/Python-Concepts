# Initialize an empty cache dictionary
cache = {}

# Function to calculate the factorial of a number
def factorial(n):
    if n in cache:
        print(f"cache:: {cache}")
        return cache[n]  # Return cached result if available

    # Calculate factorial if not cached
    result = 1
    for i in range(1, n + 1):
        result *= i

    # Cache the result
    cache[n] = result
    return result

# Example usage
print(factorial(5))  # Calculates and caches factorial of 5
