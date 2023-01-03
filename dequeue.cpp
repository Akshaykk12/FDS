#include<iostream>
#define max 20
using namespace std;
class dqueue
{
	int data[max];
	int front,rear;
	public:
	dqueue()
	{
		front=-1;
		rear=-1;
	}
	void insert_at_front(int x)
	{
		if(front==-1)
		{
			front++;
			rear++;
			data[front]=x;
		}
		else
		{
			for(int i=rear+1;i>=0;i--)
			{
				data[i]=data[i-1];
			}
			data[0]=x;
			rear++;
		}
	}
	void insert_at_end(int x)
	{
		if(rear==-1)
		{
			front++;
			rear++;
			data[rear]=x;
		}
		else
		{
			rear++;
			data[rear]=x;
		}
	}
	void display()
	{
        
		for(int i=front;i<=rear;i++)
		{
            
			cout<<data[i]<<" ";
		}
	}
	void del_front()
	{
		if(front==-1)
		{
			cout<<"\ndeletion not happen";
		}
		else
		{
			cout<<"\ndeleted element is: "<<data[front];
			front++;
		}
	}
	void del_rear()
	{
		if(rear==-1)
		{
			cout<<"\ndeletion not happen";
		}
		else
		{
			cout<<"\ndeleted element is: "<<data[rear];
			rear--;
		}
	}
		
};
int main()
{
	dqueue obj;
	int ch,x;
	while(ch!=6)
	{
		cout<<"\n\n1.Insert at front\n2.Insert at end\n3.delete at front\n4.delete at end\n5.Display\n6.Exit\nEnter your choice: ";
		cin>>ch;
		switch (ch)
		{
		case 1:
			cout<<"Enter element: ";
			cin>>x;
			obj.insert_at_front(x);
			break;
		case 2:
			cout<<"Enter element: ";
			cin>>x;
			obj.insert_at_end(x);
			break;
		case 3:
			obj.del_front();
			break;
		case 4:
			obj.del_rear();
			break;
		case 5:
			obj.display();
			break;
		case 6:
			exit(0);
		}
	}
}