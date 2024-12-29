#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
int  len, i;
float counter, percent;
char seq[ 5000 ];
counter = 0;

scanf("%s", seq);
len = strlen( seq );
for ( i=0; i<len; i++ )
	{
		if ( seq[i] == 'G' || seq[i] == 'C' )
			{
				counter = counter + 1;
			}
	}
percent = (counter/len)*100;
printf("The GC percentage of the sequence is %f\n", percent );
}
