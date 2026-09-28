#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Prima parte: l'utente deve inserire alcune informazioni sul suo sistema AI

nome_sistema = input("Inserisci il nome del sistema AI: ")

dati_personali = int(input("Utilizza dati personali? (1 = sì, 0 = no): "))
if dati_personali == 1:
    print("Hai risposto sì")
elif dati_personali == 0:
    print("Hai risposto no")
else:
    print("Risposta non valida")

decisioni_persone = int(input("Prende decisioni sulle persone? (1 = sì, 0 = no): "))
if decisioni_persone == 1:
    print("Hai risposto sì")
elif decisioni_persone == 0:
    print("Hai risposto no")
else:
    print("Risposta non valida")

spiegabilità = int(input("Le decisioni sono spiegabili? (1 = sì, 0 = no): "))
if spiegabilità == 1:
    print("Hai risposto sì")
elif spiegabilità == 0:
    print("Hai risposto no")
else:
    print("Risposta non valida")

supervisione_umana = int(input("E' presente supervisione umana? (1 = sì, 0 = no): "))
if supervisione_umana == 1:
    print("Hai risposto sì")
elif supervisione_umana == 0:
    print("Hai risposto no")
else:
    print("Risposta non valida")

# Seconda parte: il programma in base alle risposte fornite dal cliente, restituisce informazioni sul rischio del sistema AI

if dati_personali == 1:
    print("PRIVACY RISK : HIGH")
else:
    print("PRIVACY RISK: LOW")

if decisioni_persone == 1:
    print("DECISION IMPACT: HIGH")
else:
    print("DECISION IMPACT: LOW")

if spiegabilità == 0:
    print("EXPLAINABILITY RISK: HIGH")
else:
    print("EXPLAINABILITY RISK: LOW")

if supervisione_umana == 0:
    print("HUMAN OVERSIGHT RISK: HIGH")
else:
    print("HUMAN OVERSIGHT RISK: LOW")

# Terza parte: Il programma fornisce un indicatore di rischio complessivo del sistema

risk_score = 0
if dati_personali == 1:
    risk_score += 1
if decisioni_persone ==1:
    risk_score += 1
if spiegabilità == 0:
    risk_score += 1
if supervisione_umana == 0:
    risk_score += 1

if risk_score <= 1:
    print("Overall risk: LOW")
elif 2 <= risk_score <= 3:
    print("Overall risk: MEDIUM")
elif risk_score == 4:
    print("Overall risk: HIGH")


