@app.route('/sub')
def subtraction():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    testfraction = validate(str(value1))
    testfraction1 = validate(str(value2))
    if(testfraction==True):    
    	temp1 = str(value1).split('/')
    	result1 = float(temp1[0])/int(temp1[1])
    else:
    	result1 =  value1
    if(testfraction1==True):    
    	temp2 = str(value2).split('/')
    	result2 = float(temp2[0])/int(temp2[1])
    else:
    	result2 =value2
    result = result1-result2
    return str(result)
