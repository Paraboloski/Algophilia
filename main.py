import sys
import logging
from Backend.api.data import Database
from Backend.api.service import seed

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
        stream=sys.stdout
    )

    init_result = Database.init_db()
    if init_result.is_err():
        print(f"Error initializing database: {init_result.unwrap_err()}")
        sys.exit(1)
    
    try:
        seed.run_seed()
    except Exception as e:
        print(f"An unexpected error occurred during seeding: {e}")
        sys.exit(1)
        
    print(f"App init OK!")

if __name__ == "__main__":
    main()
