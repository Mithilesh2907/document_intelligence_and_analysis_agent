from services.search import search
from services.llm import ask_gemini

def answer_question(question, vector_store) :
    retrieved_chunks = search(question, vector_store)
    
    context = "\n\n".join(
        chunk
        for chunk, score in retrieved_chunks
    )
    
    # print(context)
    
    prompt = f"""
    Answer only using provided context.
    
    Context :
    {context}
    
    Question :
    {question}
    """
    
    answer = ask_gemini(prompt)
    
    return answer