import sys
import logging
import asyncio
from middleware.db import Database
from Backend.api.service import seed
from middleware.config.core.logger import setup_logging

logger = logging.getLogger(__name__)

async def main():
    listener = setup_logging()

    try:
        logger.info("Avvio applicazione")

        logger.info("Inizializzazione database...")
        init_result = await Database.init_db()

        if init_result.is_err():
            logger.error("Errore durante l'inizializzazione del database: %s", init_result.unwrap_err())
            sys.exit(1)

        logger.info("Database inizializzato correttamente")

        logger.info("Avvio seed dati...")
        await seed.run_seed()
        logger.info("Seed completato con successo")
        logger.info("Esecuzione completata con successo")

    except Exception:
        logger.exception("Errore critico non gestito")
        sys.exit(1)

    finally:
        listener.stop()


if __name__ == "__main__":
    asyncio.run(main())
