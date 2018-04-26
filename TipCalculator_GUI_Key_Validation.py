import re
import tkinter as tk
import tkinter.messagebox as mb

class TipCalc(tk.Tk):

    def __init__(self):
        super().__init__()
        self.billVar = tk.DoubleVar()
        self.tipVar = tk.DoubleVar()

        self.pattern = re.compile(r"[1-9]+")
        vcmd = (self.register(self.validateEntry), "%S")

        self.billLabel = tk.Label(self, text="Bill:")
        self.billLabel.grid(row=0, column=0)
        self.billEntry = tk.Entry(self, validate="key", validatecommand=vcmd, invalidcommand=self.inValidEntry)
        self.billEntry.grid(row=0, column=1, sticky='e' + 'w')

        self.tipLabel = tk.Label(self, text="Tip:")
        self.tipLabel.grid(row=1, column=0)
        self.tipEntry = tk.Entry(self, validate="key", validatecommand=vcmd, invalidcommand=self.inValidEntry)
        self.tipEntry.grid(row=1, column=1, sticky='e' + 'w')

        self.calcButton = tk.Button(self, text="Calculate")
        self.calcButton.bind("<Button-1>", self.totalBill)
        self.calcButton.grid(row=0, column=3)

        self.totalLabel = tk.Label(self, text="Total:")
        self.totalLabel.grid(row=2, column=0)

        self.totalOutput = tk.DoubleVar()
        self.total = tk.Label(self, textvariable=self.totalOutput)
        self.total.grid(row=2, column=1)


    def validateEntry(self, S):
        if self.pattern.match(str(S)):
            return True
        else:
            return False

    def inValidEntry(self):
        mb.showwarning("Error", "Please Enter a valid number")


    def totalBill(self, event=None):
        tipAmount = float(self.billEntry.get()) * (float(self.tipEntry.get()) / 100)
        totalAmount = float(self.billEntry.get()) + tipAmount
        self.totalOutput.set(round(totalAmount, 2))


if __name__ == "__main__":
    app = TipCalc()
    app.title("Tip Calculator")
    app.resizable(False, False)
    app.mainloop()
