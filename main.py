import sys
import kivy
import re
import calc #This module parse mathematical expressions and calculates them. 
kivy.require('1.0.6')
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import  BoxLayout

__author__='kandalf'

class KivyCalc(App):
	def build(self): #Main function of Application. 
		Window.clearcolor = (.5, .5, .5, 1) #Background color of window
		layout = BoxLayout(orientation='vertical')
		self.textbox = TextInput(background_color=[.1,.7,.5,1],font_name="DS-DIGI.TTF",font_size=40)
		self.textbox.bind(text=self.sanitizee) #Runs function when text is changed
		layout.add_widget(self.textbox)
		self.keypad = GridLayout(cols=4)
		self.showKeypad()
		layout.add_widget(self.keypad)
		return layout #Render layout object.
	
	def sanitizee(self,obj,val):
		self.textbox.text = re.sub('[^.+0-9 EPSINCOTA^/*-=\n()]', '', val) #Only this characters allowed
			
		
	def showKeypad(self): #Defines Keypad values and add them GridLayout
		
		for i in range(1,10): #Numeric Keys is auto created.
			self.numeric = Button(text=str(i))
			self.numeric.bind(on_press=self.callback)
			self.keypad.add_widget(self.numeric)
		
		fnkeys = {0:"0", 1:"CLEAR", 2:"=", 3:"+", 4:"-", 5:"*" ,6:"/", 7:".", 8:"(", 9:")", 10:"E", 11:"PI", 12:"SIN", 13:"COS", 14:"TAN"}
		
		for key in fnkeys: #Function Keys is auto created.
			self.fnkey = Button(text=fnkeys[key])
			self.fnkey.bind(on_press=self.callback)
			self.keypad.add_widget(self.fnkey)
	
	# This fuction runs when click keys on keypad. Kivy doesn't support call function with custom parameters, so
	# I get values of button objects for identify them. (obj.text).
	
	def callback(self,obj):
		
		print obj #Print Debug Information
		
		if obj.text == "CLEAR":
			self.textbox.text = ''
		elif obj.text == "=":
			lastExp = self.textbox.text.split("\n")[-1] #This get last expression from textbox for calculation.
			calc_=calc.NumericStringParser()
			try:
				self.textbox.text =  self.textbox.text  + " = " + str(calc_.eval(lastExp)) + "\n"
			except:	
				self.textbox.text =  self.textbox.text  + " = " + "E" + "\n" #Throws error
		else:
			self.textbox.text =  self.textbox.text + obj.text
				
if __name__ == '__main__':
	KivyCalc().run() #Runs Application.
