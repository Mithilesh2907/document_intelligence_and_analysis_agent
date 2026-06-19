from services.llm import ask_gemini
from services.document_loader import load_document
from services.search import search
from services.chunking import chunk_text
from services.vector_store import InMemoryVectorStore
from services.RAG_pipeline import answer_question

def main() :
    path = input("Document path: ")
    
    text = load_document(path)
    chunks = chunk_text(text)
    store = InMemoryVectorStore()
    store.add_chunks(chunks)
    
    while True :
        query = input("\nQuestion : ")
        
        if query.lower() == "exit" :
            return
        
        answer = answer_question(query, store)
        
        print("\nAnswer : ")
        print(answer)
        
        # results = search(query, store)
        
        # print("Top relevant matches : ")
        
        # for chunk, score in results :
        #     print(f"""Score: {score:.3f}""")
        #     print(chunk)
        #     print("-" * 50)
            
if __name__ == "__main__" :
    main()



# def main() :
    
#     path = input("Enter the path to the document: ")
    
#     document_text = load_document(path)
    
#     print("Enterprise Document Intelligence Agent")
#     print("Type 'exit' to quit\n")
    
#     ques = input("Ask a question about the document: ")
    
#     prompt = f"""Answer the following question about the document:
#     Question: {ques}
#     Document: {document_text[:20000]}"""
    
#     answer = ask_gemini(prompt)
#     print(answer)
    
#     # while True :
#     #     question = input("You: ")

#     #     if question.lower() == "exit":
#     #         break

#     #     answer = ask_gemini(question)

#     #     print("\nAgent:")
#     #     print(answer)
#     #     print()


# if __name__ == "__main__":
#     main()