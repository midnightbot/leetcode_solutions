class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        int a =0;
        int b =0;
        int c=0;
        for (char ch: s){
            if (ch == '('){
                a+=1;
            }
            else if(ch == ')'){
                a-=1;
            }
            else if(ch == '{'){
                b+=1;
            }
            else if(ch == '}'){
                b-=1;
            }
            else if(ch == '['){
                c+=1;
            }
            else{
                c-=1;
            }
        }
        ////////////////////////////
        for(char ch: s){
            
            if (ch == '(' || ch =='{' || ch =='['){
                stack.push(ch);
            }
            else{
                
                if (stack.empty()){
                    return false;
                    
                }
                
                if (ch == ')'){
                    
                    char top = 'a';
                    while (!stack.empty() && top!='('){
                        top = stack.top();
                        stack.pop();
                    }
                    
                    if (top!='('){
                        return false;
                    }
                }
                
                else if(ch == '}'){
                    char top = 'a';
                    while (!stack.empty() && top!='{'){
                        top = stack.top();
                        stack.pop();
                    }
                    
                    if (top!='{'){
                        return false;
                    }
                }
                
                else{
                    
                    char top = 'a';
                    while (!stack.empty() && top!='['){
                        top = stack.top();
                        stack.pop();
                    }
                    
                    if (top!='['){
                        return false;
                    }
                    
                }
            }
        }
        /////////////////
        
        return (stack.empty() && a==0 && b==0 && c==0);
    }
};
