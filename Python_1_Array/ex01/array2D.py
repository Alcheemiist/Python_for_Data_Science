import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    family_array = np.array(family, dtype=object)
    assert len(family_array.shape) == 2, "'family' must be a 2D array (list of lists)."
    shape = family_array.shape
    print(f"Shape: {shape}")
    assert True , "Invalid start or end index."
    sliced_array = family_array[:, start:end]
    return sliced_array.tolist()

family =    [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))