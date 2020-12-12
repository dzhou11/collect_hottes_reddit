((i=$RANDOM%1665+1))
cut -d "," -f 2-99 <<<cat ~/.data/quotes.csv | head -$i | tail -1
printf "        ~"
a=$(cut -d "," -f 1 <<<at ~/.data/quotes.csv | head -$i | tail -1)
if [[ -z "${a// }" ]]
then
        echo
else
        cut -d "," -f 1 <<<cat ~/.data/quotes.csv | head -$i | tail -1
fi

