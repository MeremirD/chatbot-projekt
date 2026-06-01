from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_community.document_loaders import TextLoader


# Change this to any Ollama model you have installed
chatmodel = "llama3.1:8b"

# Load the document
print("Loading document...")
loader = TextLoader("wissen.txt", encoding="utf-8")
documents = loader.load()

# Split into chunks
print("Splitting document into chunks...")
splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
chunks = splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")

# create embeddings and store in ChromaDB
print("Creating vector databse...")
embeddings = OllamaEmbeddings(model=chatmodel)
vectorstore = Chroma.from_documents(chunks, embeddings)
print("Vector database ready!")

# Init chat model
llm = ChatOllama(model=chatmodel)

print("\nRAG Chatbot started! (Type 'quit' to exit)")
print("-" * 40)

# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    # Search the vector database for relevant chunks
    relevant_docs = vectorstore.similarity_search(user_input, k=3)

    # Combine the relevant chunks into one context string
    context = "\n".join([doc.page_content for doc in relevant_docs])

    # Build the prompt with context + user question
    prompt = f"""Use the following context to answer the question.
    If the answer is not in the context, say "I don't know".
    Context:
    {context}
    Question: {user_input}
    """

    # Send to the model and get response
    response = llm.invoke([HumanMessage(content=prompt)])

    print(f"Bot: {response.content}")
    print()