import sqlite3
import deepgram
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Deepgram client with your API key
deepgram_client = deepgram.Deepgram(api_key=os.getenv("DEEPGRAM_API_KEY"))

conn = sqlite3.connect('allergy_checker.db')

def check_allergens(user_id, product_name):
    c = conn.cursor()
    
    # Get user allergens
    c.execute("SELECT allergens FROM users WHERE id = ?", (user_id,))
    user_allergens = c.fetchone()[0].split(', ')
    
    # Get product ingredients
    c.execute("SELECT ingredients FROM products WHERE product_name = ?", (product_name,))
    product_ingredients = c.fetchone()[0].split(', ')
    
    # Check for allergens in the ingredients
    for allergen in user_allergens:
        if allergen in product_ingredients:
            return False
    return True

def text_to_speech(text, output_file):
    try:
        # Use Deepgram API to convert text to speech
        response = deepgram_client.speak(
            text=text,
            output_format="wav"  # Specify the output format as WAV file
        )

        # Save the speech audio to a file
        with open(output_file, "wb") as f:
            f.write(response)

        print("Text converted to speech successfully.")
        return True
    except Exception as e:
        print("Error:", e)
        return False

def speech_to_text(audio_file):
    try:
        # Use Deepgram API to convert speech to text
        with open(audio_file, "rb") as f:
            audio_data = f.read()

        response = deepgram_client.transcribe(audio_data)

        print("Speech converted to text:", response)
        return response
    except Exception as e:
        print("Error:", e)
        return None


