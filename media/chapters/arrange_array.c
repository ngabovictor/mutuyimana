#include<stdio.h>
main()
{
	int swap, place, yes, less, great, j, i, arr[5];
	
	printf("Enter numbers: ");
	
	for(i=0; i<=4; i++)
	{
		scanf("%d", &arr[i]);
	}
	
	printf("\nBefore arrangment: ");
	
	for(i=0; i<=4; i++)
	{
		printf(" %d", arr[i]);
	}
	
	for(i=0; i<=4; i++)
	{
		less=arr[i];
		
		for(j=i+1; j<=4; j++)
		{
			if(arr[j] < arr[i])
			{
				if(arr[j] < less)
				{
					less = arr[j];
					place = j;
					yes = 1;
				}
			}
		}
		
		if(yes == 1)
		{
			swap = arr[i];
			arr[i] = less;
			arr[place] = swap;
		}
		
		yes = 0;
	}
	
	printf("\nIncreasing order: ");
	
	for(i=0; i<=4; i++)
	{
		printf(" %d", arr[i]);
	}
	
	
	for(i=0; i<=4; i++)
	{
		great=arr[i];
		
		for(j=i+1; j<=4; j++)
		{
			if(arr[j] > arr[i])
			{
				if(arr[j] > great)
				{
					great = arr[j];
					place = j;
					yes = 1;
				}
			}
		}
		
		if(yes == 1)
		{
			swap = arr[i];
			arr[i] = great;
			arr[place] = swap;
		}
		
		yes = 0;
	}
	
	printf("\nDecreasing order: ");
	
	for(i=0; i<=4; i++)
	{
		printf(" %d", arr[i]);
	}
	
	return 0;
}'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
/'''''''[''














88888888888877777776666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666655555555                 5          
