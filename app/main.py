from services.llm import ask_gemini
from services.document_loader import load_document

def main() :
    
    path = input("Enter the path to the document: ")
    
    document_text = load_document(path)
    
    print("Enterprise Document Intelligence Agent")
    print("Type 'exit' to quit\n")
    
    ques = input("Ask a question about the document: ")
    
    prompt = f"""Answer the following question about the document:
    Question: {ques}
    Document: {document_text[:20000]}"""
    
    answer = ask_gemini(prompt)
    print(answer)
    
    # while True :
    #     question = input("You: ")

    #     if question.lower() == "exit":
    #         break

    #     answer = ask_gemini(question)

    #     print("\nAgent:")
    #     print(answer)
    #     print()


if __name__ == "__main__":
    main()