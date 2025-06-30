def find_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:  # Check for an empty list
        return 0
    return sum(numbers) / len(numbers)