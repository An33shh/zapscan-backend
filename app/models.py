from pydantic import BaseModel, Field

class ScanRequest(BaseModel):
    target_url: str = Field(..., description="The URL of the website to scan")

class Vulnerability(BaseModel):
    id: int
    name: str
    risk: str
    description: str
    solution: str

class ScanResults(BaseModel):
    status: str = "completed"
    vulnerabilities: list[Vulnerability] = []
