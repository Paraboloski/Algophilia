FEATS: list[dict] = [
    {
        "name": "Accademico",
        "description": (
            "Ottieni vantaggio in tutte le prove di Tenacia nelle quali possiedi competenza."
        ),
    },
    {
        "name": "Acrobata",
        "description": (
            "Alzarti in piedi dalla condizione di prono non consuma alcuna azione. Inoltre, ottieni un bonus di +2 alle prove di Movimento."
        ),
    },
    {
        "name": "Alchimista",
        "description": (
            "Impiegando un'Azione Estrema, puoi combinare due erbe o due pozioni per fonderne gli effetti in un unico intruglio, ottimizzando l'economia delle tue azioni. "
            "Non è possibile mescolare composti già alterati. Ottieni inoltre un bonus di +3 alle prove di Artigianato per la creazione di oggetti alchemici."
        ),
    },
    {
        "name": "Analizzare",
        "description": (
            "Spendi un'Azione Estrema per effettuare una prova di Guarigione contrapposta alla Percezione del bersaglio. "
            "In caso di successo, identifichi un punto debole su un suo arto: la CA di tale arto si riduce di un valore pari alla tua Intensità e i danni inflitti in quell'area raddoppiano. "
            "In caso di fallimento, l'Azione Estrema va perduta e subisci penalità."
        ),
    },
    {
        "name": "Armiere",
        "description": (
            "La penalità inflitta dall'indossare armature si riduce di 2. Inoltre, l'armatura indossata conferisce un ulteriore bonus di +1 alla Difesa offerta e al bonus CA."
        ),
    },
    {
        "name": "Attaccabrighe",
        "description": (
            "Quando metti a segno un attacco senz'armi nel tuo turno, puoi tentare una prova di Uccisione per Afferrare il bersaglio spendendo un'Azione Complessa."
        ),
    },
    {
        "name": "Botanica Avanzata",
        "description": (
            "Apprendi i seguenti diagrammi di creazione: Elisir Viola, Elisir di Serpente, Elisir Rosso ed Elisir Torbido. "
            "Quando fabbrichi questi preparati, il costo dei materiali di creazione si riduce di 1."
        ),
    },
    {
        "name": "Carismatico",
        "description": (
            "Ottieni sempre vantaggio nelle prove di Parlare."
        ),
    },
    {
        "name": "Colpo Perforante",
        "description": (
            "Se il tuo attacco porta a 0 i PF di un avversario, puoi concatenare immediatamente un colpo aggiuntivo contro un altro bersaglio nelle prossimità (devi comunque eseguire il TPC) come azione Semplice extra."
        ),
    },
    {
        "name": "Creazione Trappole",
        "description": (
            "Apprendi i seguenti diagrammi di creazione: Trappola per orsi, Trappola botola, Punte camuffate"
            "Quando fabbrichi queste trappole, il costo dei materiali di creazione si riduce di 1."
        ),
    },
    {
        "name": "Diagnosi",
        "description": (
            "Ottieni vantaggio in qualsiasi prova di Guarigione effettuata per analizzare un corpo o un paziente. "
            "In caso di successo, determini la causa del decesso, l'arma inflitta, l'ultima azione compiuta dal soggetto prima di spirare e le sue eventuali Resistenze o Debolezze fisiologiche."
        ),
    },
    {
        "name": "Diplomazia",
        "description": (
            "All'inizio di uno scontro con una creatura senziente non palesemente votata al tuo immediato sterminio, puoi effettuare una prova di Parlare come azione Semplice extra, contrapposta alla Comprensione del bersaglio. "
            "In caso di successo, il nemico viene considerato Sorpreso. Se superi la prova del nemico di almeno 5 punti, quest'ultimo desisterà definitivamente dai propri intenti ostili."
        ),
    },
    {
        "name": "Divorare",
        "description": (
            "Ottieni la macabra capacità di nutrirti di cadaveri crudi. Così facendo, sazi la tua Fame di un valore pari alla metà del Grado di Sfida della creatura (minimo 1). "
            "Tuttavia, perdi un ammontare di PM pari a 2dX, dove 'X' equivale al dado di Presenza terrificante del nemico divorato (usa 1d4 se si tratta di un essere umano)."
        ),
    },
    {
        "name": "Domatore di bestie",
        "description": (
            "Ottieni sempre vantaggio in qualsiasi prova che implichi l'interazione o l'addestramento degli Animali."
        ),
    },
    {
        "name": "Duro a Morire",
        "description": (
            "Se un danno letale dovesse farti scendere a 0 PF, resti invece a 1 PF (una sola volta per Riposo Lungo). "
            "Hai bisogno di un successo in meno per uscire dallo stato di Martirio."
        ),
    },
    {
        "name": "En Garde",
        "description": (
            "Se agisci per primo in ordine di Iniziativa, puoi sferrare un attacco con l'arma che impugni spendendo un'azione Semplice extra. "
            "Questo colpo subisce Svantaggio al TPC e infliggerà sempre la metà dei danni originali."
        ),
    },
    {
        "name": "Esecutore",
        "description": (
            "Ogni volta che un dado danno della tua arma ottiene il valore massimo possibile, puoi tirarlo nuovamente e sommarne il risultato al totale."
        ),
    },
    {
        "name": "Esplosivi",
        "description": (
            "Apprendi i diagrammi per la fabbricazione dei seguenti ordigni: Molotov, TNT, Bomba Fumogena, Bomba Accecante e Bomba a Gas. "
            "Il costo dei materiali necessari per l'assemblaggio di questi dispositivi esplosivi si riduce di 1."
        ),
    },
    {
        "name": "Fabbricazione Armi",
        "description": (
            "Puoi applicare 3 miglioramenti su armi diversi a tua scelta come azione durante una scena di Riposo."
        ),
    },
    {
        "name": "Ferocia sconsiderata",
        "description": (
            "Prima di compiere un attacco, puoi dichiarare di subire una penalità di -5 al TPC. "
            "Se l'attacco va comunque a segno, aggiungi 2 dadi danni."
        ),
    },
    {
        "name": "Flagellante",
        "description": (
            "Per ogni condizione negativa o malus che ti affligge, ottieni un bonus cumulativo di +1 al TPC. "
            "Benefici inoltre di un +1 alle prove di Resistenza per la sopportazione del dolore."
        ),
    },
    {
        "name": "Forgia Magika",
        "description": (
            "Sfutta un azione durante una scena di Riposo per selezionare un Incantesimo che conosci e una delle seguenti proprietà: "
            "1) Istantaneo: lanci l'incantesimo all'inizio del turno come azione gratuita (pagando comunque i PM). "
            "2) Caos: il danno e il costo in PM verranno raddoppiati. "
            "3) Semplice: il lancio ti costerà solo la metà dei normali PM (minimo 1)."
        ),
    },
    {
        "name": "Forte",
        "description": (
            "i tuoi PF max aumentano permanentemente di +10"
            "I danni base delle tue armi da mischia aumentano di un dado addizionale. "
            "Ricevi un bonus di +2 a tutti i TPC in mischia e +1 nelle prove di Resistenza."
        ),
    },
    {
        "name": "Fortunato",
        "description": (
            "Puoi ripetere un singolo tiro di dado o moneta per ogni Scena di Riposo. "
            "Ogniqualvolta tiri con critico naturale, ottieni un utilizzo aggiuntivo di questo Talento."
        ),
    },
    {
        "name": "Furtivo",
        "description": (
            "Nel calcolo dei tuoi Sotterfugi, aggiungi sempre un 1d10. "
            "Ottieni inoltre un bonus di +3 alle prove di Nascondersi."
        ),
    },
    {
        "name": "Grido di Guerra",
        "description": (
            "Consumando un'azione di turno completo, effettua una prova di Comprensione con bonus pari al numero dei tuoi alleati in campo."
            "Se hai successo, diventi l'unico bersaglio di tutti gli attacchi avversari per i successivi 3 turni"
            "Durante questo periodo, ottieni Resistenza a tutti i danni in mischia. Attivabile una volta per scena."
        ),
    },
    {
        "name": "Guardia Perfetta",
        "description": (
            "Spendi un'Azione Complessa per assumere una postura di 'Guardia'. "
            "Finché resti in questa postura, supererai istantaneamente, tutti gli attacchi inarrestabili."
        ),
    },
    {
        "name": "Guaritore",
        "description": (
            "Una volta per Riposo Lungo, impiegando un'Azione Complessa, puoi purificare completamente un compagno da qualsiasi condizione o effetto negativo. "
            "Ricevi un bonus passivo di +2 in tutte le prove di Guarigione."
        ),
    },
    {
        "name": "Guerriero Oscuro",
        "description": (
            "Non subisci Svantaggio né alcuna penalità quando la tua visuale è ostacolata. "
            "Benefici inoltre di un bonus di +3 ai TPC negli scontri che si svolgono in ambienti avvolti dall'oscurità."
        ),
    },
    {
        "name": "Incisione",
        "description": (
            "Durante un Riposo, puoi consumare un'azione per incidere il marchio di una Divinità sulla pelle di un alleato a tua scelta. "
            "Richiede una prova di Evocazione da parte tua contrapposta a un TS su Resistenza del bersaglio. "
            "Per ogni punto in più, l'alleato beneficia di un incremento di +1 a un Attributo a sua scelta. "
            "L'effetto svanisce al termine del successivo Riposo; un alleato non può ricevere più di un'incisione contemporaneamente."
        ),
    },
    {
        "name": "Insonnia",
        "description": (
            "Durante i Riposi, disponi di un'azione Semplice extra da impiegare liberamente. "
            "Tuttavia, non potrai utilizzarla per dormire, e il suo utilizzo ti affligge con un malus di -1 a tutti i tiri successivi (penalità che svanisce solo dopo esserti dedicato all'azione Dormire in un futuro Riposo). "
            "Ricevi +3 ai TS contro sonno indotto, magie d'ammaliamento e manipolazioni oniriche."
        ),
    },
    {
        "name": "Intento Omicida",
        "description": (
            "Nel tuo primo turno di combattimento, puoi sprigionare la tua sete di sangue. Come Azione Gratuita, effettua una prova di Intimidire contrapposta alla Comprensione del bersaglio. "
            "Se prevali, costringi la creatura a compiere soltanto Azioni Semplici per tutto il resto dello scontro. Ricevi un bonus di +3 alle prove di Intimidazione."
        ),
    },
    {
        "name": "Intuitivo",
        "description": (
            "Una volta per Riposo, puoi spendere 5 PM per avere una profonda epifania: il GM ti rivelerà un indizio o una delucidazione in merito agli eventi delle scene trascorse. "
            "Ricevi un bonus di +3 alle prove di Percezione."
        ),
    },
    {
        "name": "Lancio dell'Arma",
        "description": (
            "Consideri ogni oggetto contundente come un'arma da lancio e puoi estrarre armi Lanciabili come azione gratuita."
            "I tuoi attacchi da lancio infliggono 1 dado di danno extra e, in caso di successo, hanno una probabilità del 25% di applicare la condizione Commozione."
        ),
    },
    {
        "name": "Le Danse Macabre",
        "description": (
            "Impiegando un'Azione Semplice, fino all'inizio del tuo turno successivo, ottieni un bonus di +3 a tutte le prove di Evocazione e ai danni di origine magica che infliggi."
        ),
    },
    {
        "name": "Magna-Medica",
        "description": (
            "Mediante un'Azione Estrema, puoi trasferire i tuoi PF a un alleato adiacente. "
            "Per ogni 2 PF che sacrifichi volontariamente, l'alleato recupera 1 PF. "
            "Puoi incanalare su di te le condizioni negative o gli status del compagno guarito (incluso lo stato di MORTE)."
        ),
    },
    {
        "name": "Mano lesta",
        "description": (
            "Ottieni vantaggio in tutte le prove per scassinare serrature, borseggiare o eseguire giochi di prestigio."
        ),
    },
    {
        "name": "Masterchef",
        "description": (
            "Durante una Scena di Riposo, ti è permesso eseguire l'Azione Cucinare per due volte, o in alternativa eseguirla e compiere una seconda e diversa azione senza limitazioni."
        ),
    },
    {
        "name": "Meditazione",
        "description": (
            "Durante una Scena di Riposo, usi un azione per selezionare un incantesimo che conosci."
            "Potrai lanciarlo a costo zero una volta prima del successivo Riposo."
        ),
    },
    {
        "name": "Metabolismo Lento",
        "description": (
            "Una volta per scena, superando un TS di Resistenza, puoi recuperare 1 punto Fame. "
            "Puoi usare questo talento solo se hai perso almeno 1 punto Fame durante la transizione tra la scena precedente e l'attuale."
        ),
    },
    {
        "name": "Occultismo Avanzato",
        "description": (
            "Ogniqualvolta attivi l'effetto potenziato di una magia, lancia una moneta. Se indovini l'esito, l'incantesimo non consuma il suo normale costo di lancio."
        ),
    },
    {
        "name": "Opportunista",
        "description": (
            "Se un nemico nella tua portata di mischia fallisce un attacco contro di te oppure ogniqualvolta una creatura cerca di fuggire, puoi usare la tua reazione (Azione Semplice fuori dal turno) per sferrare un attacco contro di essa."
            "Ottieni inoltre un bonus di +2 nelle prove contro bersagli resi vulnerabili."
        ),
    },
    {
        "name": "Ordine, Comando:",
        "description": (
            "Impiegando un'Azione Complessa (utilizzabile per scena un numero di volte pari alla tua Intensità), esegui una prova di Parlare contrapposta alla Comprensione di un alleato. "
            "In caso di successo, l'alleato esegue un'azione a sua scelta con vantaggio. Il compagno può decidere di fallire volontariamente subendo danni ai PM pari alla tua Intensità."
        ),
    },
    {
        "name": "Piano di Fuga",
        "description": (
            "La tua velocità di Corsa equivale ora al triplo della tua normale velocità di Camminata. "
            "Ottieni inoltre un bonus di +2 alle prove per divincolarti, sfuggire agli avversari o superare limitazioni fisiche di movimento."
        ),
    },
    {
        "name": "Postura di Precisione",
        "description": (
            "Quando brandisci un'arma che infligge danni Perforanti, puoi consumare un numero a tua scelta di azioni (X) durante il tuo turno per stabilizzarti, prendendo la mira."
            "Ricevi un bonus cumulativo di +1 al tuo prossimo TPC per ogni singola azione sacrificata nel mantenimento di questa postura."
        ),
    },
    {
        "name": "Postura Rapida",
        "description": (
            "Durante uno scontro, puoi spendere un'Azione Estrema per adottare una postura fluida e reattiva. "
            "Finché la mantieni attiva, benefici di un'Azione Semplice extra a ogni tuo turno. "
            "L'esecuzione di un'Azione Complessa o di spostamento interromperà istantaneamente l'effetto. Questa guardia può essere assunta una sola volta per scena."
        ),
    },
    {
        "name": "Pugile",
        "description": (
            "I tuoi colpi senz'armi infliggono 1d6 danni Contundenti e acquisiscono la proprietà Pesante. Ogniqualvolta sferri un colpo senz'armi, puoi effettuarne uno consecutivo subendo svantaggio. "
            "Se selezioni questo Talento più volte, il dado di danno aumenta a 1d8 (seconda volta) o 1d10 (terza volta). "
            "Per ogni grado acquisito in questo Talento, ottieni un bonus cumulativo di +1 alle prove di Uccisione per il resto della scena (massimo di +3)."
        ),
    },
    {
        "name": "Punta Avvelenata",
        "description": (
            "ogni arma o strumento in tuo possesso capace di causare la condizione Avvelenato infligge invece, la condizione Intossicato."
        ),
    },
    {
        "name": "Sacrificio di Sangue",
        "description": (
            "Tramite un'Azione Complessa, puoi sacrificare PF per stringere un legame di affinità temporaneo con una Divinità a tua scelta (10PF x lv). "
            "Perdi l'affinità ottenuto tramite questo Talento alla fine della scena."
        ),
    },
    {
        "name": "Scarica d'Adrenalina",
        "description": (
            "Durante una scena di combattimento, se i tuoi PF scendono alla metà del tuo massimo o meno, puoi eseguire un azione di movimento come azione Semplice extra."
        ),
    },
    {
        "name": "Schivare e colpire",
        "description": (
            "La disperazione affina i tuoi riflessi: se i tuoi PF sono pari o inferiori alla metà del tuo massimo, ottieni vantaggio in tutte le prove di Evasione."
        ),
    },
    {
        "name": "Seppellire il Trauma",
        "description": (
            "Diventi immune alle penalità derivanti dalla tua Fobia. Inoltre, dimezzi la naturale perdita di PM legata all'aumento della Paura."
        ),
    },
    {
        "name": "Sigillo di Protezione",
        "description": (
            "Usando un'Azione Complessa, tracci sul suolo o nell'aria un asilo repulsivo avente raggio di estensione pari al tuo valore di Tenacia. "
            "Tale area accoglie di sua sponte un numero limitato di individui pari alla metà della tua Tenacia. "
            "Qualsiasi estraneo non autorizzato che tenti di insinuarsi dovrà forzare la barriera, vincendo un TS su Resistenza sfidando una CD calcolata su 5 + il tuo valore di Tenacia."
        ),
    },
    {
        "name": "Sisu",
        "description": (
            "Quando ti risvegli dal Martirio, rigeneri un ammontare di PF pari alla tua Grinta x 4 (anziché x 2), con un recupero minimo garantito di 4 PF."
        ),
    },
    {
        "name": "Sopravvissuto",
        "description": "Per contrarre la perdita di 1 punto Fame devono trascorrere due sezioni temporali complete, anziché una sola.",
    },
    {
        "name": "Studente di Magia",
        "description": (
            "Lanciare incantesimi costa 2 PM in meno. "
            "Ottieni un bonus di +2 nelle prove per apprendere, trascrivere o identificare le magie."
        ),
    },
    {
        "name": "Tiro Rapido",
        "description": (
            "I tuoi polpastrelli danzano sulle armi da tiro: estrarre un'arma a distanza diviene un'Azione Gratuita, e l'azione di caricamento scende permanentemente di un grado (da Lenta a Normale, da Normale a Rapida, da Rapida a Gratuita). "
            "Ottieni inoltre un incremento di +1 ai TPC esclusivo per l'uso delle armi da fuoco."
        ),
    },
    {
        "name": "Toccato dalla Fede",
        "description": (
            "Previeni i danni inflitti da incantesimi e fonti magiche nemiche di un valore pari a 1/4 della tua Intensità (minimo 1). "
            "Ricevi un +1 a tutte le prove di Conoscenza sulle preghiere o religioni."
        ),
    },
    {
        "name": "Tossicologia",
        "description": (
            "Al prossimo effetto di Avvelenamento o Intossicazione inflitto, aumenta il dado di danno del veleno o della tossina utilizzato."
        ),
    },
    {
        "name": "Vigile",
        "description": (
            "Sei completamente immune alla condizione di Sorpreso. "
            "Il tuo perpetuo stato d'allerta ti fornisce, inoltre, un bonus di +3 a tutti i tiri che coinvolgono la sorveglianza."
        ),
    },
]
