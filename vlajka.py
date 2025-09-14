
import tkinter

class App(tkinter.Tk):
	def __init__(self, titulek, sirka, vyska):
		"""
		  konstruktor GUI aplikace (odvozené od základní třídy Tk modulu Tkinter)
		"""
		super().__init__()  # konstruktor rodičovské třídy tk modulu Tkinter
		self.title(titulek) ##### nastavení titulku okna
		# vytvorení plátna pro kreslení grafických prvků
		self.canvas = tkinter.Canvas(self, width=sirka, height=vyska, background="#000000")
		self.canvas.pack() # napojení objektu plátna do hlavního okna
	def run(self):	
		"""
		  metoda pro spuštění aplikace
		"""
		self.canvas.create_rectangle(10, 10, 310, 110,fill="white")
		self.canvas.create_rectangle(10, 110, 310, 210,fill="red")
		self.canvas.create_polygon([10,10,10,210,160,110,],fill="blue")

		##### Hlavní programová smyčka Tk (čekání na události)
		self.mainloop()
##### HLAVNÍ PROGRAM
if __name__ == "__main__":
	# vytvoření instance aplikace
	app = App("My window", 800, 600)
	# rozběhneme aplikaci
	app.run()
#### KONEC SOUBORU