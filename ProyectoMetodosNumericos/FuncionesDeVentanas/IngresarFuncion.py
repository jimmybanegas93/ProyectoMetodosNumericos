'''
Created on 3/11/2014

@author: Jimmy Ramos
'''
import sys
from PyQt4 import QtGui, QtCore
from Ventanas.IngresarFuncion import Ui_MainWindow

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnBorrar.clicked.connect(self.Borrar)
        #self.ui.btnContinuar.clicked.connect(self.Continuar)
        #self.ui.btnEvaluar.clicked.connect(self.Evaluar)
    
    #Limpiar los datos del espacio para ingresar funciones
    def Borrar(self): 
        self.ui.lnFuncion.clear()
        
    #Continuar me lleva a la pantalla de seleccionar el algoritmo con el cual resolvera la funcion
    #def Continuar(self): 
       # self.w2.show()
        
        
    #La funcion evaluar es la que me llevara a el grafico de la f(X) que haya ingresado
    #def Evaluar(self): 
       #self.w2.show()    
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())