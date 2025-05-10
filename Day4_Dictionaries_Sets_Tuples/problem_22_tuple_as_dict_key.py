"""
✅ Problem 22: Use Tuple as Dictionary Key

🧠 Problem Statement:
Write a function that demonstrates how to use a tuple as a dictionary key.
Build a dictionary where each key is a coordinate pair (x, y), and the value is a string label or numeric value.
"""

def build_coordinate_map():
    """
    Creates a dictionary with coordinate tuples as keys.

    Returns:
    dict: A dictionary where each key is a (x, y) tuple and each value is a label or numeric value.
    """
    coord_map = {
        (0, 0): 'origin',
        (1, 2): 'point A',
        (3, 4): 'point B',
        (5, 6): 'point C'
    }
    return coord_map


# 🧪 Test Output
if __name__ == "__main__":
    coords = build_coordinate_map()
    print("Coordinate Map:", coords)
    print("Value at (1, 2):", coords.get((1, 2)))   # Expected: 'point A'
    print("Value at (0, 0):", coords.get((0, 0)))   # Expected: 'origin'
