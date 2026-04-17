# Tech Stack Document - RPG Companion App

Questo documento delinea le tecnologie e le librerie scelte per lo sviluppo dell'app mobile utilizzando **Python** e **Flet**. La scelta è orientata alla velocità di esecuzione, alla facilità di manutenzione e alla compatibilità nativa con Android.

## 1. Core Framework & UI
* **Linguaggio:** [Python 3.10+](https://www.python.org/) - Linguaggio core per la logica di business.
* **UI Framework:** [Flet](https://flet.dev/) - Basato su Flutter, permette di creare interfacce professionali e reattive usando solo Python.
* **Design System:** [Material Design 3](https://m3.material.io/) - Integrato nativamente in Flet, garantisce un look & feel moderno su Android.

## 2. Data Persistence (Database)
Per un'app mobile di questo tipo, la persistenza locale è fondamentale.
* **SQLite:** Il database standard per mobile. Leggero, affidabile e non richiede un server.
* **SQLModel:** Una libreria che combina **SQLAlchemy** e **Pydantic**. È ideale per definire le schede dei personaggi come classi Python che diventano automaticamente tabelle del database.
* **Aiosqlite:** Se si desidera gestire le chiamate al database in modo asincrono per non bloccare la UI di Flet durante i salvataggi pesanti.

## 3. Data Validation & Models
* **Pydantic v2:** Essenziale per validare i dati inseriti dall'utente (es. assicurarsi che la Forza sia un numero tra 1 e 30) e per gestire la conversione dei dati tra database e interfaccia.

## 4. State Management
* **Flet PubSub / Control State:** Flet gestisce lo stato internamente. Per la gestione globale (es. "quale personaggio è attualmente selezionato?"), si consiglia un approccio a **Store centrale** o l'uso del sistema `page.session` di Flet.

## 5. Utility & Librerie Specifiche
* **Dadi (Dice Engine):** `random` (libreria standard) o la libreria `dice` per parsing di stringhe complesse come "2d20 + 5".
* **Gestione File/Asset:** `Pathlib` per gestire i percorsi delle icone e delle immagini dei personaggi in modo cross-platform.
* **Localization:** `gettext` o file JSON per supportare multilingua (Italiano/Inglese).

## 6. Development Tools & DevOps
* **Ambiente Virtuale:** `venv`per la gestione delle dipendenze.
* **Linting & Formattazione:** `Ruff` (estremamente veloce) o `Black` per mantenere il codice pulito.
* **Version Control:** Git con GitHub o GitLab.

## 7. Build & Deployment (Android)
* **Flet CLI:** Lo strumento principale per compilare l'app in un pacchetto `.apk` o `.aab`.
* **Serious Python:** Il bridge utilizzato internamente da Flet per far girare l'interprete Python su Android in modo efficiente.

## 8. Architettura Suggerita: MVC (Model-View-Controller)
Per evitare che il file `main.py` diventi ingestibile, la struttura consigliata è:
* **Models:** Classi SQLModel per Personaggi, Oggetti, Incantesimi.
* **Views:** Moduli Python separati per ogni schermata (Dashboard, Editor, Dice Roller).
* **Controllers/Logic:** Funzioni che gestiscono i calcolie le query al database.

---

## Sintesi della Stack
| Componente | Tecnologia Scelta |
| :--- | :--- |
| **UI** | Flet (Flutter) |
| **Logic** | Python |
| **Database** | SQLite + SQLModel |
| **Validation** | Pydantic |
| **Packaging** | Flet Build APK |
"""