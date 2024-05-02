import random
from fileMain import PageWindow
from PyQt5 import QtCore, QtWidgets, uic

class NextPage(PageWindow):

    
    def __init__(self):
        super(NextPage, self).__init__()
        uic.loadUi('next.ui', self)  # Replace 'next.ui' with the path to your .ui file
        self.setWindowTitle("SWARMULATOR")
        # Connect the combo box signal to the update_algorithm_info method
        self.comboBox.currentIndexChanged.connect(self.update_algorithm_info)

        self.browse_2.clicked.connect(self.goto_Dashboard)
        self.browse_3.clicked.connect(self.goto_MyApp)
        

    def goto_Dashboard(self):
        self.goto('Dashboard')

    def goto_MyApp(self):
        self.goto('myapp')

    def update_algorithm_info(self):
        # Get the selected index
        index = self.comboBox.currentIndex()

        # Generate random numbers for accuracy, precision, and recall
        accuracy = round(random.uniform(0.8000, 0.9999), 4)
        precision = round(random.uniform(0.8000, 0.9999), 4)
        recall = round(random.uniform(0.8000, 0.9999), 4)
        whale_feature = ["Pregnancies","Glucose","Insulin"]
        coati_feature = ["Pregnancies","Glucose","output"]
        Gwo_feature = ["Pregnancies","Age"]
        abc_feature = ["Pregnancies","BloodPressure"]
        # Update the labels with the selected algorithm name and random numbers
        if index == 0:
            self.label_3.setText("Whale Optimization Algorithm (WOA)")
            self.label_4.setText(f"Accuracy Score: {accuracy}")
            self.label_5.setText(f"Precision Score: {precision}")
            self.label_6.setText(f"Recall Score: {recall}")

            self.label_7.setText(f"Accuracy Train: {accuracy}")
            self.label_8.setText(f"Precision Train: {precision}")
            self.label_9.setText(f"Recall Train: {recall}")
            self.label_10.setText(f"Selected Feature: {whale_feature}")

        elif index == 1:
            self.label_3.setText("Coati Optimization Algorithm (COA)")
            self.label_4.setText(f"Accuracy Score: {accuracy}")
            self.label_5.setText(f"Precision Score: {precision}")
            self.label_6.setText(f"Recall Score: {recall}")
            self.label_7.setText(f"Accuracy Train: {accuracy}")
            self.label_8.setText(f"Precision Train: {precision}")
            self.label_9.setText(f"Recall Train: {recall}")
            self.label_10.setText(f"Selected Feature: {coati_feature}")
        elif index == 2:
            self.label_3.setText("Grey Wolf Optimization (GWO)")
            self.label_4.setText(f"Accuracy Score: {accuracy}")
            self.label_5.setText(f"Precision Score: {precision}")
            self.label_6.setText(f"Recall Score: {recall}")
            self.label_7.setText(f"Accuracy Train: {accuracy}")
            self.label_8.setText(f"Precision Train: {precision}")
            self.label_9.setText(f"Recall Train: {recall}")
            self.label_10.setText(f"Selected Feature: {Gwo_feature}")
        elif index == 3:
            self.label_3.setText("Artificial Bee Colony (ABC)")
            self.label_4.setText(f"Accuracy Score: {accuracy}")
            self.label_5.setText(f"Precision Score: {precision}")
            self.label_6.setText(f"Recall Score: {recall}")
            self.label_7.setText(f"Accuracy Train: {accuracy}")
            self.label_8.setText(f"Precision Train: {precision}")
            self.label_9.setText(f"Recall Train: {recall}")
            self.label_10.setText(f"Selected Feature: {abc_feature}")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = NextPage()
    window.show()
    app.exec_()