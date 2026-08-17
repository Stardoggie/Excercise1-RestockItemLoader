How to Run (Windows):
  * CD to the 'warehouse_restock_manifest' folder and create the virtual environment using 'python -m venv .venv'.
  * Start the virtual environment using '.venv\Scripts\Activate.ps1', then cd back to the 'WareHouse_Restock_App folder'.
  * Install dependencies using the following commands:
    * 'pip install -e .' for normal dependencies
    * 'pip install -e ".[dev]"' for testing and dev dependencies
  * Run the program by using the command 'python main.py'
  * Run tests by using the command 'pytest -v'
