from app.data.prompts import Prompts

def process_parameters(parameters):
    try:
        mood = parameters.get('mood', '')
        length = parameters.get('length', '')
        
        if not mood or not length:
            raise ValueError("Missing required parameters: mood and length")
            
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
    if length == 1.0:
        return "15文字以内"
    elif length == 2.0:
        return "20文字以上50文字以内"
    elif length == 3.0:
        return "50文字以上"
    else:
        return "20文字以上50文字以内"
    