# UI/UX Design Document - Dashboard Personaggi
**Progetto:** RPG Companion App (Python + Flet)
**Schermata:** Home / Lista Personaggi (Populated State & Empty State)

## 1. Panoramica
Questa schermata rappresenta l'hub principale dell'applicazione. Permette all'utente di visualizzare i personaggi creati, cercarli tramite un'apposita barra e avviare il flusso per la creazione di un nuovo personaggio. È progettata con un approccio "Dark Mode first" per garantire un'estetica moderna e ridurre l'affaticamento visivo.

## 2. Palette Colori (Stima)
Il design utilizza una palette scura con accenti di colore rosso scuro/ruggine per le azioni principali.

* **Background (Sfondo):** Grigio molto scuro / Quasi Nero (es. `#181818` o `ft.colors.ON_INVERSE_SURFACE`)
* **Testo Principale:** Bianco puro (`#FFFFFF` o `ft.colors.WHITE`)
* **Testo Secondario:** Grigio chiaro (es. `#B0B0B0`)
* **Sfondo Search Bar:** Grigio chiaro con leggeri toni lavanda (es. `#EBE5F0`)
* **Accento / Call to Action (Pulsante & Bordo Attivo):** Rosso mattone / Ruggine (es. `#A9332D`)

## 3. Tipografia
* **Font Family:** Cinzel.
* **Stili:**
    * *Header ("CHARACTERS"):* Maiuscolo, tracking (spaziatura lettere) ampio, bold o semi-bold.
    * *Titoli Card ("Character Name"):* Regular/Medium, dimensione media.
    * *Dettagli Card ("Level: ? soul: ?..."):* Monospace o Sans-serif di piccole dimensioni, tutto in minuscolo o Capitalize.

## 4. Analisi dei Componenti UI

### 4.1. Header
* **Testo:** "CHARACTERS" centrato in alto.
* **Separatore:** Una linea orizzontale sottile centrata sotto il titolo (implementabile con `ft.Divider` in Flet con larghezza ridotta o un `ft.Container` con altezza 1px).

### 4.2. Barra di Ricerca (Search Bar)
* **Forma:** Forma a "pillola" (bordi completamente arrotondati, `border_radius=30`).
* **Layout interno (Row):**
    * *Sinistra:* Icona Menu ad hamburger (`ft.icons.MENU`) per possibili filtri aggiuntivi alla ricerca.
    * *Centro:* Campo di testo per l'input ("Search character name..."). In Flet sarà un `ft.TextField` con `border=ft.InputBorder.NONE`.
    * *Destra:* Icona della lente di ingrandimento (`ft.icons.SEARCH`).

### 4.3. Stato Vuoto (Empty State - Mockup 2)
* Visualizzato quando non ci sono personaggi nel database.
* **Testo:** "NO CHARACTERS :("
* **Posizione:** Centrato verticalmente e orizzontalmente nello spazio rimanente tra la search bar e il pulsante in basso.

### 4.4. Lista Personaggi (Populated State - Mockup 1)
* **Layout:** Una lista scorrevole verticalmente (`ft.ListView`).
* **Card Personaggio:**
    * **Sfondo:** Trasparente o leggermente più chiaro dello sfondo principale.
    * **Bordi:** Spessi e arrotondati (circa `border_radius=10`). Il colore del bordo è normalmente **Bianco**, ma diventa **Rosso** (rosso mattone) per indicare probabilmente l'ultimo personaggio usato, lo stato "selezionato" o "attivo".
    * **Contenuto (Row):**
        * *Avatar (Sinistra):* Un'icona utente (`ft.icons.PERSON_OUTLINE`) racchiusa in un quadrato con bordi molto arrotondati, spessore della linea marcato.
        * *Dati (Destra - Column):*
            * Riga 1: Nome del personaggio.
            * Riga 2: Statistiche rapide ("Level: ?", "soul: ?", "origins: ?"). Allineate orizzontalmente con un po' di spaziatura (`ft.Row` con `spacing`).

### 4.5. Pulsante "Create New Character" (Call to Action)
* **Posizione:** Fissato in fondo allo schermo (appiccicato in basso, fuori dallo scroll della lista).
* **Stile:** Pulsante a larghezza quasi totale (con margini laterali), bordi leggermente arrotondati.
* **Colore Sfondo:** Rosso mattone (uguale al bordo della card attiva).
* **Contenuto:** Un'icona "+" all'interno di un quadrato bianco (a sinistra) seguita dal testo in maiuscolo "CREATE NEW CHARACTER" (bianco).

## 5. Implementazione Consigliata in Flet

Per replicare esattamente questo design in Flet, suggerisco la seguente struttura gerarchica della Pagina:

```python
# Struttura concettuale Flet (Pseudocodice/Traccia)
import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#181818" # Sfondo scuro
    page.horizontal_alignment = "center"
    
    # 1. Header
    header = ft.Column([
        ft.Text("CHARACTERS", size=24, weight="bold", letter_spacing=2),
        ft.Container(width=150, height=1, bgcolor=ft.colors.WHITE54)
    ], horizontal_alignment="center")

    # 2. Search Bar
    search_bar = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.MENU, color=ft.colors.BLACK87),
            ft.TextField(hint_text="Search character name...", border="none", expand=True, color=ft.colors.BLACK87),
            ft.Icon(ft.icons.SEARCH, color=ft.colors.BLACK87)
        ]),
        bgcolor="#EBE5F0",
        border_radius=30,
        padding=ft.padding.symmetric(horizontal=15, vertical=5),
        margin=ft.margin.only(top=20, bottom=20)
    )

    # 3. Lista Personaggi o Empty State (Espandibile per occupare lo spazio centrale)
    # Usa un ft.Column(expand=True) o ft.ListView(expand=True)
    
    # Esempio Card:
    # ft.Container(
    #    border=ft.border.all(2, ft.colors.WHITE), # O colore rosso per attiva
    #    border_radius=10,
    #    content=ft.Row([... avatar e testi ...])
    # )

    # 4. Bottom Button
    create_btn = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.ADD_BOX_OUTLINED), # Icona approssimativa
            ft.Text("CREATE NEW CHARACTER", weight="bold")
        ], alignment="center"),
        bgcolor="#A9332D",
        padding=15,
        border_radius=10,
        margin=ft.margin.only(bottom=20)
    )

    # Aggiunta alla pagina (Stack o Column con l'area centrale expand=True)
    # page.add(...)