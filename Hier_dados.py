import ctypes

class Abstract:
    def __init__(self, iterator = None):
        self.n = 0
        self.capacity = 1 
        self.A = self.make_array(self.capacity)
        try:
            self.extend(iterator)
        
        except:
            if type(iterator) ==  type(None):
                pass
            else:
                raise TypeError("iterator argument must be iterable")
    
    def __len__(self) -> int:
        return self.n
    
    def __getitem__(self, position):
        if not -self.n <= position < self.n :
            raise IndexError("Invalid index")
        if position >= 0:
            return self.A[position]
        else:
            return self.A[self.n + position]
    
    def __setitem__(self, position:int, value) -> None:
        if not -self.n <= position < self.n :
            raise IndexError("Invalid index")
        self.A[position] = value
    
    def __str__(self) -> str:
        string = "["
        counter = 0
        for i in self:
            counter += 1 
            string += str(i)
            if counter != self.n:
                string += ", "
        string += "]"
        return string 

    def empty(self) -> bool:
        return self.n == 0
    
    def append(self, obj) -> None:
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.A[self.n] = obj
        self.n += 1 

    def push( self, obj) -> None:
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        
        B = self.make_array(self.capacity)
        B[0] = obj
        for i in range(self.n):
            B[i+1] = self.A[i]
        self.A = B
        self.n += 1 

    def pop(self, x = -1):
        if 0 > x >= -self.n:
            x = self.n + x
        elif x < -self.n:
            raise IndexError("Invalid index")
        elif  self.n == 0:
            raise IndexError("Underflow occurred")
        removed = self.A[x]
        B = self.make_array(self.capacity)
        for i in range(self.n):
            if i < x:
               B[i] = self.A[i]
            elif i > x:
                B[i-1] = self.A[i]
        self.A = B
        self.n -= 1
        return(removed)
    
    def reverse(self):
        B = self.make_array(self.capacity)
        for i in range(self.n):
            B[i] = self[-i-1]
        self.A = B
    
    def index(self, x) -> int:
        for i in range(self.n):
            if self.A[i] == x:
                return i
            elif i != self.n-1:
                pass
            else:
                raise ValueError("array.index(x): x not in array")
            
    def remove(self, x):
        if  self.n == 0:
            raise IndexError("Underflow occurred")
        
        ix=self.index(x)
        B = self.make_array(self.capacity)
        
        for i in range(self.n):
            if i < ix:
               B[i] = self.A[i]
            elif i > ix:
                B[i-1] = self.A[i]
        
        self.A = B
        self.n -= 1

    def count(self, x):
        counter = 0
        for i in range(self.n):
            if self.A[i] == x:
                counter +=1 
        return(counter)
    
    def insert(self, ix, x):
        
        if ix < 0:
            ix = self.n + ix
        elif self.n == self.capacity:
            self.resize(2 * self.capacity)

        B = self.make_array(self.capacity)
        
        for i in range(self.n):
            if i < ix:
                B[i] = self.A[i]
            elif i == ix:
                B[i] = x
                B[i+1] = self.A[i]
            elif i > ix:
                B[i+1] = self.A[i]
        
        self.A = B
        self.n += 1

    def extend(self, x):
        for i in x:
            self.append(i)

    def resize(self, c) -> None:
        B = self.make_array(c)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = c

    def make_array(self, c) -> None:
        return(c * ctypes.py_object)()


        return(c * ctypes.py_object)()
    
class Note_simp:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
                
class Li_En_Sim:
    def __init__(self):
        self.head = None
        
    def Ini(self, valor):
        self.head = Note_simp(valor[0]) 
        Ult_Note = Note_simp(valor[1])
        self.head.prox = Ult_Note
        for i in range(len(valor)-2):
            print(i+2)
            Ult_Note.prox = Note_simp(valor[i+2])
            Ult_Note = Ult_Note.prox    
        Ult_Note.prox = None
        
    def Push(self, new_valor):
        new_note = Note_simp(new_valor)
        new_note.prox = self.head 
        self.head = new_note 
        
    def Pop(self):
        val = self.head.valor
        self.head = self.head.prox
        return val
    
    def Len(self):  
        note = self.head
        Len = 0
        while note != None:
            Len +=1
            note = note.prox 
        return Len
    
    def Item(self, idx):  
        note = self.head
        for i in range(idx-1):
            note = note.prox  
        print(note.valor)
        return note.valor
    
    def Print(self): 
        note = self.head
        val = []
        while note != None:
            val.append(note.valor)
            note = note.prox  
        print(val)
        return val
        
class Note_Dup:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ult = None 
                
class Li_En_Dup(Li_En_Sim):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def Ini(self, valor):
        self.head = Note_Dup(valor[0]) 
        Ult_Note = Note_Dup(valor[1])
        self.head.prox = Ult_Note
        
        for i in range(len(valor)-2):
            New_Note = Note_Dup(valor[i+2])
            Ult_Note.prox = New_Note
            New_Note.ult = Ult_Note
            Ult_Note = New_Note 
            
        self.tail = Ult_Note
        Ult_Note.prox = None
                                           
    def Push(self, New_Valor):
        New_Note = Note_Dup(New_Valor)
        New_Note.prox = self.head 
        self.head.ult = New_Note
        self.head = New_Note 
        
    def Pop(self):
        val = self.head.valor
        self.head = self.head.prox
        self.head.ult = None
        return val
    
    def Push_Back(self, New_Valor):
        New_Note = Note_Dup(New_Valor)
        New_Note.ult = self.tail 
        self.tail.prox = New_Note
        self.tail = New_Note 
        
    def Pop_Back(self):
        val = self.tail.valor
        self.tail = self.tail.ult
        self.tail.prox = None
        return val
    
    def Swap(self, idx): 
        note = self.head
        for i in range(idx-1):
            note = note.prox  
        val = note.valor
        note.valor = note.prox.valor
        note.prox.valor = val
        return 
    
    def Bubble_Sort(self): 
        note = self.head
        change = 1
        while change != 0:
            change = 0
            note = self.head
            while note != self.tail:
                if note.valor > note.prox.valor:
                    change +=1
                    val = note.valor
                    note.valor = note.prox.valor
                    note.prox.valor = val                    
                note = note.prox  
        return 

class lista_stack(Li_En_Sim):
    
    def swap(self):
        if self.Len() < 2:
            raise IndexError("two or more elements are needed")
        
        last = self.Pop()
        second_last = self.Pop()

        self.Push(last)
        self.push(second_last)

class Dyn_Array(Abstract):
    def __setitem__(self, position:int, value) -> None:
        if not -self.n <= position < self.n :
            raise IndexError("Invalid index")
        elif self.n != 0 and type(value) != type(self.A[0]):
            raise TypeError("value must be the same type as other values in the array")
        self.A[position] = value
    
    def push( self, obj) -> None:
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        elif self.n != 0 and type(obj) != type(self.A[0]):
            raise TypeError("value must be the same type as other values in the array")
        
        B = self.make_array(self.capacity)
        B[0] = obj
        for i in range(self.n):
            B[i+1] = self.A[i]
        self.A = B
        self.n += 1 
   
    def append(self, obj) -> None:
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        elif self.n != 0 and type(obj) != type(self.A[0]):
            raise TypeError("value must be the same type as other values in the array")
        self.A[self.n] = obj
        self.n += 1



q = Li_En_Dup()
q.Ini([1,2])
q.Pop()
q.Print()
q.Push_Back(None)
q.Pop()
q.Print()





