from fastapi import FastAPI, Request
import pdfplumber
import io

app = FastAPI()

@app.post("/extract")
async def extract_pdf(request: Request):
    pdf_bytes = await request.body()

    tables = []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            if page_tables:
                tables.extend(page_tables)

    return {
        "pages": len(pdf.pages),
        "tables": tables
    }
