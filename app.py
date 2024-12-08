from Agents import agents_team
import uuid
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse



app = FastAPI()

@app.post("/query/")
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

	leader = agents_team(pdf_path, session_id, user_id, arxiv_path, code_path)

	

	return JSONResponse()