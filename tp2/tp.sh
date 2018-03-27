cd ~/Bureau/1795926_1792901_tp2

if [ $2 == "vorace" ]; then
	python vorace/vorace.py -e $4 $5 $6
elif [ $2 == "progdyn" ]; then
	python dynamique/ProgDynamique.py -e $4 $5 $6
elif [ $2 == "tabou" ]; then
	python tabou/tabou.py -e $4 $5 $6
fi
