from tkinter import Tk, Frame, Label, Button
import RPi.GPIO as GPIO
import dht11
import time



class Main(Frame):
    # initialize GPIO
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    # read data using pin 14, 15
    instance_1 = dht11.DHT11(pin=14)
    instance_2 = dht11.DHT11(pin=15)

    temp = "0"
    hum = "0"
    def __init__(self, root):
        super().__init__(root)
        self.build()

    def get_sample(self):

        result = self.instance_1.read()
        if result.is_valid():
            

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            self.temp = "Temperature: {} C".format(result.temperature)
            self.hum = "Humidity: {} %".format(result.humidity)

            self.lbl_h.configure(text=self.hum)
            self.lbl_t.configure(text=self.temp)


    def build(self):

        self.lbl_t = Label(
            text=self.temp,
            font=("Times New Roman", 21, "bold"),
            bg="#000",
            foreground="#FFF",
        )
        self.lbl_t.place(x=11, y=30)

        self.lbl_h = Label(
            text=self.hum,
            font=("Times New Roman", 21, "bold"),
            bg="#000",
            foreground="#FFF",
        )
        self.lbl_h.place(x=11, y=80)


        self.btn = Button(
            text="Get sample", bg="#FFF", font=("Times New Roman", 15), command=lambda: self.get_sample()).place(x=10, y=150, width=120, height=50)



if __name__ == "__main__":
    root = Tk()
    root["bg"] = "#000"
    root.title("DHT11")
    root.geometry("485x550+200+200")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
