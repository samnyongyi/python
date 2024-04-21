from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

# 연산자의 우선순위 계산 함수
def precedence (op):
    if   (op=='(' or op==')') : return 0;
    elif (op=='+' or op=='-') : return 1;
    elif (op=='*' or op=='/') : return 2;
    else : return -1

# 중위 표기 수식의 후위식 변환
def Infix2Postfix( expr ):
    s = ArrayStack(100)
    output = []

    for term in expr :  # 중위식의 각 항들을 순서대로 term에 대입
        if term in '(' :    # 열린 괄호일 경우 스택에 삽입
            s.push('(')

        elif term in ')' :  # 열린 괄호가 나올 때까지 스택에서 연산자를 꺼내 출력
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' :
                    break;
                else :
                    output.append(op)

        elif term in "+-*/" :
            while not s.isEmpty() : # term이 연산자이면서 스택에서 같거나 높은 연산자를 모두 꺼내 출력
                op = s.peek()
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)    # term을 스택에 삽입

        else :                  # 피연산자
            output.append(term)

    while not s.isEmpty() : # 처리 종료시 스택에 남은 모든 요소들을 꺼내 순서대로 출력
        output.append(s.pop())
    return output# 후위 표기식 반환


