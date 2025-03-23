import subprocess
import sys
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_ezoptions():
    logging.info("Running ezoptions.py via Streamlit...")
    try:
        # Use sys.executable to ensure we use the same Python that’s running the script
        subprocess.check_call([sys.executable, "-m", "streamlit", "run", "https://raw.githubusercontent.com/pnebuloni/EzOptions/refs/heads/main/ezoptions.py"])
        logging.info("Successfully ran ezoptions.py using Streamlit.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running ezoptions.py: {e}")
        logging.error("Ensure Streamlit is installed and the URL is accessible. Install Streamlit with '{sys.executable} -m pip install streamlit'.")
        sys.exit(1)
    except FileNotFoundError:
        logging.error("Streamlit or Python not found. Ensure Streamlit is installed with '{sys.executable} -m pip install streamlit' and Python is available.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error running ezoptions.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
       run_ezoptions()
