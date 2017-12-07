#include<iostream>
using namespace std;

void makeBox(int maxSize){
	
	int row, col, row_init=0, col_init, nbr=1, k, l;
	col=maxSize-1;
	row=maxSize-1;
	col_init=(maxSize/2);
	int box[maxSize][maxSize];
	
	for(int i=0; i<=maxSize; i++){
		for(int j=0; j<=maxSize; j++){
			box[i][j]=0;
		}
	}
	
	
	box[row_init][col_init]=nbr;
	nbr+=1;
	
	for(int i=1; i<=(maxSize*maxSize); i++){

		
		if(row_init-1<0 and col_init+1<=col){
			row_init=row;
			col_init=col_init+1;
			box[row_init][col_init]=nbr;
			nbr+=1;
		}
		
		else if(row_init-1<0 and col_init+1>col){
			row_init+=1;
			box[row_init][col_init]=nbr;
			nbr+=1;
		}
		
		else if(row_init-1>=0 and col_init+1>col){
			row_init=row_init-1;
			col_init=0;
			box[row_init][col_init]=nbr;
			nbr+=1;
		}
		
		else if((row_init-1<=row and row_init-1>=0) and (col_init+1<=col and col_init+1>=0)){
			
			
			k=row_init-1;
			l=col_init+1;
			
			
			if(box[k][l] != 0){
				row_init+=1;
				box[row_init][col_init]=nbr;
				nbr+=1;
			}
			
			
			else{
				
				box[k][l]=nbr;
				nbr+=1;
				row_init=k;
				col_init=l;	
			}
			
		
		}
		
	}
	
	cout<<endl;
	cout<<"Here is the Magic Box of "<<maxSize<<endl<<endl;
	
	for(int i=0; i<maxSize; i++){
		for(int j=0; j<maxSize; j++){
			cout<<box[i][j]<<" ";
		}
		cout<<endl;
	}
}

int getInput(int maxSize){
	if(maxSize%2 == 0 and maxSize >= 0){
		cout<<"Invalid input! Did you mean "<<(maxSize-1)<<" or "<<(maxSize+1)<<"? ";
		cin>>maxSize;
		return maxSize;
	}
	
	else if(maxSize <= 0 and maxSize%2 != 0){
		cout<<"Invalid input! Did you mean "<<(0-maxSize)<<"?";
		cin>>maxSize;
		return maxSize;
	}
	
	else{
		cout<<"Invalid input! Did you mean "<<0-(maxSize+1)<<" or "<<0-(maxSize-1)<<"? ";
		cin>>maxSize;
		return maxSize;
	}
}

void checkInput(int maxSize){
	start:
	if(maxSize%2 == 0 or maxSize<0 ){
		maxSize = getInput(maxSize);
		goto start;
	}
	
	else{
		makeBox(maxSize);
	}
}

int main(){
	int maxSize;
	cout<<"Let's make a Magic Box! Just enter number of items on a line (only odd numbers are accepted): ";
	cin>>maxSize;
	checkInput(maxSize);
	return 0;
}
