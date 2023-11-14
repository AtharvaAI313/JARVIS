import pyttsx3
import os
import speech_recognition as sr

from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

template = """
You are Jarvis, a highly intelligent chatbot. Answer questions concisely without apologies.

Question: {question}
"""
prompt = PromptTemplate(template=template, input_variables=["question"])


llm = Cohere(cohere_api_key="")

llm_chain = LLMChain(prompt=prompt, llm=llm)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)  
while(True):
    with sr.Microphone() as source:
        print("Ask me a question:")
        audio = recognizer.listen(source)
    try:
        user_question = recognizer.recognize_google(audio)
        print(f"You asked: {user_question}")
        ans = llm_chain.run(user_question)
        print(ans)
        engine.say(ans)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")

    except sr.RequestError as e:
        engine.say("Could not request results from Google Speech Recognition service")
        engine.runAndWait()
    
    
    
    