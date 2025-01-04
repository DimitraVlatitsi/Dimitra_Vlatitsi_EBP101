#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
int  i, len, maxlen;
char seq[ 5000 ];
maxlen = 0;

while ( scanf("%s", seq) == 1 )
	{
		len = strlen( seq );
		if ( len > maxlen )
			{
				maxlen = len;
			}
	}
printf("The maximun length is %d\n", maxlen );
}
