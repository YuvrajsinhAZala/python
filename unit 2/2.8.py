#8. Write a program to illustrate variable scope 
#using local global and nonlocal variables. 

program ='MCA'

print(program)

def fuction1():
    global program
    program = 'MSC'
    print(program)
    gr='0000'
    

    def function2():
        nonlocal gr
        gr = '4012'
        print(gr)
        print(program)

        
    function2()
fuction1()

'''
def function3():
    global department
    department = 'FOCA'
function3()

def function4():
    print(department)
function4()
'''

