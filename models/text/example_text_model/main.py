from detoxify import Detoxify

model = Detoxify('original')

def predict(test_input):
    """Predicts the toxicity of the input text using the Detoxify model.

    Args:
        test_input (dict): A dictionary containing the input text.
            - 'input' (dict): A dictionary with the key 'text' representing the input text.
                - 'text' (str): The input text to be analyzed for toxicity.

    Returns:
        dict: A dictionary containing the prediction results.
            - 'data_type' (str): The type of data being analyzed.
            - 'output' (list): A list of the labels predicted by the model.
            - 'score' (list): A list of the corresponding prediction scores for each label.
            - 'box' (list): A list of bounding boxes (not used in this function).
            - 'additional' (list): A list of additional data such as segmentation maps (not used in this function).

    Example:
        >>> test_input = {
                "input": {
                    "text": "example text"
                }
            }
        >>> predict(test_input)
            {
                'data_type': 'text', 
                'output': ['toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack'], 
                'score': [0.0006478309, 0.000120983976, 0.00018694326, 0.00011624079, 0.00018111907, 0.00014001901], 
                'box': [], 
                'additional': []
            }
    """
    text = test_input["input"]["text"]
    prediction = model.predict(text)
    result = {
        "data_type": "text", 
        "output": list(prediction.keys()),
        "score": list(prediction.values()), 
        "box": [], 
        "additional": []
    }
    return result

if __name__ == "__main__":
    test_input = {
        "input": {
            "text": "example text"
        }
    }
    out = predict(test_input)
    print(out)