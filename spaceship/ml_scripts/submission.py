# Script for generating submission file for Kaggle competition

def generate_main_submission(data_test, model, path_data, submission_name):
    """
        Function to generate a submission file.
    """
    forecast = model.predict(data_test)
    # As the model predicts the probability of being transported (close to 1) or not (close to 0), I will use a
    # threshold of 0.5 to convert the probabilities into binary categories
    forecast = np.where(forecast > 0.5, True, False)

    # Create dataframe for submission
    passenger_id = data_test['PassengerId']
    submission = pd.DataFrame({'PassengerId': passenger_id, 'Transported': forecast[:, 0]})

    # Save submission
    submission.to_csv(path_data + '/' + submission_name, index=False)

    return submission
