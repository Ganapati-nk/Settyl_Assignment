# Negotiation Chatbot with Gemma-7b-It and LangChain

This project integrates the Gemma-7b-It AI model into a negotiation chatbot using the LangChain framework and Streamlit. The chatbot is designed to simulate a dynamic pricing process, enabling users to negotiate product prices effectively. Leveraging advanced conversational AI, it provides intelligent responses to user offers and queries.

## Features

- **Dynamic Price Negotiation:** The chatbot handles price negotiations by accepting, rejecting, or proposing counteroffers based on user input.
- **Conversational AI:** Utilizes the Gemma-7b-It model from LangChain for sophisticated conversational capabilities, ensuring relevant and engaging interactions.
- **Real-Time Interaction:** Built with Streamlit for a smooth, interactive user experience, where users can enter offers and receive immediate responses.

## How It Works

1. **Environment Setup:**
   - **Python Libraries:** Includes `streamlit`, `langchain_groq`, and `dotenv` for environment setup and integration.
   - **API Key Management:** Uses a `.env` file to securely store and manage the `GROQ_API_KEY` for model authentication.

2. **Model Integration:**
   - **Gemma-7b-It Model:** Selected for its strong conversational abilities. Integrated using the `ChatGroq` class from LangChain.
   - **Error Handling:** Implemented a try-except block to handle API key issues and ensure smooth operation.

3. **Prompt Template Design:**
   - **Custom Prompts:** Created a prompt template to guide AI responses based on conversation history and user offers.
   - **Negotiation Guidance:** Directs the AI to accept, reject, or counter user offers according to predefined rules.

4. **Negotiation Logic:**
   - **Price Handling:** Uses regular expressions to extract numeric values from user inputs for negotiation.
   - **Rule-Based Logic:** Implements rules for accepting, rejecting, or countering offers based on a base price and minimum acceptable price.

5. **AI-Driven Conversation:**
   - **Fallback Mechanism:** When no price is provided, the chatbot engages the AI model for general conversation.
   - **Context Management:** Maintains conversation context using the `LLMChain` class to ensure coherent interactions.

6. **User Interface:**
   - **Streamlit Integration:** Provides an interactive UI for users to input their offers or queries and view responses in real time.


