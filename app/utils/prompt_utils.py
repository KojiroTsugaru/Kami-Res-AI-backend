from app.data.prompts import Prompts

def process_parameters(parameters):
    try:
        mood = parameters.get('mood', '')
        length = parameters.get('length', '')
        
        if not mood or not length:
            raise ValueError("Missing required parameters: mood and length")
        
        if not isinstance(length, (int, float)):
            raise ValueError("Length must be a number")
            
        converted_length = convertLength(length)
        prompt = Prompts.get_prompt(mood, converted_length)
        
        return {
            "prompt": prompt
        }
        
    except ValueError as e:
        raise ValueError(str(e))
    except Exception as e:
        raise Exception("Error processing parameters")

def convertLength(length):
    valid_lengths = [1.0, 2.0, 3.0]
    if length not in valid_lengths:
        raise ValueError(f"Invalid length value. Must be one of: {valid_lengths}")
        
    if length == 1.0:
        return "15文字以内"
    elif length == 2.0:
        return "20文字以上50文字以内"
    elif length == 3.0:
        return "50文字以上"
    