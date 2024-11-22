INPUT_SCHEMA = {
    "text_input": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["There is a fine house in the forest"]
    },
    "max_tokens": {
        'datatype': 'INT16',
        'required': False,
        'shape': [1],
        'example': [256]
    }
}
