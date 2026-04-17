# Algophilia 

```text
📦 algophilia
 ┣ 📂 Backend                   # Business logic 
 ┃ ┣ 📂 api                     # Core programming interface
 ┃ ┃ ┣ 📂 repository            # Data access layer (Repository Pattern)
 ┃ ┃ ┗ 📂 service               # Repo orchestrator
 ┃ ┗ 📂 router                  # Routing and Tabbing
 ┣ 📂 Frontend                  # Client application (User Interface)
 ┃ ┣ 📂 assets                  # Static resources (Fonts, Icons, Images)
 ┃ ┗ 📂 src                     # Interface source code
 ┃   ┣ 📂 components            # Reusable Atomic UI components and Layouts
 ┃   ┗ 📂 views                 # Main pages and design documentation
 ┣ 📂 middleware                # Intermediate layer between DB and Business Logic
 ┃ ┣ 📂 assets                  # Data models and templates management
 ┃ ┃ ┣ 📂 models                # Entity schema definitions (SQLAlchemy/Pydantic)
 ┃ ┃ ┗ 📂 templates             # Base structures for creating new objects
 ┃ ┣ 📂 config                  # System configurations and wrappers
 ┃ ┗ 📜 db.py                   # Database connection initialization and management (SQLite)
 ┣ 📜 main.py                   # Application entry point
 ┗ 📜 pyproject.toml            # Dependency management and Python configuration (uv)