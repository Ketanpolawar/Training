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
