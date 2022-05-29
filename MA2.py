"""
Solutions to module 2 - A calculator
Student: Winston Olsson
Mail: winston.lidingo@hotmail.com
Reviewed by: Alicia Robertsson
Reviewed date: 19/04-2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""


import math
from re import M
from statistics import mean
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def fib(n):
    memory = {0:0, 1:1}
    def fib_mem(n):
        if n not in memory:
            memory[n] = fib_mem(n-1) + fib_mem(n-2)
        return memory[n]
    return fib_mem(n)

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

def power(lst):
        m=lst[0]
        n=lst[1]
        return m**n


def statement(wtok, variables):
    """ See syntax chart for statement"""
    if wtok.is_at_end()==False:
        result = assignment(wtok, variables)
        if wtok.is_at_end()==False:
            raise SyntaxError('Expected *EOL*') #Out of line
            
        return result
    else:
        pass
    


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables) #Result ska inte ändras och fortsätta räknas ut. Notering till själv, uppdatering av token sker generellt på allt. Result skickar bara vidare nuvarande position eventuellt commando på postion.
    while wtok.get_current() == '=': 
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()]=result #Plockar upp värdet av svaret Denna loop skickar inte ut något utan bara registrerar variabler. Värdet som registreras är fortfarande värdet på result.
            wtok.next() #Kör runt runt så att fler variabler kan läggas till, eller steging för att gå vidare i koden. Notera att om man tilsätter innanför paranteser.
        else:
            raise SyntaxError('Expected variable_name') #Ifall inget namn ges efter likamedtecken, 
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        else: #Else går bra här då loopen inte kör om inte det är - eller +. Både opperatorerna måste vara inom samma loop.
            result = result - term(wtok, variables)        
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':  
        wtok.next()
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
        else: #Samma som för expression gäller här.
            arg=factor(wtok, variables)
            if arg==0:
                raise EvaluationError('Division with 0') #Division med 0
            else:
                result = result / arg

    return result


def factor(wtok, variables): 
    """ See syntax chart for factor"""
    function_1={'sin':math.sin,'cos':math.cos,'exp':math.exp,'log':math.log,'fib':fib,'fac':fac, 'abs':abs}
    function_n={'min':min,'max':max,'mean':mean,'sum':sum,'pwr':power} #Definerar vad de är för något

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.get_current()== '-':
        wtok.next()
        result= -1*factor(wtok,variables)

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        elif wtok.get_current() in function_1:
            func=function_1[wtok.get_current()]
            func_name=wtok.get_current()
            wtok.next()
            if wtok.get_current() == '(':
                wtok.next()
                inside_func=assignment(wtok,variables) #Tog orimligt lång tid att fixa så att inte paranteserna åker med in. Bästa sättet jag kom på nu var att skicka in så att paranteserna sköts separat.
                if inside_func<=0 and func==math.log: #log fix
                    raise EvaluationError('Zero or negative number within log')
                elif (inside_func.is_integer()==False or inside_func<0) and (func==fac or func==fib):
                    raise EvaluationError(f'Expected positive interger in {func_name}, got {inside_func}')
                elif wtok.get_current() != ')': #Denna function är mer eller mindre bara en utökning på parantes definitionen
                    raise SyntaxError("Expected ')'")
                else:
                    result=func(inside_func)
                    wtok.next()
            else:
                raise SyntaxError('() is needed when calling a function')
        elif wtok.get_current() in function_n:
            func_n=function_n[wtok.get_current()]
            lst=[]
            wtok.next()
            if wtok.get_current() == '(':
                while wtok.get_current() != ')': #Denna var lättare, slut parantes kommer den skrika på som unbalanced paranthesis
                    wtok.next()
                    lst.append(assignment(wtok,variables))
                result=func_n(lst)
                wtok.next()
            else:
                raise SyntaxError('() is needed when calling a function')

        else:
            raise EvaluationError('Variable not found') #Detta löser om man försöker köra koden med en variabel som inte finns    
    
    else:
        raise SyntaxError(
            "Expected number,'-', variable, function or '('") #Name finns nu med 
    return result



         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}

    
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars': #Lägg till vars komandot
            print(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result,variables)
                if wtok.is_at_end()==False: #Här lägger vi till identification av slutet och beskriver vad som händer om vi inte kommer dit. Går att sätta denna i factor också. Förmodligen fixad nu i statement.
                    raise SyntaxError('Unnexpected token')                

            except SyntaxError as se:
                if wtok.is_at_end(): #När jag skulle lägga till definition av EOL utanför syntax blev det knasigt.
                    tok='*EOL*'
                else:
                    tok=wtok.get_current() #Skrivelse till error för förklaring var felet ligger                
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{tok}' just after '{wtok.get_previous()}'")
            except EvaluationError as ee:
                print("*** Evaluiation error: ", ee)                


            except TokenError as te:
                print('*** Token error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()

