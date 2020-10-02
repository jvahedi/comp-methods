#resests current directories and files to default

rm -r */

FOLDERS='src doc tests examples'

mkdir ${FOLDERS}

for f in */; do echo "#$f" >> $f/README.md; done

tree ./
