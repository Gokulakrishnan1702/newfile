public void search(int data) 
{
    Node temp = head;
    int position = 1;
    while (temp != null) {
        if (temp.data == data) {
            System.out.println("Element found at position: " + position);
            return;
        }
        temp = temp.next;
        position++;
    }
    System.out.println("Element not found.");
}
        while(current.next.next!=null)
        {
            current=current.next;
        }
        current.next=null;
    }
    node head;
}




public void count() 
{
    int count = 0;
    Node temp = head;
    while (temp != null) {
        count++;
        temp = temp.next;
    }
    System.out.println("Total nodes: " + count);
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
            
                temp=temp.next;
            }
            if(temp.next==null||temp==null)
            {
                System.out.println("Position out of bounds");
                return;
            }
            temp.next=temp.next.next;
            temp.next.prev=temp;
            
        }