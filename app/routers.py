from fastapi import APIRouter, HTTPException
from zapv2 import ZAPv2
import time

from app.models import ScanRequest, ScanResults, Vulnerability
from config import ZAP_API_KEY  

router = APIRouter()
zap = ZAPv2(apikey=ZAP_API_KEY)

@router.post("/scan/", response_model=ScanResults)
async def scan_website(request: ScanRequest):
    target_url = request.target_url

    # 1. Start or Connect to ZAP:
    try:
        zap.core.ping()  # Check if ZAP is running
    except ConnectionError:
        raise HTTPException(status_code=500, detail="Unable to connect to ZAP")

    # 2. Spider Scan:
    scan_id = zap.spider.scan(target_url)
    while (int(zap.spider.status(scan_id)) < 100):
        # Wait for the spider to finish
        time.sleep(5)

    # 3. Active Scan:
    scan_id = zap.ascan.scan(target_url)
    while (int(zap.ascan.status(scan_id)) < 100):
        # Wait for the active scan to finish
        time.sleep(5)

    # 4. Retrieve and Process Alerts:
    alerts = zap.core.alerts(baseurl=target_url)
    vulnerabilities = []
    for alert in alerts:
        vulnerabilities.append(Vulnerability(
            id=alert.get('id'),
            name=alert.get('name'),
            risk=alert.get('risk'),
            description=alert.get('description'),
            solution=alert.get('solution'),
        ))

    # 5. Return Scan Results:
    return ScanResults(vulnerabilities=vulnerabilities)
