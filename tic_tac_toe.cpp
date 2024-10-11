#include <bits/stdc++.h>
using namespace std;
int row=0;
int column=0;
char token='X';
char board[3][3]={
        {'1','2','3'},
        {'4','5','6'},
        {'7','8','9'}
    };
int hh=0;
void functionone(){
    cout<<"    |   |   \n";
    cout<<"  "<<board[0][0]<<" | "<<board[0][1]<<" | "<<board[0][2]<<"\n";
    cout<<"____|___|___\n";
    cout<<"    |   |   \n";
    cout<<"  "<<board[1][0]<<" | "<<board[1][1]<<" | "<<board[1][2]<<"\n";
    cout<<"____|___|___\n";
    cout<<"    |   |   \n";
    cout<<"  "<<board[2][0]<<" | "<<board[2][1]<<" | "<<board[2][2]<<"\n";
    cout<<"____|___|___\n";
}


void functiontwo(){
    char digit=' ';
    if(token=='X'){
        
        cout<<"Player 1 (X) turns ";
        cin>>digit;
    }else{
        cout<<"Player 2 (O) turns ";
        cin>>digit;
    }

    switch (digit) {
    case '1':
        row=0;
        column=0;
        break;
    case '2':
        row=0;
        column=1;
        break;
    case '3':
        row=0;
        column=2;
        break;
    case '4':
        row=1;
        column=0;
        break;
    case '5':
        row=1;
        column=1;
        break;
    case '6':
        row=1;
        column=2;
        break;
    case '7':
        row=2;
        column=0;
        break;
    case '8':
        row=2;
        column=1;
        break;
    case '9':
        row=2;
        column=2;
        break;
    
    default:
        cout << "invalid Input !!";
    }

    if(token=='X' && board[row][column] !='X' && board[row][column]!='O'){
        board[row][column]='X';
        token='O';
    }else if(token=='O' && board[row][column] !='X' && board[row][column]!='O'){
        board[row][column]='O';
        token='X';
    }else{
        cout<<"Occupied"<<endl;
        functiontwo();
    }
}

bool functionthree(){
    for(int i=0;i<3;i++){
        if(board[i][0]==board[i][1] && board[i][0]==board[i][2] || board[0][i]==board[1][i] && board[0][i]==board[2][i]){
            return true;
        }
    }

    if(((board[0][0]==board[1][1]) && (board[0][0]==board[2][2]) )|| (board[0][2]==board[1][1] && board[0][2]==board[2][0])){
        return true;
    }

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(board[i][j]!='X' && board[i][j]!='O'){
                return false;
            }
        }
    }
    hh=1;
    return true;
}


int main(){
    while(!functionthree()){
        functionone();
        functiontwo();
        functionthree();
    }
    if(token=='X' && hh==0){
        functionone();
        cout<<" player 2 (O) wins";
    }else if(token=='O' && hh==0){
        functionone();
        cout<<" player 1 (X) wins";
    }else{
        functionone();
        cout<<"Draw";
    }

}