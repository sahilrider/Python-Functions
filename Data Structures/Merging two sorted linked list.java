   import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    static class SinglyLinkedList {
        public SinglyLinkedListNode head;
        public SinglyLinkedListNode tail;

        public SinglyLinkedList() {
            this.head = null;
            this.tail = null;
        }

        public void insertNode(int nodeData) {
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

            if (this.head == null) {
                this.head = node;
            } else {
                this.tail.next = node;
            }

            this.tail = node;
        }
    }

    public static void printSinglyLinkedList(SinglyLinkedListNode node, String sep, BufferedWriter bufferedWriter) throws IOException {
        while (node != null) {
            bufferedWriter.write(String.valueOf(node.data));

            node = node.next;

            if (node != null) {
                bufferedWriter.write(sep);
            }
        }
    }

   static SinglyLinkedListNode mergeLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
       SinglyLinkedListNode List=null;
       SinglyLinkedListNode temp=null;
       SinglyLinkedListNode a=head1;
       SinglyLinkedListNode b=head2;
       if(head1.data>=head2.data)
       {
           List=head2;
           temp=head2;
           b=b.next;
       }
       else
       {
           List=head1;
           temp=head1;
           a=a.next;
       }
       while(a!=null && b!=null)
       {
           if(a.data<=b.data)
           {
            temp.next=a;
            temp=a;
            a=a.next;
           }
           else
           {
              temp.next=b;
              temp=b;
              b=b.next;   
           }
       }
       if(a!=null)
       {
           temp.next=a;
       }
      if(b!=null)
       {
           temp.next=b;
       }
       return List;
    }
