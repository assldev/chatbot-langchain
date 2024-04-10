from utilities.llm_factory import LLMFactory

def main():

    
    llm_response = llm_object.get_message("Suggest company name!")
    print(llm_response)

def main():

    # INITIALIZE CHATBOT
    llm_factory = LLMFactory()
    llm_object = llm_factory.get_llm("openai", {
        "temperature": 0.2
    })

    conversation_history = []

    while True:
        user_input = input("You: ")
        conversation_history.append(f"User: {user_input}")

        if user_input.lower() == "quit":
            break

        llm_response = llm_object.get_message(user_input, conversation_history)
        conversation_history.append(f"AI: {llm_response}")

        print(f"AI: {llm_response}")

if __name__ == "__main__":
    main()
