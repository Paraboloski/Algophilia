# PRD - RPG Companion App (Android)

## 1. Introduzione
Il progetto consiste nello sviluppo di una **Companion App** per sistemi Android, realizzata in **Python** utilizzando il framework **Flet**. L'applicazione è progettata per assistere i giocatori di giochi di ruolo cartacei (es. D&D 5e, Pathfinder) nella gestione digitale delle proprie schede personaggio, inventari e statistiche in tempo reale durante le sessioni di gioco.

## 2. Obiettivi del Prodotto
* **Semplificazione:** Digitalizzare la scheda cartacea rendendo i calcoli automatici.
* **Portabilità:** Ottimizzata per dispositivi Android (smartphone e tablet).
* **Offline First:** Funzionamento completo senza necessità di connessione internet costante.
* **Personalizzazione:** Supporto per diversi personaggi e, potenzialmente, diversi sistemi di gioco.

## 3. Target Audience
* Giocatori di D&D e TTRPG che cercano un'alternativa digitale alle schede cartacee.
* Master (DM) che vogliono monitorare rapidamente i dati dei propri personaggi.

## 4. Requisiti Funzionali (User Stories)

### 4.1 Gestione Personaggi
* **Creazione Personaggio:** L'utente deve poter creare un nuovo personaggio inserendone gli attributi richiesti dal sistema.
* **Visualizzazione Lista:** Una dashboard iniziale con la lista di tutti i personaggi salvati.
* **Modifica/Eliminazione:** Possibilità di aggiornare i dati o eliminare una scheda obsoleta.

### 4.2 Scheda Statistiche (Core)
* **Caratteristiche:** Gestione di Grinta, Tenacia, Intensità e Resilienza
* **Punti Ferita (FP) e Punti Menta (PM):** Gestore dinamico per PF e PM correnti e massimi con visualizzazione grafica in stile videogioco(barra della vita con percentuale e comportamenti dinamici in base ad esso, ecc).
* **Classe Armatura (CA)** Campi dedicati per i valori di difesa e velocità.
* **Abilità (Skills):** Elenco dei Talenti e Incantesimi con selezione della competenza (proficiency / Knowledges).

### 4.3 Inventario e Equipaggiamento
* **Lista Oggetti:** Aggiunta di oggetti con nome, peso e descrizione.
* **Equipaggiamento Attivo:** Possibilità di segnare quali oggetti sono attualmente impugnati o indossati.

### 4.4 Utility di Gioco
* **Dice Roller:** Un lanciatore di dadi integrato (d4, d6, d8, d10, d12, d20, d100) con log dei risultati e gif / risultati.
* **Coin Flip:** Un lanciatore di monete integrato (testa, croce) con log dei risultati e gif / animazione.

## 5. Requisiti Non Funzionali

### 5.1 UI/UX
* **Design Responsivo:** L'interfaccia Flet deve adattarsi a diverse risoluzioni di schermi Android.
* **Dark Mode:** Supporto nativo per il tema scuro per risparmiare batteria e non affaticare la vista durante sessioni notturne.
* **Navigazione Intuitiva:** Uso di una `NavigationBar` inferiore o un `NavigationRail` laterale.

### 5.2 Prestazioni e Archiviazione
* **Persistenza Dati:** Utilizzo di **SQLite** locale per il salvataggio dei personaggi.
* **Velocità:** L'app deve avviarsi in meno di 1 secondo.

## 6. Specifiche Tecniche e Architettura
* **Linguaggio:** Python 3.14.4
* **Framework UI:** Flet (Flutter engine)
* **Database:** SQLite (tramite la libreria `sqlite3`)
* **Packaging:** `flet build apk` per la generazione del pacchetto Android.
* **Struttura Progetto:**
    * `/Backend`: Business logic, database e modelli e modelli (Character, Item, Spell).
    * `/Frontend`: Definizione delle schermate e dei componenti grafici.
    * `main.py`: Punto di ingresso dell'app.

## 7. User Journey (Flusso Utente)
1.  L'utente apre l'app e vede la lista dei personaggi (o uno stato vuoto).
2.  Clicca sul tasto per creare un personaggio.
3.  Inserisce i dati base e salva.
4.  Dalla dashboard, clicca sulla card del personaggio per aprire la scheda completa.
5.  Durante la sessione, modifica la scheda e il salvataggio è automatico.
6.  Opzionalmente, l'utente può anche eliminare quel personaggio.

## 8. Roadmap di Sviluppo
* **Fase 1 (MVP):** Creazione dei modelli.
* **Fase 2:** Implementazione della business logic.
* **Fase 3:** Costruzione delle interfaccie utente e dei componenti.
* **Fase 4:** Esportazione/Importazione schede in formato JSON.

## 9. Rischi e Mitigazione
* **Perdita Dati:** Implementare un sistema di backup semplice (esportazione file).
* **Limiti Flet su Mobile:** Alcune funzionalità hardware specifiche potrebbero richiedere integrazioni più complesse, ma per una scheda RPG le API standard sono sufficienti.
"""