import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)
    assert height_array.shape == weight_array.shape, "The height and weight lists must have the same size."
    assert np.any(height_array == 0) , "Height cannot be zero."
    bmi_values = weight_array / (height_array ** 2)
    return bmi_values.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array = np.array(bmi, dtype=float)
    result_array = bmi_array > limit    
    return result_array.tolist()

heights = [1.70, 1.80, 1.60]
weights = [65, 80, 50]
bmi_values = give_bmi(heights, weights)
print(bmi_values) 
limit_value = 25
above_limit = apply_limit(bmi_values, limit_value)
print(above_limit) 