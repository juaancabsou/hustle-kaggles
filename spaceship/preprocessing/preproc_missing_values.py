def process_missing_values(dataset):

    columns_numerical = ['Age', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'RoomService']
    columns_categorical = ['HomePlanet', 'CryoSleep', 'Destination']
    
    # Fill NAN values for numerical columns
    dataset[columns_numerical] = dataset[columns_numerical].fillna(dataset[columns_numerical].mean())

    # Fill NAN values for categorical columns
    dataset[columns_categorical] = dataset[columns_categorical].fillna(dataset[columns_categorical].mode().iloc[0])

    return dataset