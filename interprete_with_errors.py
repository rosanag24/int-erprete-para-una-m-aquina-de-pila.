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
        if (item == "true"):
            self.stack.append(True)
        else:
            if (item =="false"):
                self.stack.append(False)
            else:
                if(item.isdigit()):
                    self.stack.append(int(item)) 
                else:
                    print("INVALID INPUT")
#POP:
    def POP(self):
        self.stack.pop()
#ADD:
    def ADD(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE ADD <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) + int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#SUB:
    def SUB(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE SUBTRACT <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) - int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#MUL:
    def MUL(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE MULTIPLY <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) * int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#DIV:
    def DIV(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE DIVIDE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1)/int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#AND:
    def AND(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) and isinstance(i1,bool):
                self.stack.append(bool(i1) and bool(i2))
            else:
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#OR:
    def OR(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) and isinstance(i1,bool):
                self.stack.append(bool(i1) or bool(i2))
            else:
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
                
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
        
#LT:
    def LT(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) < int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#LE:
    def LE(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) <= int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#GT:
    def GT(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) > int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#GE:
    def GE(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) >= int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#EQ:
    def EQ(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) == int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#NEQ:
    def NEQ(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            if (isinstance(i2,bool)) or isinstance(i1,bool):
                print("ERROR: IT'S NOT POSSIBLE COMPARE <",i1,"> WITH <",i2,">")
            else:
                self.stack.append(int(i1) != int(i2))
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#UMINUS:
    def UMINUS(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            if isinstance(i1,int):
                self.stack.append(-int(i1))
            else:
                print("ERROR: VALUE <",i1,"> IS NOT AN INTEGER")
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#NOT:
    def NOT(self):
        if(len(self.stack) > 0):     
            i1 = self.stack.pop()
            if isinstance(i1,bool):
                self.stack.append(not bool(i1))
            else:
                print("ERROR: VALUE <",i1,"> IS NOT A BOOLEAN")
        else:
            print("ERROR: MISSING VALUE, THERE ARE NOT ENOUGHT ELEMENTS IN THE STACK")
#RVALUE:
    def RVALUE(self, id):
        self.stack.append(self.rval[id])
#LVALUE:
    def LVALUE(self, id):
        self.lval[id] = id
        self.stack.append(self.lval[id])
#ASSIGN:
    def ASSIGN(self):
        if(len(self.stack) > 1):
            i1 = self.stack.pop()
            i2 = self.stack.pop()
            self.rval[i1] = int(i2)
        else:
            print("ERROR: UNABLE ASSIGNATION NOT ENOUGHT ELEMENTS ON STACK")
#GOTO:
    def GOTO(self, lb):
        if (lb in self.labels):
            return self.labels[lb]
        else:
            print("ERROR: LABEL <",lb,"> DOESN'T EXIST")
#GOTRUE:
    def GOTRUE(self, lb):  
        if(len(self.stack)>=0):          
            p = self.stack.pop()
            if (lb in self.labels):
                if (isinstance(p,bool)):
                    if (p):
                        return self.labels[lb]
                else:
                    print("ERROR: VALUE ",p," IS NOT A BOOLEAN")
            else:
                print("ERROR: NON EXISTENT LABEL")
        else:
            print("ERROR: NOT ENOUGHT ITEMS IN THE STACK")
#GOFALSE:
    def GOFALSE(self, lb):  
        if(len(self.stack)>=0):          
            p = self.stack.pop()
            if (lb in self.labels):
                if (isinstance(p,bool) ):
                    if (not p): 
                        return self.labels[lb]
                else:
                    print("ERROR: VALUE ",p," IS NOT A BOOLEAN")
            else:
                print("ERROR: NON EXISTENT LABEL")
        else:
            print("ERROR: NOT ENOUGHT ITEMS IN THE STACK")
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
        if(id in self.rval):
            print(self.rval[id])
        else: 
            print("ERROR: NOT EXISTENT VALUE FOR ID <",id,">" )

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


# FUNCIONES AUXILIARES
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
#sin_salto, elimina el salto de linea anexado al ultimo elemento de la instruccion
    def sin_salto(self, i):
        j = i[0:len(i)-1]
        return j

#CORRIDA DE LA PILA
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
