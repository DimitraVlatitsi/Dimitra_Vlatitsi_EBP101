#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
int  i, len, maxlen;
char seq[ 5000 ];
maxlen = 0;

for ( i=0 ; i<10 ; i++ )
	{
		scanf("%s", seq);
		len = strlen( seq );
		if ( len > maxlen )
			{
				maxlen = len;
			}
	}
printf("The maximun length is %d\n", maxlen );
}
