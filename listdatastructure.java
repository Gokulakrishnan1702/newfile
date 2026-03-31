class node 
{
    int data;
    node next;
node(int data)
{
    this.data=data;
    this.next= null;
}}
class singlelinkedlist
{
   void insertatend(int data)
   { 
    node newnode=new node(data);
    if(head==null)
    {
        head=newnode;
        return;
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
            System.out.print(current.data+"-->");
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
        node current=head;
        while(current.next.next!=null)
        {
            current=current.next;
        }
        current.next=null;
    } 