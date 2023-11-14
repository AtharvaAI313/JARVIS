# Jarvis Chatbot README

Jarvis is a simple chatbot powered by the LangChain library, using the Cohere language model. It can answer questions based on a predefined template and is designed to provide concise responses.

## Requirements

- Python 3.7 or above
- Required Python packages:
  - pyttsx3
  - os
  - speech_recognition
  - langchain (install using `pip install langchain`)
  
## Setup

1. Install the required packages:

   ```bash
   pip install pyttsx3 os speech_recognition langchain
   ```

2. Obtain a Cohere API key from [Cohere](https://cohere.so/).

3. Replace the empty string in `cohere_api_key` with your Cohere API key:

   ```python
   llm = Cohere(cohere_api_key="your_cohere_api_key_here")
   ```

## Usage

1. Run the script:

   ```bash
   python jarvis_chatbot.py
   ```

2. Speak a question into the microphone when prompted. Jarvis will attempt to recognize the question and provide a concise answer.

   ```bash
   Ask me a question:
   ```

3. Jarvis will process the input using the Cohere language model and provide a response:

   ```bash
   You asked: How does photosynthesis work?
   Photosynthesis is the process by which plants convert light energy into chemical energy.
   ```

4. The response will be spoken aloud using text-to-speech.

## Customization

You can customize the chatbot behavior by modifying the template string and other parameters in the script. The template string is used to structure the input for the language model. Adjust the `template` variable as needed.

```python
template = """You are Jarvis, a highly intelligent chatbot. Answer questions concisely without apologies. {question}"""
```

## Notes

- If the script is unable to understand the audio input, it will print "Sorry, I couldn't understand the audio."

- In case of a request error with the Google Speech Recognition service, it will notify the user.

Feel free to experiment with different templates and language models to enhance Jarvis's capabilities.
