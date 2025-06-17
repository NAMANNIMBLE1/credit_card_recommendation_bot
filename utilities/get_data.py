import json

def get_credit_cards():
    """
    Returns the credit cards data from the data/credit_cards.json file
    Returns:
        list: A list of credit cards data
    """
    with open("data/credit_cards.json", "r") as f:
        return json.load(f)


# print(get_credit_cards()) # for checking purpose