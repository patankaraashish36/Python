#include<iostream.h>
#include<conio.h>
Void  main()
{
clrscr ();
int state=0, x=0, i, l;
char input [50];
cin>>input;
cout <<input;
while (input[x]! = '/0')
{
i=input[x];
switch(state)
{
case0 : if (i=='a')
{
}
else if(i='b')
{
state=1;
}
else
{
cout<<'error in input 0';
}
break;
case 1: if (i=='a')
{
state=0
}
else if(i=='b')
{
state=2;
}
else 
{
cout<<'error in input';
}
break;
case 2: if(i=='a')
{
state=0;
}
else if(i=='b')
{
state=3;
}
else 
{
cout<<'error in input';
}
break;
case 3: if (if=='a'||i=='b')
{
state=3;
}
else
{
cout<<”error in input 3”;
break;
}
x=x+1;
}
if(state==3)
 
cout<<”string accepted”;
}
else
{
cout<<”string not accepted”;
}
return 0;
}
}
