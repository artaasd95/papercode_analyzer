from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.storage.agent.postgres import PgAgentStorage
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from langchain_community.document_loaders import PyPDFLoader
from phi.knowledge.langchain import LangChainKnowledgeBase
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import uuid

def generate_vector_store(document_path):

	loader = PyPDFLoader(document_path)
	pages = loader.load_and_split()
	embedding = OpenAIEmbeddings()
	faiss_vectorstore = FAISS.from_documents(pages, embedding=embedding)
	faiss_retriever = faiss_vectorstore.as_retriever(
                search_type="similarity_score_threshold",
                search_kwargs={
                    #'k': 5, 'fetch_k': 50, 
                            'score_threshold': 0.7}
                )

	return faiss_retriever
	

def agents_team(pdf_path, ):


	model = Groq(id="llama3-groq-70b-8192")
	#model=OpenAIChat(id="gpt-4o")

	db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
	paper_pdf_storage = PgAgentStorage(table_name="paper_pdf_sessions", db_url=db_url)
	arxiv_storage = PgAgentStorage(table_name="arxiv_sessions", db_url=db_url)
	code_analyzer_storage = PgAgentStorage(table_name="code_analyzer_sessions", db_url=db_url)
	leader_storage = PgAgentStorage(table_name="leader_sessions", db_url=db_url)

	faiss_retriever = generate_vector_store(pdf_path)
	knowledge_base_faiss = LangChainKnowledgeBase(
                retriever=faiss_retriever,
                num_documents=2,
                #optimize_on=1000
                )

	paper_pdf = Agent(
		model=model,
		storage=paper_pdf_storage,
		tools=[],
		show_tool_calls=True,
		add_chat_history_to_messages=True,
		add_history_to_messages=True,
		knowledge_base=knowledge_base_faiss,
		add_references_to_prompt=True,
		name='Paper reader',
		description="You are a pro researcher",
		instructions=[

		],

		)

	arxiv_analyzer = Agent(
		model=model,
		storage=arxiv_storage,
		tools=[ArxivToolkit()],
		show_tool_calls=True,
		add_chat_history_to_messages=True,
		add_history_to_messages=True,
		name='Arxiv analyzer',
		description="You are a pro arxiv paper finder and analyzer",
		instructions=[

		],
		
		)

	code_analyzer = Agent(
		model=model,
		storage=code_analyzer_storage,
		tools=[],
		show_tool_calls=True,
		add_chat_history_to_messages=True,
		add_history_to_messages=True,
		name='code analyzer',
		description="You are a pro and experienced code analyzer, reviewer and programmer",
		instructions=[

		],
		
		)

	leader_agent = Agent(
		model=model,
		storage=leader_storage,
		tools=[],
		show_tool_calls=True,
		add_chat_history_to_messages=True,
		add_history_to_messages=True,
		name='Paper research code analyzer',
		description="You the head of a team that find, analyze academic papers,"+\
		"read them and find the code of them or even provide code",
		instructions=[

		],
		team=[paper_pdf, arxiv_analyzer, code_analyzer]
		
		)



	return leader_agent