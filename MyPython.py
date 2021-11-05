from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtWidgets, uic
import sys
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
import urllib
import webbrowser
import pandas
import csv


# Main Window Code
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('CourseScrapping.ui', self)
        self.show()
        self.connectSignalsSlots()
        sys.setrecursionlimit(150000)
#         self.actionInsertion_Sort.triggered.connect(self.getChoiceInsertionSort)
#         self.actionMerge_Sort.triggered.connect(self.getChoiceMergeSort)
#         self.actionSelection_Sort.triggered.connect(self.getChoiceSelectionSort)
        self.actionQuick_Sort.triggered.connect(self.getChoiceQuickSort)
        self.actionBubble_Sort.triggered.connect(self.GetChoiceBubbleSort)
#         self.actionHeap_Sort.triggered.connect(self.getChoiceHeapSort)
#         self.actionHybirdized_Algorithms.triggered.connect(self.getChoiceHybirdizedAlgorithm)
#         self.actionOR.triggered.connect(self.getChoiceFilters)
#         self.actionIs_equal_to.triggered.connect(self.getChoiceFilters)
#         self.actionIs_not_Equal_to.triggered.connect(self.getChoiceFilters)
#         self.actionIs_less_tha.triggered.connect(self.getChoiceFilters)
#         self.actionIs_Greater_Than.triggered.connect(self.getChoiceFilters)
#         self.actionIs_Null.triggered.connect(self.getChoiceFilters)
#         self.actionIs_fretaer_than_Equal_to.triggered.connect(self.getChoiceFilters)
#         self.actionContains.triggered.connect(self.getChoiceFilters)
#         self.actionEnds_With.triggered.connect(self.getChoiceFilters)
#         self.actionStarts_with.triggered.connect(self.getChoiceFilters)
#         self.actionAbout_the_app.triggered.connect(self.OpenLink)
#         self.actionSorting_and_Searching.triggered.connect(self.OpenLink1)
        
        
#     def partition(array, start, end):
#         pivot = array[start]
#         low = start + 1
#         high = end

#         while True:

#             while low <= high and array[high] >= pivot:
#                 high = high - 1

#             while low <= high and array[low] <= pivot:
#                 low = low + 1

#             if low <= high:
#                 array[low], array[high] = array[high], array[low]
#             else:

#                 break

#         array[start], array[high] = array[high], array[start]

#         return high
#     def quickSort(array, start, end):
#         if start >= end:
#             return

#         p = partition(array, start, end)
#         quickSort(array, start, p-1)
#         quickSort(array, p+1, end)
        
#     def insertionSort(array):
#         for step in range(1, len(array)):
#             key = array[step]
#             j = step - 1
#             while j >= 0 and key < array[j]:
#                 array[j + 1] = array[j]
#                 j = j - 1
#             array[j + 1] = key
#     def mergeSort(array):
#         if len(array) > 1:
#             r = len(array)//2
#             L = array[:r]
#             M = array[r:]      
#             mergeSort(L)
#             mergeSort(M)
#             i = j = k = 0
#             while i < len(L) and j < len(M):
#                 if L[i] < M[j]:
#                     array[k] = L[i]
#                     i += 1
#                 else:
#                     array[k] = M[j]
#                     j += 1
#                 k += 1
#             while i < len(L):
#                 array[k] = L[i]
#                 i += 1
#                 k += 1

#             while j < len(M):
#                 array[k] = M[j]
#                 j += 1
#                 k += 1
#     def selectionSort(array, size):
#         for step in range(size):
#             min_idx = step

#             for i in range(step + 1, size):

#                 if array[i] < array[min_idx]:
#                     min_idx = i
#             (array[step], array[min_idx]) = (array[min_idx], array[step])
    
#     def bubbleSort(array):     
#         for i in range(len(array)):
#             for j in range(0, len(array) - i - 1):

#                 if array[j] > array[j + 1]:
#                     temp = array[j]
#                     array[j] = array[j+1]
#                     array[j+1] = temp
#     def heapify(arr, n, i):
#         largest = i
#         l = 2 * i + 1
#         r = 2 * i + 2
#         if l < n and arr[i] < arr[l]:
#             largest = l
#         if r < n and arr[largest] < arr[r]:
#             largest = r
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)

#     def heapSort(arr):
#         n = len(arr)
#         for i in range(n//2, -1, -1):
#             heapify(arr, n, i)

#         for i in range(n-1, 0, -1):
#             arr[i], arr[0] = arr[0], arr[i]
#             heapify(arr, i, 0)
#     def HybirdizedAlgorithm(arr):
#         if len(arr)>37:
#             mergeSort(arr)
#         else:
#             insertionSort(arr)
#         return arr
#     def binarySearch(array, x, low, high):

#         if high >= low:
#             mid = low + (high - low)//2
#             if array[mid] == x:
#                 return mid
#             elif array[mid] > x:
#                 return binarySearch(array, x, low, mid-1)
#             else:
#                 return binarySearch(array, x, mid + 1, high)
#         else:
#             return -1
#     def linearSearch(array, n, x):
#         for i in range(0, n):
#             if (array[i] == x):
#                 return i
#         return -1

# Connecting the Functions with GUI
    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.MessageP)
        self.pushButton.clicked.connect(self.LoadData)
        self.pushButton.clicked.connect(self.loaddata)
        self.pushButton_3.clicked.connect(self.loaddata)
        self.pushButton_3.clicked.connect(self.SettingR)
        self.pushButton_3.clicked.connect(self.ResVal)
        self.pushButton_2.clicked.connect(self.SettingR)
#Loading the data into the progress bar..        
    def LoadData(self):
        for i in range(101):
            time.sleep(.67)
            self.progressBar.setValue(i)
            self.lineEdit.setText(str(i))
            val=100-self.progressBar.value()
            self.lineEdit_2.setText(str(val))
            
#Printing message in the progress bar.            
    def MessageP(self):
        QMessageBox.about(self, "Progress", "Scrapping has Started!!")
    def SettingR(self):
        self.lineEdit.setText(str(self.progressBar.value()))
        val=100-self.progressBar.value()
        self.lineEdit_2.setText(str(val))
    def ResVal(self):
        self.lineEdit.setText(str(self.progressBar.value()))
        val=100-self.progressBar.value()
        self.lineEdit_2.setText(str(val))
        QMessageBox.about(self, "Progress", "Scrapping has Resumed at"+str(self.progressBar.value())+"%")

        for i in range(self.progressBar.value(),101):
            time.sleep(.1)
            self.progressBar.setValue(i)  
            
#Quick Sort Algorithm...
    def getChoiceQuickSort(self):
        items = ("Course Title","University Name","Course Type","Course Ratings","Number of Students","Course Level","Student Reviews")
        item, okPressed = QInputDialog.getItem(self, "Select Columns for Sorting","Column:", items, 0, False)
        def partition(array, start, end):
            pivot = array[start]
            low = start + 1
            high = end
            while True:
                while low <= high and array[high] >= pivot:
                    high = high - 1
                while low <= high and array[low] <= pivot:
                    low = low + 1
                if low <= high:
                    array[low], array[high] = array[high], array[low]
                else:
                    break
            array[start], array[high] = array[high], array[start]
            return high
        def quickSort(array, start, end):
            if start >= end:
                return
            p = partition(array, start, end)
            quickSort(array, start, p-1)
            quickSort(array, p+1, end)
        def insertionSort(array):
            for step in range(1, len(array)):
                key = array[step]
                j = step - 1
                while j >= 0 and key < array[j]:
                    array[j + 1] = array[j]
                    j = j - 1
                array[j + 1] = key
        def mergeSort(array):
            if len(array) > 1:
                r = len(array)//2
                L = array[:r]
                M = array[r:]      
                mergeSort(L)
                mergeSort(M)
                i = j = k = 0
                while i < len(L) and j < len(M):
                    if L[i] < M[j]:
                        array[k] = L[i]
                        i += 1
                    else:
                        array[k] = M[j]
                        j += 1
                    k += 1
                while i < len(L):
                    array[k] = L[i]
                    i += 1
                    k += 1

                while j < len(M):
                    array[k] = M[j]
                    j += 1
                    k += 1
        def selectionSort(array, size):
            for step in range(size):
                min_idx = step

                for i in range(step + 1, size):

                    if array[i] < array[min_idx]:
                        min_idx = i
                (array[step], array[min_idx]) = (array[min_idx], array[step])

        def bubbleSort(array):     
            for i in range(len(array)):
                for j in range(0, len(array) - i - 1):

                    if array[j] > array[j + 1]:
                        temp = array[j]
                        array[j] = array[j+1]
                        array[j+1] = temp
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)
            for i in range(n//2, -1, -1):
                heapify(arr, n, i)

            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
        def HybirdizedAlgorithm(arr):
            if len(arr)>37:
                mergeSort(arr)
            else:
                insertionSort(arr)
            return arr
        def binarySearch(array, x, low, high):

            if high >= low:
                mid = low + (high - low)//2
                if array[mid] == x:
                    return mid
                elif array[mid] > x:
                    return binarySearch(array, x, low, mid-1)
                else:
                    return binarySearch(array, x, mid + 1, high)
            else:
                return -1
        def linearSearch(array, n, x):
            for i in range(0, n):
                if (array[i] == x):
                    return i
            return -1



        Course_Title=[]
        Uni_Name=[]
        No_of_Students=[]
        Stu_Reviews=[]
        Stu_Ratings=[]
        Course_Level=[]
        Course_Type=[]

        with open('big.csv', mode ='r',encoding="utf8")as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                Course_Title.append(lines[0])
                Uni_Name.append(lines[1])
                Course_Type.append(lines[2])
                Stu_Ratings.append(lines[3])
                No_of_Students.append(lines[4])
                Course_Level.append(lines[5])
                Stu_Reviews.append(lines[6])
        if okPressed and item:
            if item=="Course Title":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                quickSort(Course_Title,0,len(Course_Title)-1)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
                end=time.time()
                h=end-start
                QMessageBox.about(self, "Sorting","Time for Sorting in Quick Sort is: "+str(h)+"s")
            elif item=="University Name":
                start=time.time()

                QMessageBox.about(self, "Sorting", "Sorting has Started for University Name!!")
                quickSort(Uni_Name,0,len(Uni_Name)-1)
                self.tableWidget.setRowCount(len(Uni_Name))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                    print("Name")
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
                end=time.time()
                h=end-start
                QMessageBox.about(self, "Sorting","Time for Sorting is: "+str(h))

            elif item=="Course Type":
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Type!!")                
                quickSort(Course_Type,0,len(Course_Type)-1)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            elif item=="Course Ratings":
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Rating!!")
                quickSort(Stu_Ratings,0,len(Stu_Ratings)-1)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            elif item=="Number of Students":
                QMessageBox.about(self, "Sorting", "Sorting has Started for Number of Students!!")
                quickSort(No_of_Students,0,len(No_of_Students)-1)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            elif item=="Course Level":
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Level!!")
                quickSort(Course_Level,0,len(Course_Level)-1)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            elif item=="Student Reviews":
                QMessageBox.about(self, "Sorting", "Sorting has Started for Student Reviews!!")
                quickSort(Stu_Reviews,0,len(Stu_Reviews)-1)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1

#         
#     def getChoiceFilters(self):
#         text1, okPressed = QInputDialog.getText(self, "Filter Box","Enter Key word:", QLineEdit.Normal, "")
#         if okPressed and text1 != '':
#             text2, okPressed = QInputDialog.getText(self, "Filter Box","Enter Key word:", QLineEdit.Normal, "")
#             if text1.isdigit()==True:
#                 if text2.isdigit==True:
#                     if len(text1)<30 and len(text2)<30:
#                         linearSearch()
#                     else:
#                         binarySearch()
#             else:


#Bubble Sort Algorithm:              
    def GetChoiceBubbleSort(self):
        items = ("Course Title","University Name","Course Type","Course Ratings","Number of Students","Course Level","Student Reviews")
        item, okPressed = QInputDialog.getItem(self, "Select Columns for Sorting","Column:", items, 0, False)
        def bubbleSort(array):     
            for i in range(len(array)):
                for j in range(0, len(array) - i - 1):
                    if array[j] > array[j + 1]:
                        temp = array[j]
                        array[j] = array[j+1]
                        array[j+1] = temp
        Course_Title=[]
        Uni_Name=[]
        No_of_Students=[]
        Stu_Reviews=[]
        Stu_Ratings=[]
        Course_Level=[]
        Course_Type=[]

        with open('big.csv', mode ='r',encoding="utf8")as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                Course_Title.append(lines[0])
                Uni_Name.append(lines[1])
                Course_Type.append(lines[2])
                Stu_Ratings.append(lines[3])
                No_of_Students.append(lines[4])
                Course_Level.append(lines[5])
                Stu_Reviews.append(lines[6])
        if okPressed and item:
            if item=="Course Title":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Course_Title)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Univeristy Name":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Uni_Name)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Course Type":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Course_Type)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Student Ratings":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Stu_Ratings)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Number of Students":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(No_of_Students)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Course Level":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Course_Level)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Student Reviews":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Stu_Reviews)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1


                
                
    def GetChoiceBubbleSort(self):
        items = ("Course Title","University Name","Course Type","Course Ratings","Number of Students","Course Level","Student Reviews")
        item, okPressed = QInputDialog.getItem(self, "Select Columns for Sorting","Column:", items, 0, False)
        def bubbleSort(array):     
            for i in range(len(array)):
                for j in range(0, len(array) - i - 1):
                    if array[j] > array[j + 1]:
                        temp = array[j]
                        array[j] = array[j+1]
                        array[j+1] = temp
        Course_Title=[]
        Uni_Name=[]
        No_of_Students=[]
        Stu_Reviews=[]
        Stu_Ratings=[]
        Course_Level=[]
        Course_Type=[]

        with open('big.csv', mode ='r',encoding="utf8")as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                Course_Title.append(lines[0])
                Uni_Name.append(lines[1])
                Course_Type.append(lines[2])
                Stu_Ratings.append(lines[3])
                No_of_Students.append(lines[4])
                Course_Level.append(lines[5])
                Stu_Reviews.append(lines[6])
        if okPressed and item:
            if item=="Course Title":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Course_Title)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Univeristy Name":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Uni_Name)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Course Type":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Course_Type)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Student Ratings":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Stu_Ratings)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Number of Students":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(No_of_Students)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Course Level":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Course_Level)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
            if item=="Student Reviews":
                start=time.time()
                QMessageBox.about(self, "Sorting", "Sorting has Started for Course Title!!")
                bubbleSort(Stu_Reviews)
                self.tableWidget.setRowCount(len(Course_Title))
                row=0
                for title in  Course_Title:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                    row=row+1
                row=0
                for ar in Uni_Name:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
                    row=row+1
                row=0
                for lo in  Course_Type:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
                    row=row+1
                row=0
                for pr in Stu_Ratings:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
                    row=row+1
                row=0
                for bd in No_of_Students:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
                    row=row+1
                row=0
                for ba in Course_Level:
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
                    row=row+1
                row=0
                for ds in Stu_Reviews:
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
                    row=row+1
    
    def loaddata(self):
        Course_Title=[]
        Uni_Name=[]
        No_of_Students=[]
        Stu_Reviews=[]
        Stu_Ratings=[]
        Course_Level=[]
        Course_Type=[]

        with open('big.csv', mode ='r',encoding="utf-8")as file:
            csvFile = csv.reader(file)

            for lines in csvFile:
                Course_Title.append(lines[0])
                Uni_Name.append(lines[1])
                Course_Type.append(lines[2])
                Stu_Ratings.append(lines[3])
                No_of_Students.append(lines[4])
                Course_Level.append(lines[5])
                Stu_Reviews.append(lines[6])
        row=0
        self.tableWidget.setRowCount(len(Course_Title))
        for title in  Course_Title:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
            row=row+1
        row=0
        for ar in Uni_Name:
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ar))
            row=row+1
        row=0
        for lo in  Course_Type:
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(lo))
            row=row+1
        row=0
        for pr in Stu_Ratings:
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(pr))
            row=row+1
        row=0
        for bd in No_of_Students:
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(bd))
            row=row+1
        row=0
        for ba in Course_Level:
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(ba))
            row=row+1
        row=0
        for ds in Stu_Reviews:
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(ds))
            row=row+1
        
    def OpenLink(self):
        webbrowser.open('https://demos.telerik.com/kendo-ui/grid/index')
    def OpenLink1(self):
        webbrowser.open('https://demos.telerik.com/kendo-ui/grid/basic-usage')
   
    
    
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()