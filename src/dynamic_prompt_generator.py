import json

def load_parameters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        params = json.load(file)
    return params

def replace_placeholders(prompt, params):
    for key, value in params.items():
        placeholder = f"{{{{ {key} }}}}"
        if placeholder in prompt:
            prompt = prompt.replace(placeholder, str(value))
        else:
            raise ValueError(
                f"Placeholder {placeholder} not found in the prompt.")
    return prompt

def generate_dynamic_prompt(prompt_file_path, params):
    # Load initial prompt from the specified file
    with open(prompt_file_path, 'r', encoding='utf-8') as file:
        initial_prompt = file.read()

    # Replace placeholders in the prompt
    customized_prompt = replace_placeholders(initial_prompt, params)
    return customized_prompt