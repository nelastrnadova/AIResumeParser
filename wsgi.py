import os

from dotenv import load_dotenv
from app import app

if __name__ == '__main__':
    load_dotenv()
    port = int(os.getenv("PORT", 5000))
    debug = bool(os.getenv("DEBUG", True))
    app.run(host='0.0.0.0', port=port, debug=debug)
