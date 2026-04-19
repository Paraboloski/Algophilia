from src.data.models.skills import God

SPELLS: list[dict] = [
    # ── SULFUR ─────────────────────────────────────────────────────────────
    {
        "label": "Marcescenza",
        "affinity_with": God.SULFUR,
        "affinity_level": 1,
        "description": (
            "Fai marcire la vittima dall'interno per renderla vulnerabile agli attacchi. "
            "Aumentadi +1 il dado dei danni subiti dal nemico."
            "Se l'incantesimo viene usato su oggetti, ricevono danni doppi. L'incantesimo dura 1d4 turni."
        ),
        "enhancements": [
            {
                "label": "Putrefazione",
                "affinity_required": 2,
                "description": (
                    "Aumenta il dado dei danni subiti dal nemico di +2, invece di +1. "
                    "Se l'incantesimo viene usato su oggetti, ricevono danni tripli."
                ),
            },
            {
                "label": "Decomposizione",
                "affinity_required": 3,
                "description": (
                    "Aumenta il dado dei danni subiti dal nemico di +3, invece di +1. "
                    "Se l'incantesimo viene usato su oggetti, ricevono danni quadrupli."
                ),
            },
        ],
    },
    {
        "label": "Maestro dei parassiti",
        "affinity_with": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "Ottieni l'abilità di parlare con coloro che spesso passano inosservati."
            "Puoi evocare uno sciame di vermi per attaccare i nemici entro un raggio di 3m dal punto in cui li evochi."
            "I vermi possono causare un effetto casuale determinato da 1d4, che può essere Confusione, Avvelenamento, Nausea o Nulla."
            "Tutte le creature all'interno dell'area e tutte le creature che vi entrano, devono eseguire una prova di Evasione contrapposta alla tua Evocazione per evitare di venir attaccati dai vermi."
            "L'effetto termina alla fine della scena."
        ),
        "enhancements": [
            {
                "label": "Re dei parassiti",
                "affinity_required": 3,
                "description": (
                    "Puoi fare 3 domande a parassiti come ratti o insetti; risponderanno sinceramente secondo le loro conoscenze."
                    "Inoltre, possono sacrificarsi come azione Complessa per nutrirti fungendo da Cibo di Grado 0."
                ),
            },
            {
                "label": "Vero Re dei parassiti",
                "affinity_required": 3,
                "description": (
                    "Le possibili condizioni causate dai vermi vengono determinata da 3d4 invece che 1d4."
                ),
            },
        ],
    },
    {
        "label": "Branco di Ratti",
        "affinity_with": God.SULFUR,
        "affinity_level": 3,
        "description": (
            "Evoca un branco di ratti per disturbare i nemici."
            "Tutti i nemici entro un raggio di 3m dalla zona di evocazione scelta devono eseguire una prova di Evasione contrapposta alla tua Evocazione."
            "Se falliscono, subiscono tutti 1d6 danni magici e sono Confusi. "
        ),
        "enhancements": [],
    },
    {
        "label": "Sciame di Locuste",
        "affinity_with": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "Evoca uno sciame di locuste per disturbare il nemico. Infliggi l'effetto confusione sul bersaglio."
        ),
        "enhancements": [
            {
                "label": "Piaga delle locuste",
                "affinity_required": 3,
                "description": "Infliggi 1d6 danni a turno fino alla fine della scena.",
            },
        ],
    },
    {
        "label": "Stormo di Corvi",
        "affinity_with": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "Evoca 2 corvi che volano verso il tuo nemico e tentano di farlo a pezzi."
            "Scegli 1 o 2 parti del corpo bersaglio ed esse verranno attaccatate, infliggendo 1d4 danni per corvo."
            "Non può fallire."
        ),
        "enhancements": [
            {
                "label": "Corvi letali",
                "affinity_required": 3,
                "description": (
                    "Ogni corvo infligge 2d4 danni invece che 1d4."
                    "Se scegli come bersaglio da colpire la testa, il bersaglio dovrà effettuare una prova di Evasione contrapposta alla tua Evocazione per evitare di venir accecato."
                ),
            },
        ],
    },

    # ── HASTUR ─────────────────────────────────────────────────────────────
    {
        "label": "Portale di Sangue",
        "affinity_with": God.HASTUR,
        "affinity_level": 1,
        "description": (
            "Presso un cerchio rituale, puoi pagare 10Pf per evocare un porta spazio-temporale."
            "Il portale collega tutti i cerchi rituali dello stesso tipo, permettendoti di viaggiare liberamente tra di essi."
        ),
        "enhancements": [],
    },
    {
        "label": "Spada di Sangue",
        "affinity_with": God.HASTUR,
        "affinity_level": 1,
        "description": (
            "Sacrifica 10PF: Evochi una spada dal tuo stesso sangue che infligge danni magici pari a 1d8."
            "Questa spada dura fino alla fine della scena."
            "Non puoi evocare l'arma se stai già impugnando un altra arma."
        ),
        "enhancements": [
            {
                "label": "Spada della passione",
                "affinity_required": 2,
                "description": "Puoi pagare altri 10PF aggiuntivi per aumentare i danni della spada di 2d8 invece di 1d8 permanentemente.",
            },
            {
                "label": "Lancia di Longino",
                "affinity_required": 3,
                "description": (
                    "Puoi pagare 30PF totali e, al posto che una spada, evochi una lancia di sangue che infligge 2d8 danni perforanti e 1d8 danni magici."
                    "Ogniqualvolta effettui un attacco con la lancia, ottieni +1 Grinta (fino a un massimo di 4) e puoi lanciare la lancia (a una distanza pari alla tua Grinta in linea retta) contro un nemico infliggendo danni doppi(tuttavia, perdi la tua lancia a prescindere se colpisci o meno)."
                )
            },
        ],
    },
    {
        "label": "Corona di Spine",
        "affinity_with": God.HASTUR,
        "affinity_level": 3,
        "description": (
            "Selezioni un bersaglio entro la tua Tenacia in m."
            "Evochi una corona di spine che si avvinghia alla testa del bersaglio."
            "Ogniqualvolta ricevi un qualsiasi danno, 1/2 viene inflitto al bersaglio selezionato come danno magico."
        ),
        "enhancements": [
            {
                "label": "Il Dolore della Croce",
                "affinity_required": 3,
                "description": (
                    "Selezioni un bersaglio entro la tua Tenacia in m."
                    "Una croce inquietante ti inchioda ad essa, impedendoti di eseguire azioni di Movimento. La croce svanisce alla fine della scena."
                    "Ogniqualvolta ricevi un qualsiasi danno, l'intero ammontare viene inflitto al bersaglio selezionato come danno magico."
                ),
            },
        ],
    },
    {
        "label": "Golem di Sangue",
        "affinity_with": God.HASTUR,
        "affinity_level": 2,
        "description": (
            "Sacrifica PF per evocare un golem che combatta temporaneamente al tuo fianco."
            "Crei un Golem di Carne e Sangue che obbedisce a tutti i tuoi comandi. I PF del Golem sono pari ai PF sacrificati per evocarlo."
            "Puoi ordinare di attaccare usando un'Azione Semplice. Ha un bonus per colpire pari alla tua Tenacia e il suo pugno infligge 1d12 danni."
        ),
        "enhancements": [
            {
                "label": "Bodyguard",
                "affinity_required": 3,
                "description": (
                    "Ogniqualvolta gli ordini di attaccare usando un'Azione Semplice, effettua due colpi al posto di 1."
                ),
            },
            {
                "label": "Assassino",
                "affinity_required": 3,
                "description": "I danni del pugno del golem aumentano a 2d8 invece di 1d12.",
            },
        ],
    },

    # ── New Gods ──────────────────────────────────────────────────────────────
    {
        "label": "Radiazione",
        "affinity_with": God.NEW_GODS,
        "affinity_level": 1,
        "description": (
            "Fa brillare una luce fragorosa in un raggio di 5m. Applichi la condizione Fotosensibile a tutte le creature in quella zona."
        ),
        "enhancements": [],
    },
    {
        "label": "Rivela Aura",
        "affinity_with": God.NEW_GODS,
        "affinity_level": 1,
        "description": (
            "Puoi percepire la presenza di nemici intorno a te. Entro un raggio di 20m puoi localizzare tutti i nemici con "
            "un Livello di Minaccia pari alla metà del tuo valore di Tenacia."
            "Conosci il loro Livello di Minaccia e dove si trovano."
        ),
        "enhancements": [],
    },
    {
        "label": "Leggimente",
        "affinity_with": God.NEW_GODS,
        "affinity_level": 2,
        "description": (
            "Ogniqualvolta effettui una prova di Parlare puoi, invece, leggere i pensieri della creatura bersaglio."
            "Fallire la prova, tuttavia, metterà in allerta il bersaglio."
        ),
        "enhancements": [],
    },

    {
        "label": "Incatenare",
        "affinity_with": God.NEW_GODS,
        "affinity_level": 1,
        "description": (
            "Catene saltano fuori dal terreno e legano il nemico a te."
            "Applichi la condizione Afferrato al bersaglio e a te stesso."
        ),
        "enhancements": [
            {
                "label": "Catene demoniache",
                "affinity_required": 2,
                "description": "Applica Paralizzato invece di Afferrato.",
            },
        ],
    },
    {
        "label": "Illuminazione di Betel",
        "affinity_with": God.NEW_GODS,
        "affinity_level": 2,
        "description": (
            "La luce di Betel potenzia la tua natura magica."
            "Riduci il costo di tutti gli effetti potenziati di -2 fino alla fine della scena."
        ),
        "enhancements": [],
    },
    {
        "label": "Catene del Tormento",
        "affinity_with": God.NEW_GODS,
        "affinity_level": 3,
        "description": (
            "Evochi le catene che hanno tormentato Ronn Chambara il Tormentato per centinaia di anni. "
            "Infliggi ad una creatura bersaglio e a te stesso 3d12 danni magici."
        ),
        "enhancements": [
            {
                "label": "Tritacarne",
                "affinity_required": 3,
                "description": "Applichi la condizione Critica al bersaglio e a te stesso.",
            },
        ],
    },

    # ── MARDUK ───────────────────────────────────────────────────────────────
    {
        "label": "Feromoni",
        "affinity_with": God.MARDUK,
        "affinity_level": 1,
        "description": (
            "Rilascio di feromoni che spinge l'avversario a deviare tutta l'attenzione verso di te"
            "Tutti i nemici che tentano di attaccare devono effettuare una prova di Comprensione contrapposta alla tua Evocazione e, in caso di fallimento, saranno costretti a scegliere te come unico bersaglio."
        ),
        "enhancements": [
            {
                "label": "Ormoni ammalianti",
                "affinity_required": 3,
                "description": (
                    "Puoi scegliere una qualunque creatura alleata per rilasciare i feronomi."
                ),
            },
        ],
    },
    {
        "label": "Sussurri Amorevoli",
        "affinity_with": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Curi 2d10+5 PF di un alleato scelto entro 5m da te."
        ),
        "enhancements": [
            {
                "label": "Dichiarazione d'amore",
                "affinity_required": 3,
                "description": "Aumenta il recupero a 4d10. Puoi scegliere come bersaglio dell'incantesimo tutte le creature alleate nella zona di evocazione.",
            },
        ],
    },
    {
        "label": "Fiore Cerebrale",
        "affinity_with": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Pianta il seme di Fiore Celebrale in una creatura bersaglio."
            "La creatura dovrà eseguire una prova di Guarigione contrapposta alla tua Evocazione per evitare di venir inseminata"
            "Se fallisce, ogni recuperi 1d6 PM."
        ),
        "enhancements": [],
    },
    {
        "label": "Fiore Cardiaco",
        "affinity_with": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Pianta il seme di Fiore Cardiaco in una creatura bersaglio."
            "La creatura dovrà eseguire una prova di Guarigione contrapposta alla tua Evocazione per evitare di venir inseminata"
            "Se fallisce, ogni recuperi 2d6 PF."
        ),
        "enhancements": [],
    },

    {
        "label": "Radici Mietitrici",
        "affinity_with": God.MARDUK,
        "affinity_level": 1,
        "description": (
            "Evochi radici dal terreno che squarciano tutto ciò che incontrano."
            "Tutti i nemici entro un raggio di 3m da te devono effettuare una prova di Evasione contro la tua abilità di Evocazione."
            "Se falliscono, subiscono 4d4 danni magici e subiscono la condizione fratturato."
        ),
        "enhancements": [
            {
                "label": "Radicamento",
                "affinity_required": 2,
                "description": (
                    "Puoi distruggere istantaneamente oggetti inorganici come pareti di pietra, terra, o legno."
                    "La quantità che puoi rompere è pari alla metà del tuo valore di Tenacia in altezza, larghezza e lunghezza."
                ),
            },
        ],
    },

    # ── Gro-goroth ────────────────────────────────────────────────────────────
    {
        "label": "Necromanzia",
        "affinity_with": God.GORGOROTH,
        "affinity_level": 1,
        "description": (
            "Catturi un anima dispersa e la rinchiudi dove originariamente viveva."
            "Esegui una prova di Evocazione: Puoi riportare in vita un nemico che ha un Livello di Minaccia uguale o inferiore a 1/4 del tuo valore di Tenacia come tuo servitore fino a riposo lungo."
            "Fallire la prova potrebbe comportare rendere ostile la creatura resuscitata."
            "Se la creatura resuscitata muore di nuovo mentre è sotto l'effetto di questo incantesimo, non può essere resuscitato tramite necromanzia, e questo incantesimo non funziona sui personaggi giocabili."
            "Puoi avere un numero di servitori zombie pari al tuo livello. "
            "Ordinare alle creature di attaccare in una scena di combattimento richiede un Azione Semplice."
        ),
        "enhancements": [
            {
                "label": "Necromanzia avanzata",
                "affinity_required": 3,
                "description": (
                    "puoi riportare in vita un nemico che ha un Livello di Minaccia uguale o inferiore a 1/2 del tuo valore di Tenacia."
                ),
            },
        ],
    },

    {
        "label": "Piromazia",
        "affinity_with": God.GORGOROTH,
        "affinity_level": 2,
        "description": (
            "Infliggi 2d4 danni fuoco ad una creatura bersaglio e applichi Ustione. Puoi dare fuoco a qualcosa di infiammabile."
        ),
        "enhancements": [
            {
                "label": "Palla di fuoco",
                "affinity_required": 3,
                "description": "Evochi un enorme sfera infuocata che infligge 4d4 danni fuoco a tutte le creature del raggio di 8m da dove lanci l'incantesimo.",
            },
        ],
    },
    {
        "label": "Terra Bruciata",
        "affinity_with": God.GORGOROTH,
        "affinity_level": 2,
        "description": (
            "Brucia completamente i dintorni per creare un ambiente vulcanico. "
            "Infliggi l'effetto Ustione su chiunque entro un'area di 6 m di raggio, siano essi nemici o alleati."
            "Si può eseguire una prova di evasione per uscire immediatamente dal raggio d'azione dell'incantesimo ma con una penalità di -2."
        ),
        "enhancements": [
            {
                "label": "Terremoto",
                "affinity_required": 3,
                "description": "La penalità aumenta a -5 invece di -2.",
            },
        ],
    },
    {
        "label": "Dolore",
        "affinity_with": God.GORGOROTH,
        "affinity_level": 1,
        "description": (
            "Crea un vortice devastante dai tuoi sentimenti concentrati di dolore e odio."
            "Infliggi 1d8 + valore di Tenacia in danni fisici (Contundente, Tagliente o Perforante a tua scelta)."
        ),
        "enhancements": [
            {
                "label": "Doppio Dolore",
                "affinity_required": 2,
                "description": "Puoi selezionare fino a 2 bersagli contemporaneamente.",
            },
            {
                "label": "Odio e Dolore",
                "affinity_required": 3,
                "description": "Al costo di 1 pt. Sopravvivenza puoi amputare un arto casuale alle creature bersaglio da questo incantesimo.",
            },
        ],
    },
    {
        "label": "Nebbia oscura",
        "affinity_with": God.GORGOROTH,
        "affinity_level": 2,
        "description": (
            "Evochi una nube tossica e oscura."
            "Accechi tutti i nemici entro un raggio di 3m infliggi 1d4 -2 (minimo 0) danni alla testa."
            "Tutte le creature all'interno del raggio devono eseguire una prova di Evasione per uscire immediatamente dall'area."
        ),
        "enhancements": [
            {
                "label": "Smog",
                "affinity_required": 3,
                "description": "Se una creatura rimane nell'area della nube per almeno un turno, subisce la condizione Avvelenato.",
            },
        ],
    },
    {
        "label": "Buco Nero",
        "affinity_with": God.GORGOROTH,
        "affinity_level": 3,
        "description": (
            "Un'energia negativa concentrata che può essere scagliata contro un bersaglio più volte "
            "Effettui 4 attacchi contro un bersaglio mirando a parti del corpo random."
            "Per ogni attacco, il bersaglio dovrà eseguire una prova di Evasione per evitare di venir colpito."
            "Ogni attacco a segno infligge 3d6 danni magici."
        ),
        "enhancements": [
            {
                "label": "Materia Oscura",
                "affinity_required": 3,
                "description": (
                    "Tutte le prove di Evasione eseguite dal bersaglio di questo incantesimo sono con svantaggio."
                ),
            },
        ],
    },
]
