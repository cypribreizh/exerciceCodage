BEGIN {
	printf("Nom\t\tNuméro\n---------------\n");
	total = 0;
}
NR>=1 {
	if ($2>24) {
		printf ("%-10s %6d\n", $1, $2);
		total += $2;
		}
	}
END {
	printf("\t\t-------\n\t\t%6d\n", total)
}
