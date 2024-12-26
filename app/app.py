from Agents import agents_team
import uuid
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uuid
from typing import Optional
from pydantic import BaseModel


teams = dict()


app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    pdf_path: Optional[str] = None
    arxiv_path: Optional[str] = None
    code_path: Optional[str] = None


@app.post("/query")
async def process_data(request: Request):
	request_body = await request.json()
	try:
		query = request_body.get("query")
	except Exception as e:
		raise HTTPException(status_code=400, detail=f"query not provided: {str(e)}")
	
	try:
		pdf_path = request_body.get("pdf_path")
	except:
		pdf_path = None

	try:
		arxiv_path = request_body.get("arxiv_path")
	except:
		arxiv_path = None
	
	try:
		code_path = request_body.get("query")
	except:
		code_path = None
	
	session_id = str(uuid.uuid4)
	user_id = str(uuid.uuid4)

	if session_id not in teams.keys():
		leader = agents_team(pdf_path, session_id, user_id, arxiv_path, code_path)
		teams[session_id] = leader
	else:
		leader = teams[session_id]

	response = leader.run_query(query)

	return JSONResponse(content={"answer": response})