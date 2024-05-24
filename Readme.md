# ZapScan: A Web Vulnerability Scanner 🕷️🔍

ZapScan is a powerful web vulnerability scanner built with [FastAPI](https://fastapi.tiangolo.com/) and [OWASP ZAP](https://www.zaproxy.org/). It automates the process of identifying common security vulnerabilities in web applications, helping developers and security professionals safeguard their websites against potential threats.

## Key Features 🚀

- **Automated Scanning:** Easily scan any website for common vulnerabilities.
- **OWASP Top 10 Coverage:** Identifies a wide range of vulnerabilities listed in the [OWASP Top 10](https://owasp.org/www-project-top-ten/).
- **Detailed Reports:** Get comprehensive scan reports with vulnerability details, risk assessments, and recommended solutions.
- **FastAPI Backend:** Leveraging FastAPI's performance, scalability, and ease of development.
- **React Frontend:** An intuitive user interface for initiating scans and viewing results (work in progress).

## Installation 🛠️

**Prerequisites:**

- Python 3.7+
- Node.js and npm (for the React frontend)
- OWASP ZAP (running in daemon mode)

**Steps:**

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd ZapScan
2. **Backend(FastAPI):**

   ```bash
   cd zapscan-env 
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. **Frontend(FastAPI)**

   ```bash
   cd zapscan-frontend
   npm install
4. **Configuration:**

   Open zapscan-env/config.py and replace YOUR_API_KEY with your actual ZAP API 
   key.
## Usage 🖥️

1.  **Start OWASP ZAP Daemon:**
    -   Follow the instructions in the [OWASP ZAP documentation](https://www.zaproxy.org/docs/docker/about/) to start ZAP in daemon mode.

2.  **Start Backend Server:**

    ```bash
    uvicorn app.main:app --reload  # From the root of zapscan-env directory
    ```

3.  **Start Frontend (Optional):**

    ```bash
    cd zapscan-frontend
    npm start  
    ```

4.  **Access the Scanner:**
    -   Open your browser and navigate to `http://localhost:8000` (or the appropriate port).
    -   If you have set up the react frontend, open the browser to `http://localhost:3000`

## Contributing 🤝

Contributions are welcome! Please feel free to submit issues, bug reports, or pull requests to improve ZapScan.

## License 📄

This project is licensed under the MIT License.

## Disclaimer ⚠️

ZapScan is intended for educational and testing purposes only. Use it responsibly and always obtain proper authorization before scanning any website.
