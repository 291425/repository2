from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout,QColorDialog,QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # stworzenie przycisku z napisem test
        self.button = QPushButton('Oblicz i rysuj', self)
        self.xlabel=QLabel("współrzędna XA", self)
        self.xEdit=QLineEdit()
        self.ylabel=QLabel("współrzędna YA", self)
        self.yEdit=QLineEdit()
        self.x_2label=QLabel("współrzędna XB", self)
        self.x_2Edit=QLineEdit()
        self.y_2label=QLabel("współrzędna YB", self)
        self.y_2Edit=QLineEdit()
        self.x_3label=QLabel("współrzędna XC", self)
        self.x_3Edit=QLineEdit()
        self.y_3label=QLabel("współrzędna YC", self)
        self.y_3Edit=QLineEdit()
        self.x_4label=QLabel("współrzędna XD", self)
        self.x_4Edit=QLineEdit()
        self.y_4label=QLabel("współrzędna YD", self)
        self.y_4Edit=QLineEdit()
        
        #stworzenie przycisków do wyboru koloru 
        self.clrChoose=QPushButton("Wybierz kolor", self)
        
        #stworzenie przycisku do usuwania danych 
        self.button1 = QPushButton('Usuń dane', self)
        #stworzenie przycisku do zapisywania danych do pliku
        self.button2 = QPushButton('Zapisz', self)
        
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        
        #stworzenie okienek i podpisów dla współrzędnych punktu P
        self.info = QLabel ("Informacje o Punkcie P", self)
        self.x_5label = QLabel("XP",self)
        self.x_6label = QLabel()
        self.y_5label = QLabel("YP",self)
        self.y_6label = QLabel()
        self.informacja = QLabel()
        
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        # ladne ustawienie i wyrodkowanie
        layout = QGridLayout(self)
        layout.addWidget(self.button, 9, 1, 1, -1)
        layout.addWidget(self.xlabel, 1, 1)
        layout.addWidget(self.xEdit, 1, 2)
        layout.addWidget(self.ylabel, 2, 1)
        layout.addWidget(self.yEdit, 2, 2)
        layout.addWidget(self.x_2label, 3, 1)
        layout.addWidget(self.x_2Edit, 3, 2)
        layout.addWidget(self.y_2label, 4, 1)
        layout.addWidget(self.y_2Edit, 4, 2)
        layout.addWidget(self.x_3label, 5, 1)
        layout.addWidget(self.x_3Edit, 5, 2)
        layout.addWidget(self.y_3label, 6, 1)
        layout.addWidget(self.y_3Edit, 6, 2)
        layout.addWidget(self.x_4label, 7, 1)
        layout.addWidget(self.x_4Edit, 7, 2)
        layout.addWidget(self.y_4label, 8, 1)
        layout.addWidget(self.y_4Edit, 8, 2)
        layout.addWidget(self.canvas, 10, 1, 1, -1)
        layout.addWidget(self.clrChoose, 11, 1, 1, -1)
        
        #informacje zwiazane z pkt P
        layout.addWidget(self.info, 1, 3)
        layout.addWidget(self.x_5label, 2, 3)
        layout.addWidget(self.x_6label, 3, 3)
        layout.addWidget(self.y_5label, 2, 4)
        layout.addWidget(self.y_6label, 3, 4)
        layout.addWidget(self.informacja, 4, 3)
        
        layout.addWidget(self.button1, 8, 3, 1, -1)
        layout.addWidget(self.button2, 7, 3, 1, -1)
        
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        self.button1.clicked.connect(self.usun)
        self.button2.clicked.connect(self.zapisz)

    def checkValues(self,lineE):
        if lineE.text().lstrip('-').replace('.','').isdigit():
            return float (lineE.text())
        else:
            sys.exit("zle wspolrzedne, wprowadz jeszcze raz")
            
    def rysuj(self,clr='m'):
        x=self.checkValues(self.xEdit)
        y=self.checkValues(self.yEdit)
        
        x1 = self.checkValues(self.x_2Edit)
        y1 = self.checkValues(self.y_2Edit)
        
        x2 = self.checkValues(self.x_3Edit)
        y2 = self.checkValues(self.y_3Edit)
        
        x3 = self.checkValues(self.x_4Edit)
        y3 = self.checkValues(self.y_4Edit)
        
        P1, P2=[x, x1],[y, y1]
        P3, P4=[x2, x3],[y2, y3]
        
        S=[x,y,
           x1,y1,
           x2,y2,
           x3,y3]
        M=(S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4])

        if M != 0:
            t1=((S[4]-S[0])*(S[7]-S[5])-(S[5]-S[1])*(S[6]-S[4]))/((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))
            t2=((S[4]-S[0])*(S[3]-S[1])-(S[5]-S[1])*(S[2]-S[0]))/((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))       
            XP=S[4]+t2*(S[6]-S[4])
            YP=S[5]+t2*(S[7]-S[5])
            #sprawdzenie, w którym miejscu znajduje się punkt P
            if t1>=0 and t1<=1 and t2>=0 and t2<=1:
                self.x_6label.setText(str('{:.3f}'.format(XP)))
                self.y_6label.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przecięciu dwóch odcinków')
            elif 0<=t1<=1:
                self.x_6label.setText(str('{:.3f}'.format(XP)))
                self.y_6label.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przedłużeniu odcinka CD')
            elif 0<=t2<=1: 
                self.x_6label.setText(str('{:.3f}'.format(XP)))
                self.y_6label.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przedłużeniu odcinka AB')
            else:
                self.x_6label.setText(str('{:.3f}'.format(XP)))
                self.y_6label.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przedłużeniu obu odcinków')
        
        #sprawdzneie czy nie dzielimy przez zero
        else:
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Warning)
            msg_err.setWindowTitle('Błąd')
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText('Dzielenie przez zero. Nie można obliczyć współrzędnych punktu przecięcia.')
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
        
        if x != None and y !=None:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, 'o',color=clr)
            ax.text(x,y,'A['+str(x)+','+str(y)+']')
            ax.plot(x1, y1, 'o', color=clr)
            ax.text(x1,y1,'B['+str(x1)+','+str(y1)+']')
            ax.plot(x2, y2, 'o', color=clr)
            ax.text(x2,y2,'C['+str(x2)+','+str(y2)+']')
            ax.plot(x3, y3, 'o', color=clr)
            ax.text(x3,y3,'D['+str(x3)+','+str(y3)+']')
            ax.plot((x,x1), (y,y1),'-',color=clr)
            ax.plot((x2,x3), (y2,y3),'-',color=clr)
            if M != 0:
                ax.plot(XP,YP,'o',color='black')
                ax.text(XP,YP,'P['+str('{:.3f}'.format(XP))+','+str('{:.3f}'.format(YP))+']')
                ax.plot((x,XP), (y,YP),'--',dashes=(1,5),color=clr)
                ax.plot((x1,XP),(y1,YP),'--',dashes=(1,5),color=clr)
                ax.plot((x2,XP),(y2,YP),'--',dashes=(1,5),color=clr)
                ax.plot((x3,XP),(y3,YP),'--',dashes=(1,5),color=clr)
                #plt.plot(P1, P2, P3, P4, marker='o', color=clr)
                #plt.plot(XP,YP,'o','k')
                #plt.plot(P1, P2, XP, YP,'--','k')
            self.canvas.draw() 
        #sprawdzenie czy dane zostały wprowadzone poprawnie    
        else:
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Warning)
            msg_err.setWindowTitle('Błąd')
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText('Wprowadzono niepoprawne współrzędne')
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
        
    def handleButton(self, clr='r'):
        self.rysuj()                    #rysowanie wykresu
    
    def clrChooseF(self):
         color=QColorDialog.getColor()
         if color.isValid():
             self.handleButton(color.name()) #pozwala wybrać kolor wykresu
        
    def usun(self):                 #usuwa dane z okienek
        self.xEdit.clear()
        self.yEdit.clear()
        self.x_2Edit.clear()
        self.y_2Edit.clear()
        self.x_3Edit.clear()
        self.y_3Edit.clear()
        self.x_4Edit.clear()
        self.y_4Edit.clear()
        self.x_6label.clear()
        self.y_6label.clear()
        self.informacja.clear()
        self.figure.clear()
        
        
        
    def zapisz(self):               #zapisywanie wyników do pliku
        wyniki = open('wyniki.txt','a')
        wyniki.write(55*'*')
        wyniki.write('\n|{:^10}|{:^10}|{:^30}|\n'.format('XP', 'YP', 'Informacja o punkcie P'))
        wyniki.write(55*'*')
        wyniki.write('\n|{:^10}|{:^10}|{:^30}|\n'.format(self.x_6label.text(),self.y_6label.text(), self.informacja.text()))
        wyniki.write(55*'*')

if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    
    window = Window()
    window.show()
    sys.exit(app.exec_())
    