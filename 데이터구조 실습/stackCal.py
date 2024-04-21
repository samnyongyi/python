 from ArrayStack import ArrayStack
 def evalPostfix( expr ):		# expr은 리스트
    s = ArrayStack(100)
    for token in expr :
        if token in "+-*/" :
            val2 = s.pop()
            val1 = s.pop()
            if   (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :
            s.push( float(token) )	# 실수로 변환하여 스택에 저장필수
    return s.pop()
