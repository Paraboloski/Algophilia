from pathlib import Path
from app.utils import Env


SEED = [
    Path("app/assets/templates/feats.yaml"),
    Path("app/assets/templates/items.yaml"),
    Path("app/assets/templates/souls.yaml"),
    Path("app/assets/templates/armors.yaml"),
    Path("app/assets/templates/spells.yaml"),
    Path("app/assets/templates/origins.yaml"),
    Path("app/assets/templates/weapons.yaml"),
    Path("app/assets/templates/conditions.yaml"),
    Path("app/assets/templates/knowledges.yaml"),
    Path("app/assets/templates/accessories.yaml"),
    Path("app/assets/templates/weapon_tags.yaml"),
]


class Settings:
    def __init__(self) -> None:
        env = Env()
        self.seed_files: list[Path] = SEED
        self.log_dir: str = "app/assets/logs"
        self.database_url: str = env.require("DATABASE_URL")
        self.telegram_token = env.get_env("TELEGRAM_TOKEN") 
        self.telegram_chat_id = env.get_env("TELEGRAM_CHAT_ID")
        self.schema_path: str = "app/assets/templates/schema.sql"


settings = Settings()