import tkinter as tk
import tkinter.messagebox as mb

class TipCalc(tk.Tk):

    def __init__(self):
        super().__init__()
        self.billVar = tk.DoubleVar()
        self.tipVar = tk.DoubleVar()

        self.billLabel = tk.Label(self, text="Bill:")
        self.billLabel.grid(row=0, column=0)
        self.billEntry = tk.Entry(self, textvariable=self.billVar)
        self.billEntry.grid(row=0, column=1, sticky='e' + 'w')

        self.tipLabel = tk.Label(self, text="Tip:")
        self.tipLabel.grid(row=1, column=0)
        self.tipEntry = tk.Entry(self, textvariable=self.tipVar)
        self.tipEntry.grid(row=1, column=1, sticky='e' + 'w')

        self.calcButton = tk.Button(self, text="Calculate")
        self.calcButton.bind("<Button-1>", self.totalBill)
        self.calcButton.grid(row=0, column=3)

        self.totalLabel = tk.Label(self, text="Total:")
        self.totalLabel.grid(row=2, column=0)

        self.totalOutput = tk.DoubleVar()
        self.total = tk.Label(self, textvariable=self.totalOutput)
        self.total.grid(row=2, column=1)


    def notPositive(self, data):
        try:
            if data <= 0:
                raise NotPositiveError
            else:
                return data
        except:
            mb.showwarning("Error", "Please Enter a valid number")


    def totalBill(self, event=None):
        if self.notPositive(self.billVar.get()) and self.notPositive(self.tipVar.get()):
            tipAmount = self.billVar.get() * (self.tipVar.get() / 100)
            totalAmount = self.billVar.get() + tipAmount
            self.totalOutput.set(round(totalAmount, 2))



if __name__ == "__main__":
    app = TipCalc()
    app.title("Tip Calculator")
    app.mainloop()
