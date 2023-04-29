with open('errors.txt', encoding='utf-8') as q:
    for i in q:
        code = ''
        mess = ''
        mode = 0
        for j in i:
            if mode == 0:
                code += j
            if mode == 0 and j == ' ':
                mode = 1
            if mode == 2:
                mess += j
            if j == '«' and mode == 1:
                mode = 2

            if mode == 2 and j == '»':
                mode = 3
        s = f'''
        
@app.errorhandler({code[:-1]})
def error{code[:-1]}():
    return render_template('error.html',
                           code={code[:-1]},
                           mess="{mess[:-1]}")'''
        print(s)