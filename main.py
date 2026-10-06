
# Il programma chiede all'utente di inserire alcune informazioni sul suo sistema AI, quindi restituisce una valutazione del rischio su singoli parametri (PRIVACY RISK,DECISION IMPACT, EXPLAINABILITY RISK, HUMAN OVERSIGHT RISK), nonchè una valutazione complessiva sul sistema. 

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

def valuta_rischio(risposta, rischio_alto):
    if risposta == rischio_alto:
        return "HIGH RISK"
    else:
        return "LOW RISK"


def calcola_risk_score(fattori_rischio):
    risk_score = 0
    
    for fattore in fattori_rischio.values():
        if fattore:
            risk_score += 1
    
    return risk_score
    
def valuta_rischio_complessivo(risk_score):
    if risk_score <= 1:
        return "LOW"
    elif risk_score <= 3:
        return "MEDIUM"
    else:
        return "HIGH"

        
# PROGRAMMA PRINCIPALE 

nome_sistema = input("Inserisci il nome del sistema AI: ")

dati_personali = chiedi_si_no("Utilizza dati personali? (1 = sì, 0 = no): ")

privacy_risk = valuta_rischio(dati_personali, 1)

decisioni_persone = chiedi_si_no("Prende decisioni sulle persone? (1 = sì, 0 = no): ")

decision_impact = valuta_rischio(decisioni_persone, 1)

spiegabilita = chiedi_si_no("Le decisioni sono spiegabili? (1 = sì, 0 = no): ")

indice_spiegabilita = valuta_rischio(spiegabilita, 0)


supervisione_umana = chiedi_si_no("E' presente supervisione umana? (1 = sì, 0 = no): ")

indice_supervisione = valuta_rischio(supervisione_umana, 0)


rischi = {
    "PRIVACY RISK": privacy_risk,
    "DECISION IMPACT": decision_impact,
    "EXPLAINABILITY RISK": indice_spiegabilita,
    "HUMAN OVERSIGHT RISK": indice_supervisione
}

fattori_rischio = {
    "Personal data": dati_personali == 1,
    "Decision impact": decisioni_persone == 1,
    "Explainability": spiegabilita == 0,
    "Human oversight": supervisione_umana == 0
}
    
risk_score = calcola_risk_score(fattori_rischio)

overall_risk = valuta_rischio_complessivo(risk_score)

#REPORT FINALE


print("======================================")

print("AI RISK ASSESSMENT")

print("======================================")

print(f"Sistema AI: {nome_sistema}")

print()

for nome_rischio, valutazione in rischi.items():
    print(f"{nome_rischio}: {valutazione}")

print("\n")

print(f"RISK SCORE: {risk_score}/4")
print(f"OVERALL RISK: {overall_risk}")


print("======================================")