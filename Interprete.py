import re

class Interprete:
    stack_op =  []  #Stores the Stack operations.
    stack   =   []  #Stores the values through the program execution.
    labels =    {}  #store the labels and the stack_op position the are pointing
    rval =      {}  # rvalues
    lval =      {}  #lvalues
#### OPERACIONES SOBRE PILA (FINALIZADAS LAS VERIFICACIONES)####

#getLabels Lee las etiquetas y guarda su posicion antes de que se ejecute el programa
    def getLabels(self):
        PC = 0
        for i in self.stack_op:
            instruction = self.stack_op[PC]
            ins_parts = instruction.split(" ")
            if (len(ins_parts) > 1) and (self.tiene_etiq(ins_parts[0])):
                ins_parts[0] = self.sin_salto(ins_parts[0])
                self.labels[ins_parts[0]] = PC
            PC = PC + 1
#PUSH:
    def PUSH(self, item):
        if (item == "true" or item =="false"):
            self.stack.append(bool(item))
        else:
            if(item.isdigit()):
               self.stack.append(int(item)) 
            else:
                print("INVALID INPUT")
                return False
#POP:
    def POP(self):
        self.stack.pop()
#ADD:
    def ADD(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(i1+i2)
#SUB:
    def SUB(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1)-int(i2))
#MUL:
    def MUL(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1)*int(i2))
#DIV:
    def DIV(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1)/int(i2))
#AND:
    def AND(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(bool(i1) and bool(i2))
#OR:
    def OR(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(bool(i1) or bool(i2))
        
#LT:
    def LT(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1) < int(i2))
#LE:
    def LE(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        print(self.stack)
        self.stack.append(int(i1)<=int(i2))
#GT:
    def GT(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1) > int(i2))
#GE:
    def GE(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1) >= int(i2))
#EQ:
    def EQ(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1) == int(i2))
#NEQ:
    def NEQ(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.stack.append(int(i1) != int(i2))
#UMINUS:
    def UMINUS(self):
        i1 = self.stack.pop()
        self.stack.append(-int(i1))
#NOT:
    def NOT(self):
        i1 = self.stack.pop()
        self.stack.append(not bool(i1))
#RVALUE:
    def RVALUE(self, id):
        self.stack.append(self.rval[id])
#LVALUE:
    def LVALUE(self, id):
        self.lval[id] = id
        self.stack.append(self.lval[id])
#ASSIGN:
    def ASSIGN(self):
        i1 = self.stack.pop()
        i2 = self.stack.pop()
        self.rval[i1] = int(i2)
#GOTO:
    def GOTO(self, lb):
        return self.labels[lb]
#GOTRUE:
    def GOTRUE(self, lb):
        if (self.stack.pop()):
            return self.labels[lb]
#GOFALSE:
    def GOFALSE(self, lb):
        print(lb)
        print(self.stack)
        p = self.stack.pop()
        print(p)
        if (not p):
            print("PASO")
            return self.labels[lb]
#READ:
    def READ(self,id):
        i = input();
        if (id == "true" or id=="false"):
            self.rval[id] = bool(i)
            self.lval[id] = id 
        else:
            if(i.isdigit()):
                self.rval[id] = int(i) 
                self.lval[id] = len(self.lval) + 1 
            else:
                print("INVALID INPUT")
                return False
#PRINT:
    def PRINT(self,id):
        print(self.rval[id])

#RESET:
    def RESET(self):
        while(len(self.stack)>0):
            self.stack.pop()
        self.rval.clear
        self.lval.clear
        self.labels.clear

    def tiene_etiq(self, inst):
        z = re.match("[a-zA-Z]+:$",inst)
        return z



    def sin_salto(self, i):
        j = i[0:len(i)-1]
        return j

    def run(self):
        self.getLabels()
        PC = 0
        param_0 = ["EXIT","RESET","POP","MUL","DIV","ADD","SUB","AND","OR","LT","LE","GT","GE","EQ","NEQ","ASSIGN", "NOT", "UMINUS"]
        param_1 = ["PUSH","RVALUE","LVALUE","GOTO","GOTRUE","GOFALSE","READ","PRINT"]
        while (PC < len(self.stack_op)):
            instruction = self.stack_op[PC]
            ins_parts = instruction.split(" ")
            if(ins_parts[0]=="EXIT" or ins_parts[0]=="EXIT\n"):
                    break
            #verificamos cuantos componentes tiene el operador
            ins_parts[len(ins_parts)-1] = self.sin_salto(ins_parts[len(ins_parts)-1])
            #print(self.stack_op[PC])
            #print(self.rval)
            #print(self.labels)
            #print(self.lval)
            #print(self.stack)
            #CASO CON 1 SOLA ENTRADA
            if (len(ins_parts) == 1) and (ins_parts[0] in param_0):
                if(ins_parts[0]=="RESET"):
                    self.RESET()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="POP"):
                    self.POP()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="MUL"):
                    self.MUL()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="DIV"):
                    self.DIV()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="ADD"):
                    self.ADD()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="SUB"):
                    self.SUB()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="AND"):
                    self.AND()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="OR"):
                    self.OR()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="LT"):
                    self.LT()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="LE"):

                    self.LE()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="GT"):
                    self.GT()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="GE"):
                    self.GE()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="EQ"):
                    self.EQ()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="NEQ"):
                    self.NEQ()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="ASSIGN"):
                    self.ASSIGN()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="NOT"):
                    self.NOT()
                    PC = PC +1 #Aumentamos el contador del programa.  
                if(ins_parts[0]=="UMINUS"):
                    self.UMINUS()
                    PC = PC +1 #Aumentamos el contador del programa.  
            else:
                # CASO 2 ENTRADAS
                if (len(ins_parts) == 2 ):
                    # A CONTINUACION POSIBLES CASOS
                    # CASO OPERADORES SIN PARAMETRO CON ETIQUETA
                    if(self.tiene_etiq(ins_parts[0])):
                        self.labels[ins_parts[0]] = PC
                        if(ins_parts[1]=="EXIT"):
                            break
                        if(ins_parts[1]=="RESET"):
                            self.RESET()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="POP"):
                            self.POP()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="MUL"):
                            self.MUL()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="DIV"):
                            self.DIV()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="ADD"):
                            self.ADD()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="SUB"):
                            self.SUB()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="AND"):
                            self.AND()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="OR"):
                            self.OR()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="LT"):
                            self.LT()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="LE"):
                            self.LE()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="GT"):
                            self.GT()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="GE"):
                            self.GE()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="EQ"):
                            self.EQ()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="NEQ"):
                            self.NEQ()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="ASSIGN"):
                            self.ASSIGN()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="NOT"):
                            self.NOT()
                            PC = PC +1 #Aumentamos el contador del programa.  
                        if(ins_parts[1]=="UMINUS"):
                            self.UMINUS()
                            PC = PC +1 #Aumentamos el contador del programa.  
                    # CASO 2 ENTRADAS 1 PARAMETRO SIN ETIQUETAS
                    else:
                        if (len(ins_parts) == 2) and (ins_parts[0] in param_1):                                    
                            if(ins_parts[0]=="PUSH"):
                                self.PUSH(ins_parts[1])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[0]=="RVALUE"):
                                self.RVALUE(ins_parts[1])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[0]=="LVALUE"):
                                self.LVALUE(ins_parts[1])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[0]=="GOTO"):
                                r = self.GOTO(ins_parts[1])
                                if isinstance(r, int):
                                    PC = r
                                else:
                                    PC = PC + 1
                            if(ins_parts[0]=="GOTRUE"):
                                r = self.GOTRUE(ins_parts[1])
                                if isinstance(r, int):
                                    PC = r
                                else:
                                    PC = PC + 1
                            if(ins_parts[0]=="GOFALSE"):
                                r = self.GOFALSE(ins_parts[1])
                                if isinstance(r, int):
                                    PC = r
                                else:
                                    PC = PC + 1
                                    
                            if(ins_parts[0]=="READ"):
                                self.READ(ins_parts[1])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[0]=="PRINT"):
                                self.PRINT(ins_parts[1])
                                PC = PC +1 #Aumentamos el contador del programa.  
                        else:
                            print("INVALID INPUT")
                else:
                    if (len(ins_parts) == 3):
                        # CASO 3 ENTRADAS: INSTRUCCION DE 1 PARAMETRO Y ETIQUETA
                        if(self.tiene_etiq(ins_parts[0])):
                            self.labels[ins_parts[0]] = PC
                            if(ins_parts[1]=="PUSH"):
                                self.PUSH(ins_parts[2])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[1]=="RVALUE"):
                                self.RVALUE(ins_parts[2])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[1]=="LVALUE"):
                                self.LVALUE(ins_parts[2])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[1]=="GOTO"):
                                r = self.GOTO(ins_parts[2])
                                if isinstance(r, int):
                                    PC = r
                                else:
                                    PC = PC + 1
                            if(ins_parts[1]=="GOTRUE"):
                                r = self.GOTRUE(ins_parts[2])
                                if isinstance(r, int):
                                    PC = r
                                else:
                                    PC = PC + 1
                            if(ins_parts[1]=="GOFALSE"):
                                r = self.GOFALSE(ins_parts[2])
                                if isinstance(r, int):
                                    PC = r
                                else:
                                    PC = PC + 1
                            if(ins_parts[1]=="READ"):
                                self.READ(ins_parts[2])
                                PC = PC +1 #Aumentamos el contador del programa.  
                            if(ins_parts[1]=="PRINT"):
                                self.PRINT(ins_parts[2])
                                PC = PC +1 #Aumentamos el contador del programa.  
                    else:
                        if (PC < len(self.stack_op)):
                            print("INVALID OPERATION: SKIP")
                        else:
                            break  
