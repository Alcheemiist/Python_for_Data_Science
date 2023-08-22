import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    family_array = np.array(family, dtype=object)

    if len(family_array.shape) != 2:
        raise ValueError("'family' must be a 2D array (list of lists).")

    shape = family_array.shape
    print(f"Shape: {shape}")
    if start < 0 or end > shape[1] or start > end:
        raise ValueError("Invalid start or end index.")

    sliced_array = family_array[:, start:end]

    return sliced_array.tolist()
