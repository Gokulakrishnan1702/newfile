class node 
{
    int data;
    node next;
    node prev;
node(int data)
{
    this.data=data;
    this.next= null;
    this.prev=null;
}} 
class doublelinkedlist
{
   void create(int data)
   { 
    node newnode=new node(data);
    if(head==null)
    {
        head=temp=newnode;
        return;
    }
    temp.next=newnode;
    newnode.prev=temp;
    temp=newnode;
   }
    void insertatend(int data)
    { 
     node newnode=new node(data);
     if(head==null)
     {
          head=newnode;
          return;
     }
    node temp=head;
     while(temp.next!=null)
     {
          temp=temp.next;
     }
     temp.next=newnode;
     newnode.prev=temp;

} 
    void insertatfront(int data)
    { 
     node newnode=new node(data);
     if(head==null)
     {
          head=newnode;
          return;
     }
     newnode.next=head;
     head.prev=newnode;
     head=newnode;
    }



 void display()
    {
        node current=head;
        if(head==null)
        {
            System.out.println("list is empty");
            return;
        }
        while(current!=null)
        {
            System.out.print(current.data+"<=>");
            current=current.next;
        }
        System.out.println("null");
    }        
    void deleteatfront()
    {
        if(head==null)
        {
            System.out.println("list is empty");
            return;
        }
        head=head.next;
        head.prev=null;
    }

    void deleteatend()
    {
        if(head==null)
        {
            System.out.println("list is empty");
            return;
        }
        if(head.next==null)
        {
            head=null;
            return;
        }
        node temp=head;
        viod insertatposition(int data,int position)
        {
            node newnode=new node(data);
            if(head==null)
            {
                head=newnode;
                return;
            }
            if(position==0)
            {
                insertatfront(data);
                return;
            }
            node temp=head;
            for(int i=0;i<position-1;i++)
            {
                if(temp).next==null)
                {
                    System.out.println("Position out of bounds");
                    return;
                }
                temp=temp.next;
            }
            newnode.next=temp.next;
            if(temp.next!=null)
            {
                temp.next.prev=newnode;
            }
            temp.next=newnode;
            newnode.prev=temp;
        }
        void deleteatposition(int position)
        {
            if(head==null)
            {
                System.out.println("list is empty");
                return;
            }
            if(position==0)
            {
                deleteatfront();
                return;
            }
            node temp=head;
            for(int i=0;i<position-1;i++)
            {
                if(temp.next==null)
                {
                    System.out.println("Position out of bounds");
                    return;
                }
                temp=temp.next;
            }
            if(temp.next==null)
            {
                System.out.println("Position out of bounds");
                return;
            }
            temp.next=temp.next.next;
            if(temp.next!=null)
            {
                temp.next.prev=temp;
            }
        }