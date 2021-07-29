import re

class Interprete:
    stack_op =  []  #Stores the Stack operations.
    stack   =   []  #Stores the values through the program execution.
    labels =    {}  #store the labels and the stack_op position the are pointing
    rval =      {}  # rvalues
    lval =      {}  #lvalues
#### OPERACIONES SOBRE PILA (FINALIZADAS LAS VERIFICACIONES)####

#PUSH:
    def PUSH(self, item):
        self.stack.append(item)
#POP:
    def POP(self):
        self.stack.pop()
#ADD:
    def ADD(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1)+int(i2))
#SUB:
    def SUB(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1)-int(i2))
#MUL:
    def MUL(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1)*int(i2))
#DIV:
    def DIV(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1)/int(i2))
#AND:
    def AND(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(bool(i1) and bool(i2))
#OR:
    def OR(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(bool(i1) or bool(i2))
        
#LT:
    def LT(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1) < int(i2))
#LE:
    def LE(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1) <= int(i2))
#GT:
    def GT(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1) > int(i2))
#GE:
    def GE(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1) >= int(i2))
#EQ:
    def EQ(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1) == int(i2))
#NEQ:
    def NEQ(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.PUSH(int(i1) != int(i2))
#UMINUS:
    def UMINUS(self):
        i1 = self.stack.pop
        self.PUSH(-int(i1))
#NOT:
    def NOT(self):
        i1 = self.stack.pop
        self.PUSH(not bool(i1))
#RVALUE:
    def RVALUE(self, id):
        self.PUSH(self.rval[id])
#LVALUE:
    def LVALUE(self, id):
        self.PUSH(id(self.rval[id]))
#ASSIGN:
    def ASSIGN(self):
        i1 = self.stack.pop
        i2 = self.stack.pop
        self.rval[i1] = int(i2)
#GOTO:
    def GOTO(self, lb):
        return self.labels[lb]
#GOTRUE:
    def GOTRUE(self, lb):
        if (self.stack.pop):
            return self.labels[lb]
#GOFALSE:
    def GOFALSE(self, lb):
        if (not self.stack.pop):
            return self.labels[lb]
#READ:
    def READ(self,id):
        i = input();
        if (id == "true" or id=="false"):
            self.rval[id] = bool(id) 
        else:
            if(i.isdigit()):
                self.rval[id] = int(id) 
            else:
                print("INVALID INPUT")
                return False
#PRINT:
    def PRINT(self,id):
        print(self.rval[id])

#RESET:
    def RESET(self):
        while(len(self.stack)>0):
            self.stack.pop
        self.rval.clear
        self.lval.clear
        self.labels.clear

    def tiene_etiq(self, inst):
        z = re.match("[a-zA-Z]+$",inst)
        return z
        
    def run(self):
        PC = 0
        param_0 = ["EXIT","RESET","POP","MUL","DIV","ADD","SUB","AND","OR","LT","LE","GT","GE","EQ","NEQ","ASSIGN", "NOT", "UMINUS"]
        param_1 = ["PUSH","RVALUE","LVALUE","GOTO","GOTRUE","GOFALSE","READ","PRINT"]
        while (True):
            instruction = self.stack_op[PC]
            ins_parts = instruction.split(" ")
            #verificamos cuantos componentes tiene el operador
            if (len(ins_parts) == 1) and (ins_parts[0] in param_0):
                if(ins_parts[0]=="EXIT"):
                    break
                if(ins_parts[0]=="RESET"):
                    self.RESET()
                if(ins_parts[0]=="POP"):
                    self.POP
                if(ins_parts[0]=="MUL"):
                    self.MUL
                if(ins_parts[0]=="DIV"):
                    self.DIV
                if(ins_parts[0]=="ADD"):
                    self.ADD
                if(ins_parts[0]=="SUB"):
                    self.SUB
                if(ins_parts[0]=="AND"):
                    self.AND
                if(ins_parts[0]=="OR"):
                    self.OR
                if(ins_parts[0]=="LT"):
                    self.LT
                if(ins_parts[0]=="LE"):
                    self.LE
                if(ins_parts[0]=="GT"):
                    self.GT
                if(ins_parts[0]=="GE"):
                    self.GE
                if(ins_parts[0]=="EQ"):
                    self.EQ
                if(ins_parts[0]=="NEQ"):
                    self.NEQ
                if(ins_parts[0]=="ASSIGN"):
                    self.ASSIGN
                if(ins_parts[0]=="NOT"):
                    self.NOT
                if(ins_parts[0]=="UMINUS"):
                    self.UMINUS
            else:
                print("ERROR: OPERATOR NOT IDENTIFIED "+ins_parts[0])
        
            if (len(ins_parts) == 2):
                # CASO OPERADORES SIN PARAMETRO CON ETIQUETA
                if(self.tiene_etiq(ins_parts[0])):
                    self.labels[self.getLabel] = PC
                    if(ins_parts[1]=="EXIT"):
                        break
                    if(ins_parts[1]=="RESET"):
                        self.RESET()
                    if(ins_parts[1]=="POP"):
                        self.POP
                    if(ins_parts[1]=="MUL"):
                        self.MUL
                    if(ins_parts[1]=="DIV"):
                        self.DIV
                    if(ins_parts[1]=="ADD"):
                        self.ADD
                    if(ins_parts[1]=="SUB"):
                        self.SUB
                    if(ins_parts[1]=="AND"):
                        self.AND
                    if(ins_parts[1]=="OR"):
                        self.OR
                    if(ins_parts[1]=="LT"):
                        self.LT
                    if(ins_parts[1]=="LE"):
                        self.LE
                    if(ins_parts[1]=="GT"):
                        self.GT
                    if(ins_parts[1]=="GE"):
                        self.GE
                    if(ins_parts[1]=="EQ"):
                        self.EQ
                    if(ins_parts[1]=="NEQ"):
                        self.NEQ
                    if(ins_parts[1]=="ASSIGN"):
                        self.ASSIGN
                    if(ins_parts[1]=="NOT"):
                        self.NOT
                    if(ins_parts[1]=="UMINUS"):
                        self.UMINUS
                else:
                    if (ins_parts[1] == "true" or ins_parts[1]=="false") or (ins_parts[1].isdigit()) :                                    
                        if(ins_parts[0]=="PUSH"):
                            self.PUSH(ins_parts[1])
                        if(ins_parts[0]=="RVALUE"):
                            self.RVALUE(ins_parts[1])
                        if(ins_parts[0]=="LVALUE"):
                            self.LVALUE(ins_parts[1])
                        if(ins_parts[0]=="GOTO"):
                            self.GOTO(ins_parts[1])
                        if(ins_parts[0]=="GOTRUE"):
                            self.GOTRUE(ins_parts[1])
                        if(ins_parts[0]=="GOFALSE"):
                            self.GOFALSE(ins_parts[1])
                        if(ins_parts[0]=="READ"):
                            self.READ(ins_parts[1])
                        if(ins_parts[0]=="PRINT"):
                            self.PRINT(ins_parts[1])
                    else:
                        print("INVALID INPUT")
            if (len(ins_parts) == 3):
                if(self.tiene_etiq(ins_parts[0])):
                    self.labels[self.getLabel] = PC
                    if(ins_parts[0]=="PUSH"):
                        self.PUSH(ins_parts[1])
                    if(ins_parts[0]=="RVALUE"):
                        self.RVALUE(ins_parts[1])
                    if(ins_parts[0]=="LVALUE"):
                        self.LVALUE(ins_parts[1])
                    if(ins_parts[0]=="GOTO"):
                        self.GOTO(ins_parts[1])
                    if(ins_parts[0]=="GOTRUE"):
                        self.GOTRUE(ins_parts[1])
                    if(ins_parts[0]=="GOFALSE"):
                        self.GOFALSE(ins_parts[1])
                    if(ins_parts[0]=="READ"):
                        self.READ(ins_parts[1])
                    if(ins_parts[0]=="PRINT"):
                        self.PRINT(ins_parts[1])
            else:
                print("INVALID OPERATION: PARAMETER NUMBER EXCEDED")
            PC = PC +1 #Aumentamos el contador del programa.    