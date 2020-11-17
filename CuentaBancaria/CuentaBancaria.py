class CuentaBancaria:
    num_cuenta=""
    nombre=""
    balance_general=0

    def __init__(self,num,n,balance):
        self.balance_general=balance
        self.nombre=n
        self.num_cuenta=num

    def Deposito(self):
        decision=input("Seleccione una opcion \n 1.Deposito hacia su cuenta \n 2.Deposito hacia cuentas de terceros")
        if(decision==1):
            dep=input("Cuanto dinero depositara?")
            self.balance_general=self.balance_general+dep
        elif(decision==2):
            dep=input("Cuanto dinero depositara?")
            self.balance_general=self.balance_general-dep
        else:
            print("opcion invalida")
    def impuestoBancario(self):
        impuesto=self.balance_general*.05
        self.balance_general=self.balance_general-impuesto
    def mostrar(self):
        print("Nombre:",self.nombre,"Numero de cuenta:",self.num_cuenta,"Balance general:",self.balance_general)

micuenta=CuentaBancaria("1234","jesus",100)
micuenta.mostrar()
micuenta.impuestoBancario()
micuenta.mostrar()