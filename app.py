import streamlit as st
import re  
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Negotiation Chatbot", page_icon="🤖")
st.title("Negotiation Chatbot")

try:
    llm = ChatGroq(api_key=groq_api_key, model="Gemma-7b-It")
except Exception as e:
    st.error("Failed to initialize the language model. Please check the API key.")
    st.stop()

prompt = """
You are a negotiation assistant helping the user negotiate a product price.
You should offer a base price, and respond to user offers by either accepting, rejecting, or proposing a counteroffer.
The conversation should be straightforward: accept the offer if it meets or exceeds the base price, or suggest a counteroffer if it's lower but not too low.

Conversation so far:
{conversation_history}

The user proposes: {question}
Respond with a direct negotiation answer.
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=['conversation_history', 'question'],
    template=prompt
)

chain = LLMChain(llm=llm, prompt=prompt_template)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Let's start negotiating. The base price for the product is $1000. What's your offer?"}
    ]
    st.session_state.base_price = 1000
    st.session_state.max_discount = 500
    st.session_state.minimum_price = st.session_state.base_price - st.session_state.max_discount

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_conversation_history():
    conversation = ""
    for message in st.session_state.messages:
        if message["role"] == "user":
            conversation += f"User: {message['content']}\n"
        else:
            conversation += f"Assistant: {message['content']}\n"
    return conversation

def extract_price(text):
    price = re.findall(r'\d+', text)  
    if price:
        return float(price[0])  
    return None

def negotiate_price(user_input):
    user_offer = extract_price(user_input)

    if user_offer is None:
        return "Please provide a numerical offer for the product."
    
    if user_offer >= st.session_state.base_price:
        return f"Deal accepted at ${user_offer}$. Thank you!"
    
    elif user_offer < st.session_state.minimum_price:
        return f"Your offer of ${round(user_offer)}$ is too low. The lowest I can accept is ${st.session_state.minimum_price}$."
    
    else:
        counter_offer = (st.session_state.base_price + user_offer) / 2
        return f"I can't accept ${user_offer}$. How about we meet in the middle at ${round(counter_offer, 2)}$?"

if user_input := st.chat_input("Type your offer or question here:"):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    conversation_history = get_conversation_history()

    if extract_price(user_input):
        negotiation_response = negotiate_price(user_input)
    else:
        try:
            negotiation_response = chain.run({
                "conversation_history": conversation_history,
                "question": user_input
            })
        except Exception as e:
            negotiation_response = "Sorry, I couldn't generate a response. Please try again later."

    st.session_state.messages.append({"role": "assistant", "content": negotiation_response})

    with st.chat_message("assistant"):
        st.markdown(negotiation_response)
