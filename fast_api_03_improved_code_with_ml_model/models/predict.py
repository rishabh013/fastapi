import pickle
import pandas as pd

# import the ml model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

# get class label from the model(important for machine probabiliteis to class name)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])

    # predict the class
    predict_class = model.predict(input_df)[0]

    # Get the class probabilities
    class_probabilities = model.predict_proba(input_df)[0]
    confidence = max(class_probabilities)

    # Create mapping of class labels to their probabilities
    class_prob_dict = dict(zip(class_labels, map(lambda p: round(p, 4), class_probabilities)))
    return {
        'predicted_class': predict_class,
        'confidence': round(confidence, 4),
        'class_probabilities': class_prob_dict
    }