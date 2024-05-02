import random

from fileMain import PageWindow
from PyQt5 import QtCore, QtWidgets, uic

class MyApp(PageWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('compare.ui', self)  
        self.setWindowTitle("SWARMULATOR")
        self.previous.clicked.connect(self.goto_next)
        self.update_algorithm_info()
        
    def goto_next(self):
        self.goto('next')
    def update_algorithm_info(self):
        # Get the selected index
        # index = self.comboBox.currentIndex()

        # Generate random numbers for accuracy, precision, and recall
        # accuracy = round(random.uniform(0.8000, 0.9999), 4)
        # precision = round(random.uniform(0.8000, 0.9999), 4)
        # recall = round(random.uniform(0.8000, 0.9999), 4)
        self.whale_feature = ["Pregnancies","Glucose","Insulin"]
        self.coati_feature = ["Pregnancies","Glucose","output"]
        self.Gwo_feature = ["Pregnancies","Age"]
        self.abc_feature = ["Pregnancies","BloodPressure"]
        
        
        # self.label_3.setText("Whale Optimization Algorithm (WOA)")
        # self.label_4.setText(f"Accuracy Score: {accuracy}")
        # self.label_5.setText(f"Precision Score: {precision}")
        # self.label_6.setText(f"Recall Score: {recall}")

        self.label_6.setText("Whale optimization                   0.81433      0.71429")
        self.label_7.setText("Coati optimization                   0.86808      0.76623")
        self.label_8.setText("GreyWolf  optimization               0.7785       0.68831")
        self.label_9.setText("Artificial Bee Colony                0.74919      0.72727")
        self.label_10.setText( "Train")
        self.label_11.setText( "Test")

        self.label_4.setText("Precision")
        self.label_19.setText( "Whale optimization                  0.81138      0.71429")
        self.label_20.setText( "Coati optimization                  0.86866      0.76144")
        self.label_21.setText( "GreyWolf  optimization              0.78381      0.6746")
        self.label_22.setText( "Artificial Bee Colony               0.74894      0.72662")
        self.label_23.setText( "Train")
        self.label_24.setText( "Test")

        self.label_5.setText("Recall")
        self.label_25.setText( "Whale optimization                   0.81433     0.71429")
        self.label_26.setText( "Coati optimization                   0.86808      0.76623")
        self.label_27.setText( "GreyWolf  optimization               0.7785       0.68831")
        self.label_28.setText( "Artificial Bee Colony                0.74919      0.72727")
        self.label_29.setText( "Train")
        self.label_30.setText( "Test")

        self.label_31.setText( "Algorithms")
        self.label_32.setText( "Selected Features")
        self.label_33.setText( f"Whale Optimization Algorithm (WOA) =  {self.whale_feature} ")
        self.label_34.setText( f"Coati Optimization Algorithm (COA) =  {self.coati_feature} ")
        self.label_35.setText( f"Grey Wolf Optimization (GWO) =      {self.Gwo_feature}")
        self.label_36.setText( f"Artificial Bee Colony (ABC) =    {self.abc_feature}")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()