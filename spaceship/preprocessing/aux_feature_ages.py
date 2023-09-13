def assign_age_group(age):
    """
    Assign an age group label based on the given age.

    Age groups are categorized as follows:
    - 0_child: Age <= 12
    - 1_teenager: Age <= 17
    - 2_young_adult: Age <= 25
    - 3_adult: Age <= 30
    - 4_middle_age: Age <= 50
    - 5_senior: Age > 50

    Args:
        age (int or float): The age of the passenger.

    Returns:
        str: The age group label.
    """
    if age <= 12:
        return '0_child'
    elif age <= 17:
        return '1_teenager'
    elif age <= 25:
        return '2_young_adult'
    elif age <= 30:
        return '3_adult'
    elif age <= 50:
        return '4_middle_age'
    else:
        return '5_senior'