
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


def calcola_risk_score(dati_personali, decisioni_persone, spiegabilita, supervisione_umana):
    risk_score = 0
    
    if dati_personali == 1:
        risk_score += 1
    
    if decisioni_persone == 1:
        risk_score += 1
    
    if spiegabilita == 0:
        risk_score += 1
    
    if supervisione_umana == 0:
        risk_score += 1
    
    return risk_score

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

    
risk_score = calcola_risk_score(dati_personali, decisioni_persone, spiegabilita, supervisione_umana)

if risk_score <= 1:
    overall_risk = "LOW"

elif 2 <= risk_score <= 3:
    overall_risk = "MEDIUM"

elif risk_score == 4:
    overall_risk = "HIGH"

#REPORT FINALE


print("======================================")

print("AI RISK ASSESSMENT")

print("======================================")

print(f"Sistema AI: {nome_sistema}")

print()

print(f"PRIVACY RISK: {privacy_risk}")

print(f"DECISION IMPACT: {decision_impact}")

print(f"EXPLAINABILITY RISK: {indice_spiegabilita}")

print(f"HUMAN OVERSIGHT RISK: {indice_supervisione}")

print(f"Overall risk: {overall_risk}")


print("======================================")