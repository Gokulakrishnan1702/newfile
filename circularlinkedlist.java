class circularlinkedlist {
    Node head;
    Node tail;

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public void add(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
            newNode.next = head; // Point to itself to make it 
        
            tail.next = newNode;
            tail = newNode;
            tail.next = head; // Maintain the circular nature
        }
    }
    public void display() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        Node current = head;
        do {
            System.out.print(current.data + " -> ");
            current = current.next;
        } while (current != head);
        System.out.println("(back to head: " + head.data + ")");
    }

    public static void main(String[] args) {
        circularlinkedlist cll = new circularlinkedlist();
        cll.add(1);
        cll.add(2);
        cll.add(3);
        cll.add(4);
        cll.display(); // Output: 1 -> 2 -> 3 -> 4 -> (back to head: 1)
    }
}