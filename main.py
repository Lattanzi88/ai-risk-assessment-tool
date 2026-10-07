# Il programma chiede all'utente di inserire alcune informazioni sul suo sistema AI,
# quindi restituisce una valutazione del rischio su singoli parametri
# (PRIVACY RISK, HUMAN IMPACT, HUMAN OVERSIGHT, EXPLAINABILITY),
# nonché una valutazione complessiva sul sistema.

import json

# FUNZIONI

def chiedi_si_no(domanda):
    while True:
        try:
            risposta = int(input(domanda))
        except:
            print("Input non valido. Inserisci 1 oppure 0.")
            continue

        if risposta == 1 or risposta == 0:
            break

    return risposta


def calcola_risk_score(fattori_rischio):
    risk_score = 0

    for chiave, valore in fattori_rischio.items():
        if valore["attivo"]:
            risk_score += valore["gravità"]

    return risk_score

def valuta_rischio_complessivo(risk_score):
    if risk_score >= 6:
        return "HIGH"
    elif 3 <= risk_score <= 5:
        return "MEDIUM"
    else:
        return "LOW"


def stampa_rischi(fattori_rischio):
    for chiave, valore in fattori_rischio.items():

        if valore["attivo"]:
            rischio = "HIGH RISK"
            descrizione = valore["descrizione_alto"]
        else:
            rischio = "LOW RISK"
            descrizione = valore["descrizione_basso"]

        print(chiave, ":", rischio, "-", valore["categoria"])
        print("Severity:", valore["gravità"])
        print(descrizione)
        print()
        
def crea_report(nome_sistema, fattori_rischio, risk_score, overall_risk):
    rischi = {}
    for chiave, valore in fattori_rischio.items():
        if valore["attivo"]:
            rischi[chiave] = "HIGH RISK"
            
        else:
            rischi[chiave] = "LOW RISK"
            
    report = {"sistema": nome_sistema,
              "risk score": risk_score,
              "overall risk": overall_risk,
              "rischi": rischi 
    }

    return(report)
    
# PROGRAMMA PRINCIPALE

nome_sistema = input("Inserisci il nome del sistema AI: ")

dati_sensibili = chiedi_si_no(
    "Il sistema utilizza dati sensibili? (1 = sì, 0 = no): "
)

impatto = chiedi_si_no(
    "Il sistema ha un impatto diretto sulle persone? (1 = sì, 0 = no): "
)

supervisione = chiedi_si_no(
    "Il sistema prevede una supervisione umana? (1 = sì, 0 = no): "
)

spiegabilita = chiedi_si_no(
    "Il sistema è spiegabile? (1 = sì, 0 = no): "
)


# STRUTTURA DEI FATTORI DI RISCHIO

fattori_rischio = {

    "Privacy": {
        "attivo": dati_sensibili == 1,
        "categoria": "Data Protection",
        "descrizione_alto": "Il sistema tratta dati personali o sensibili",
        "descrizione_basso": "Il sistema non tratta dati personali o sensibili",
        "gravità": 3
    },

    "Human Impact": {
        "attivo": impatto == 1,
        "categoria": "Human Impact",
        "descrizione_alto": "Il sistema prende decisioni che riguardano le persone",
        "descrizione_basso": "Il sistema non prende decisioni che riguardano direttamente le persone",
        "gravità": 2
    },

    "Human Oversight": {
        "attivo": supervisione == 0,
        "categoria": "Human Oversight",
        "descrizione_alto": "Non è presente una supervisione umana",
        "descrizione_basso": "È presente una supervisione umana",
        "gravità": 2
    },

    "Explainability": {
        "attivo": spiegabilita == 0,
        "categoria": "Transparency",
        "descrizione_alto": "Le decisioni del sistema non sono spiegabili",
        "descrizione_basso": "Le decisioni del sistema sono spiegabili",
        "gravità": 1
    }
}

# VALUTAZIONE DEL RISCHIO

risk_score = calcola_risk_score(fattori_rischio)

overall_risk = valuta_rischio_complessivo(risk_score)

report = crea_report(
    nome_sistema,
    fattori_rischio,
    risk_score,
    overall_risk
)

file = open("assessment_report.json", "w")

json.dump(report, file, indent=4)

file.close()

# REPORT FINALE

print("======================================")

print("AI RISK ASSESSMENT")

print("======================================")

print(f"Sistema AI: {nome_sistema}")

print()

stampa_rischi(fattori_rischio)

print(f"RISK SCORE: {risk_score}/8")

print(f"OVERALL RISK: {overall_risk}")

print("======================================")

