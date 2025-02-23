from app.data.prompts import Prompts

def process_parameters(parameters):
    mood = parameters.get('mood', '')
    length = parameters.get('length', '')
    prompt = generate_prompt(mood, length)

    result = {
        "prompt": prompt,
        "status": "success"
    }
    
    return result

def generate_prompt(mood, length):
    convertedLength = convertLength(length)
    prompt_helper = Prompts.prompt_helper.format(length=convertedLength)

    prompts = {
        "casual": Prompts.casual,
        "humorous": Prompts.humorous,
        "cool": Prompts.cool
    }

    if mood in prompts:
        prompt = prompt_helper + prompts[mood]
    else:
        prompt = "気分が認識できません"
    
    return prompt

def convertLength(length):
    if length == 1.0:
        return "15文字以内"
    elif length == 2.0:
        return "20文字以上50文字以内"
    elif length == 3.0:
        return "50文字以上"
    else:
        return "20文字以上50文字以内"
    