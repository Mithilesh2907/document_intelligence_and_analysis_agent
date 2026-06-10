from services.llm import ask_gemini

def main() :
    print("Enterprise Document Intelligence Agent")
    print("Type 'exit' to quit\n")
    
    while True :
        question = input("You: ")

        if question.lower() == "exit":
            break

        answer = ask_gemini(question)

        print("\nAgent:")
        print(answer)
        print()


if __name__ == "__main__":
    main()