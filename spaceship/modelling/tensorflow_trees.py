# Script for gathering all the model functions regarding tensorflow trees
import pandas as pd
import numpy as np
import json

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Tensorflow libraries
import tensorflow as tf
import tensorflow_decision_forests as tfdf

print("TensorFlow v" + tf.__version__)
print("TensorFlow Decision Forests v" + tfdf.__version__)


def tf_tree_based_models(x_train, x_val, df_test, target_name, model_name='random_forest', hyperparameters=None):
    """
    Function to train tree-based models with Tensorflow Decision Forests
    As this function at the moment can't be used with Windows, I will save the predictions in a folder alongside the 
    stats of the model. So if the parameter predict is True, then the function will save the predictions in a folder. Else, it will read the predictions from the folder.
    """
    path_results = '/Users/juaancabsou/Documents/kaggle/kaggle_spaceship/y_forecast/'

    # Check models available
    # ------------------------------
    checker_tfdf_correct_model(model_name)

    # Create a tensorflow datasets (train, validation, test)
    # ------------------------------
    df_tf_train = tfdf.keras.pd_dataframe_to_tf_dataset(x_train, label=target_name)
    df_tf_val = tfdf.keras.pd_dataframe_to_tf_dataset(x_val, label=target_name)
    df_tf_test = tfdf.keras.pd_dataframe_to_tf_dataset(df_test)

    # Generate and train the model
    # ------------------------------
    model = generate_tfdf_model(model_name, hyperparam=None)
    model.compile(metrics=["accuracy"])
    model.fit(df_tf_train)

    # Evaluate the model on the validation set using Out-of-bag metrics (OOB)
    # ------------------------------
    try:
        logs = model.make_inspector().training_logs()
        plt.plot([log.num_trees for log in logs], [log.evaluation.accuracy for log in logs])
        plt.xlabel("Number of trees")
        plt.ylabel("Out-of-bag accuracy")
        plt.show()

    except Exception as e:
        print('Model does not have OOB metrics')
        print(e)

    # Get general stats on the model
    # ------------------------------
    stats_evaluation = model.make_inspector().evaluation()
    print(stats_evaluation)

    evaluation = model.evaluate(df_tf_val, return_dict=True)
    for name, value in evaluation.items():
        print(f"{name}: {value:.4f}")

    # Which features are the most important?
    # ------------------------------
    importance = model.make_inspector().variable_importances()["NUM_AS_ROOT"]
    df_importance = pd.DataFrame(importance)
    display(df_importance)


    # Make predictions
    # ------------------------------
    predictions = model.predict(df_tf_test)
    predictions = predictions.flatten()

    result = {
        'model_name': model_name,
        'loss': evaluation['loss'],
        'accuracy': evaluation['accuracy']
    }

    # Save result and predictions
    # ------------------------------
    np.save(path_results + model_name + '_predictions.npy', predictions)
    json.dump(result, open(path_results + model_name + '_stats.json', 'w'))

    result['predictions'] = predictions
    return result


def checker_tfdf_correct_model(model_name):
    # Check models available
    if model_name not in ['random_forest', 'gradient_boosted_trees', 'cart', 'extremely_randomized_trees', 'random_forest_v2']:
        raise ValueError('Model name not available')
        print('Possible models to use with Tensorflow Decision Forests: \n')
        for tdf_model in tfdf.keras.get_all_models():
            print(tdf_model)
    return None


def generate_tfdf_model(model_name, hyperparam=None):
    """
    Function to generate the model
    """
    
    # Models without hyperparameters
    # ------------------------------
    if hyperparam is None:
        if model_name == 'random_forest':
            model = tfdf.keras.RandomForestModel()
        elif model_name == 'gradient_boosted_trees':
            model = tfdf.keras.GradientBoostedTreesModel()
        elif model_name == 'cart':
            model = tfdf.keras.CartModel()

    else:
        # Models with hyperparameters
        # ------------------------------
        if model_name == 'random_forest':
            model = tfdf.keras.RandomForestModel(hyperparameter_template=hyperparam, task='classification')
        elif model_name == 'gradient_boosted_trees':
            model = tfdf.keras.GradientBoostedTreesModel(hyperparameter_template=hyperparam, task='classification')
        elif model_name == 'cart':
            model = tfdf.keras.CartModel(hyperparameter_template=hyperparam, task='classification')
 

    print('Model', model_name, 'created')
    return model