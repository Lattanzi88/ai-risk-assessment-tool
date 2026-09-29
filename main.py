
# Il programma chiede all'utente di inserire alcune informazioni sul suo sistema AI, quindi restituisce una valutazione del rischio su singoli parametri (PRIVACY RISK,DECISION IMPACT, EXPLAINABILITY RISK, HUMAN OVERSIGHT RISK), nonchè una valutazione complessiva sul sistema. 

# FUNZIONI

def valuta_privacy(dati_personali):
    if dati_personali == 1:
        return "HIGH RISK"
    elif dati_personali == 0:
        return "LOW RISK"
    else:
        return "INVALID"


def valuta_impatto_persone(decisioni_persone):
    if decisioni_persone == 1:
        return "HIGH RISK"
    elif decisioni_persone == 0:
        return "LOW RISK"
    else:
        return "INVALID"
        

def valuta_spiegabilita(spiegabilita):
    if spiegabilita == 1:
        return "LOW RISK"
    elif spiegabilita == 0:
        return "HIGH RISK"
    else:
        return "INVALID"


def human_in_the_loop(supervisione_umana):
    if supervisione_umana == 1:
        return "LOW RISK"
    elif supervisione_umana == 0:
        return "HIGH RISK"
    else:
        return "INVALID"

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


dati_personali = int(input("Utilizza dati personali? (1 = sì, 0 = no): "))

privacy_risk = valuta_privacy(dati_personali)

print("PRIVACY RISK:", privacy_risk)


decisioni_persone = int(input("Prende decisioni sulle persone? (1 = sì, 0 = no): "))

decision_impact = valuta_impatto_persone(decisioni_persone)

print("DECISION IMPACT:", decision_impact)


spiegabilita = int(input("Le decisioni sono spiegabili? (1 = sì, 0 = no): "))

indice_spiegabilita = valuta_spiegabilita(spiegabilita)

print("EXPLAINABILITY RISK:", indice_spiegabilita)


supervisione_umana = int(input("E' presente supervisione umana? (1 = sì, 0 = no): "))

indice_supervisione = human_in_the_loop(supervisione_umana)

print("HUMAN OVERSIGHT RISK: ", indice_supervisione)

    
risk_score = calcola_risk_score(dati_personali, decisioni_persone, spiegabilita, supervisione_umana)

if risk_score <= 1:
    print("Overall risk: LOW")

elif 2 <= risk_score <= 3:
    print("Overall risk: MEDIUM")

elif risk_score == 4:
    print("Overall risk: HIGH")


