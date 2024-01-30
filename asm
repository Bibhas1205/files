if test $# -ne 1
then
	echo "Use : $0 <filename>"
else 
	if echo $1|grep -q '\.'
	then
		file=$(echo $1|cut -d '.' -f 1)
		nasm -f elf $1
	else
		file=$1
		sudo mv $1 $1".asm"
		nasm -f elf $1".asm"
	fi
	
	ld -m elf_i386 -s -o $file $file".o"
	sudo rm $file".o"
	sudo chmod +x $file
	./$file
	rm $file
fi
