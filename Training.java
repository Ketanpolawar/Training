import java.util.Stack;
class Main {
    public static void main(String[] args) {
        int c;
        String str="()))(())()))((";
        Stack<String> st=new Stack<String>();
        c=check(str,st);
        System.out.println(c);
    }
    public static int check(String str,Stack<String> st){
        int count=0;
        for(int i=0;i<str.length();i++){
            if(str.charAt(i)=='('){
                st.add("(");
            }
            else if(!st.isEmpty() && str.charAt(i)==')'){
                st.pop();
                count=count+1;
            }
            
        }
        return count;
        
    }
}


//Linked List

// Online Java Compiler
// Use this editor to write, compile and run your Java code online

public class LinkedList{
    public static void main(String[] args){
        
        LinkedList obj = new LinkedList();
        obj.addLast(1);
        obj.addLast(2);
        obj.addLast(3);
        obj.addLast(4);
        obj.display();
    }
    

class Node{
    Node(int val){
        this.data=val;
    }
    int data;
    Node next;
}
Node head;


public void addLast(int value){
    Node temp = head;
    Node obj =new Node(value);
    if(temp==null){
        head = obj;
        return;
    }
    while(temp.next != null){
        temp=temp.next;
    }
    temp.next=obj;
}

public void display(){
    Node temp =head;
    while(temp!=null){
        System.out.print(temp.data+"=>");
        temp=temp.next;
    }
}
}
