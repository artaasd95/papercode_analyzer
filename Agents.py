from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.storage.agent.postgres import PgAgentStorage




model = Groq(id="llama3-groq-70b-8192")
#model=OpenAIChat(id="gpt-4o")

db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
paper_pdf_storage = PgAgentStorage(table_name="paper_pdf_sessions", db_url=db_url)
arxiv_storage = PgAgentStorage(table_name="arxiv_sessions", db_url=db_url)
code_analyzer_storage = PgAgentStorage(table_name="code_analyzer_sessions", db_url=db_url)
leader_storage = PgAgentStorage(table_name="leader_sessions", db_url=db_url)



paper_pdf = Agent(
        model=model,
        storage=paper_pdf_storage,
        tools=[],
        show_tool_calls=True,
        add_chat_history_to_messages=True,
        add_history_to_messages=True,
        name='Paper reader',
        description="You are a pro researcher",
        instructions=[

        ],

        )

arxiv_analyzer = Agent(
        model=model,
        storage=arxiv_storage,
        tools=[],
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