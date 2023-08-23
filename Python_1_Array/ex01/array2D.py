import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    print(type(family))
    assert isinstance(family, list), "'First parameter must be a list."
    family_array = np.array(family, dtype=object)
    assert len(family_array.shape) == 2,  \
        "'family' must be a 2D array (list of lists)."
    index = len(family_array[0])
    for row in family_array:
        assert len(row) == index, "the list are not the same size."
    shape = family_array.shape
    print("My shape is : ", shape)
    sliced_array = family_array[start:end, :]
    print("My new Shape is : ", sliced_array.shape)
    return sliced_array.tolist()
