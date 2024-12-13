#!/bin/bash

# Definē ceļu uz repozitoriju
REPO_PATH="C:\Users\Arturs\OneDrive\Desktop\Work\School_work\Datubāze_ar_neatkarīgo_testu"

# Pārbauda, vai direktorija eksistē
if [ -d "$REPO_PATH" ]; then

    echo "Repozitorijs ir atrasts: $REPO_PATH"

    # Pāriet uz repozitorija direktoriju, ja tas neizdodas, iznāk no skripta ar kļūdas kodu 1
    cd "$REPO_PATH" || { echo "Neizdevās atrast direktoriju."; exit 1; }

    echo "Atjaunina repozitoriju..."

    # Izpilda 'git pull', lai iegūtu jaunākās izmaiņas no attālinātā repozitorija
    git pull || { echo "Git pull neizdevās."; exit 1; }

    echo "Izdevās git pull."
else
    echo "Direktorija neeksistē."
fi
