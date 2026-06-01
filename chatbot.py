from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(model="llama3.1:8b")

# System prompt - customize this to define the personality and rules of the chatbot
system_prompt = "You are a helpful assistant."

print("chatbot started! (Type 'quit' to exit)")
print("-" * 40)

# Conversation history - we start with the system message
# This list grows with every message, so the bot remembers the conversation
messages = [SystemMessage(content=system_prompt)]

# Infinite loop - keeps the chat running until user types 'quit'
while True:

    # Wait for user input
    user_input = input("You: ")

    # Exit condition - if user types 'quit', break out of the loop
    if user_input.lower() == "quit":
        break

    # Wrap user input in a HumanMessage and add it to the history
    messages.append(HumanMessage(content=user_input))

    # Send the entire conversation history to the model and get a response
    # The model sees ALL previous messages - that's how it remembers context
    response = llm.invoke(messages)

        # Add the bot's response to the history too
    # This way the next message will include this response as context
    messages.append(response)
    
    # Print the bot's response text
    print(f"Bot: {response.content}")
    print()  # Empty line for better readability