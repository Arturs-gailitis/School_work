#!/bin/bash

REPO_PATH="C:\Users\Arturs\OneDrive\Desktop\Work\School_work\Datubāze_ar_neatkarīgo_testu"

if [ -d "$REPO_PATH" ]; then

    echo "Repozitorijs ir atrasts: $REPO_PATH"

    cd "$REPO_PATH" || { echo "Neizdevās atrast direktoriju."; exit 1; }

    echo "Atjaunina repozitoriju..."
    git pull || { echo "Git pull neizdevās."; exit 1; }

    echo "Izdevās git pull."
else
    echo "Direktorija neeksistē."
fi
