CONDITIONS: list[dict] = [
    {
        "label": "Afferrato",
        "description": "Una creatura afferrata non può eseguire azioni di movimento finché l'effetto di questa condizione persiste. Ogni turno può eseguire una prova contrapposta di Forzare per divincolarsi.",
        "is_afflicted": False
    },
    {
        "label": "Amputazione",
        "description": (
            "Una creatura che vede amputato/e il/le braccio/a: dimezza i propri Slot di Carico."
            "Una creatura che vede amputata/e una/le gamba/e: dimezza la propria Resilienza per ogni gamba persa."
            "L'arto perso non può essere utilizzato e la CA è ridotta di 2 per ogni arto mancante."
        ),
        "is_afflicted": False
    },
    {
        "label": "Astinenza",
        "description": "Una creatura in astinenza deve superare una prova di Autocontrollo (CD 15, +1 per ogni giorno precedente) per ogni giorno trascorso senza la propria dose, altrimenti subisce -5 a tutte le azioni. Se le viene offerta la dipendenza, deve superare il test o assecondarla immediatamente. L'astinenza termina dopo 3 settimane senza aver assecondato il vizio.",
        "is_afflicted": False
    },
    {
        "label": "Avvelenato ",
        "description": "Una creatura avvelenata perde 1d4 PF all'inizio e fine del proprio turno. Subire l'avvelenamento mentre si è già afflitti da tale condizione causa lo stato Intossicato.",
        "is_afflicted": False
    },
    {
        "label": "Cecità",
        "description": "Una creatura accecata esegue tiri e prove sempre con svantaggio.",
        "is_afflicted": False
    },
    {
        "label": "Commozione cerebrale (x)",
        "description": "Una creatura con una commozione cerebrale non può eseguire azioni per X turni e vede la propria Difesa ridotta di 5. La condizione termina se la creatura viene attaccata.",
        "is_afflicted": False
    },
    {
        "label": "Confuso",
        "description": "Una creatura confusa, all'inizio del proprio turno, tira 1d6: 1-2-Si muove in una direzione determinata da 1d8. 3-4-Non compie azioni in questo turno. 5-6-Attacca la creatura più vicina con l'arma impugnata oppure se stessa.",
        "is_afflicted": False
    },
    {
        "label": "Emorragia",
        "description": "Una creatura in emorragia vede i propri PF max dimezzati. Una prova di Guarigione con successo critico declassa la condizione a Sanguinamento.",
        "is_afflicted": False
    },
    {
        "label": "Fame (1-4)",
        "description": "Una creatura affamata subisce effetti in base al livello. 1 (25%): . 2 (50%): . 3 (75%): . 4 (100%): Fallisce automaticamente tutte le prove relative ai propri Talenti. Dormire senza sfamarsi, ti porta al Martirio.",
        "is_afflicted": False
    },
    {
        "label": "Fotosensibile",
        "description": "Una creatura sensibile alla luce subisce una penalità di -3 alle prove di Intensità e Resilienza.",
        "is_afflicted": False
    },
    {
        "label": "Frattura",
        "description": "Una creatura con una frattura ha l'arto interessato compromesso. Le azioni che coinvolgono quell'arto hanno sempre svantaggio. Se non trattata, la condizione persiste e si evolve in Infezione.",
        "is_afflicted": False
    },
    {
        "label": "Infezione",
        "description": "Una creatura con un arto infetto entra in Martirio se non curata entro un numero di Turni Giornalieri pari a metà della propria Grinta (arrotondato per difetto, min 1) oppure se va a Dormire senza curare la condizione. Rimuovere l'arto infetto cura l'effetto.",
        "is_afflicted": False
    },
    {
        "label": "Intossicato",
        "description": "Una creatura intossicata perde PF all'inizio e alla fine del proprio turno. Il danno iniziale è di 1d4; ogni turno, il dado aumenta (1d6, 1d8, 1d10, 1d12, ecc.).",
        "is_afflicted": False
    },
    {
        "label": "Nausea",
        "description": "Una creatura nauseata può eseguire solo Azioni Semplici. Esegue una prova di Resistenza ogniqualvolta prova a sfamarsi; se fallisce, vomita e subisce 1d4 danni, aumentando di 1 stadio la Fame. Alla fine di ogni turno è possibile effettuare una prova di Guarigione; un successo critico rimuove del tutto l'effetto.",
        "is_afflicted": False
    },
    {
        "label": "Paralizzato",
        "description": "Una creatura paralizzata non può eseguire azioni, reazioni, muoversi o parlare. Fallisce automaticamente i tiri di Grinta e Resilienza. Gli attacchi contro di essa hanno vantaggio.",
        "is_afflicted": False
    },
    {
        "label": "Paura (1-4)",
        "description": "Una creatura spaventata subisce effetti in base al livello. 1 (25%): . 2 (50%): Ottiene il Talento Suicidio. 3 (75%): . 4 (100%): La fobia diventa Panophobia. Se la fobia è già Panophobia, esegue una prova di Autocontrollo; se fallisce, entra in Martirio.",
        "is_afflicted": False
    },
    {
        "label": "Prono",
        "description": "Una creatura prona concede un bonus di +2 a tutti gli attacchi effettuati contro di essa. Deve utilizzare la propria azione di movimento per rialzarsi.",
        "is_afflicted": False
    },
    {
        "label": "Sanguinamento",
        "description": "Una creatura sanguinante perde 1d4 PF all'inizio del proprio turno. Alla fine di ogni turno è possibile effettuare una prova di Guarigione; un successo critico rimuove del tutto l'effetto. Subire Sanguinamento mentre si è già afflitti da tale condizione causa lo stato Emorragia.",
        "is_afflicted": False
    },
    {
        "label": "Sorpreso",
        "description": "Una creatura sorpresa subisce -1 a tutti i tiri di attacco e difesa durante il proprio turno. I nemici hanno +1 agli attacchi contro di essa. L'effetto termina all'inizio del suo prossimo turno.",
        "is_afflicted": False
    },
    {
        "label": "Sovraccarico",
        "description": "Una creatura sovraccarica subisce -1 alle prove di Grinta e Tenacia per ogni 2 punti sopra i propri Slot di Carico e riduce la propria velocità dell'ammontare. Se 5 punti sopra, la creatura è immobilizzata dal proprio peso (velocità 0).",
        "is_afflicted": False
    },
    {
        "label": "Stato critico",
        "description": "Una creatura in stato critico subisce automaticamente danni critici da qualsiasi attacco. Subire 2 volte questa condizione porta la creatura a 1 PF.",
        "is_afflicted": False
    },
    {
        "label": "Ustione",
        "description": "Una creatura ustionata perde 2d6 PF all'inizio del proprio turno. È richiesta un'Azione Estrema per rimuovere la condizione.",
        "is_afflicted": False
    }
]