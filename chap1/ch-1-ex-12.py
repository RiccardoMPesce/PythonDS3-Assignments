class LogicGate:
    def __init__(self, lbl):
        self.name = lbl
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter pin A input for gate " + self.get_label() + ": "))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):
    def __init__(self, nlbl):
        UnaryGate.__init__(self, nlbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class NandGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if not (a == 1 and b == 1):
            return 1
        else:
            return 0


class NorGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if not (a == 1 or b == 1):
            return 1
        else:
            return 0


class XorGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a != b:
            return 1
        else:
            return 0


class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

class HalfAdder(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.xor_gate = XorGate(lbl)
        self.and_gate = AndGate(lbl)

    def perform_gate_logic(self):
        return (self.xor_gate.perform_gate_logic(), self.and_gate.perform_gate_logic())
        
class FullAdder(HalfAdder):
    def __init__(self, lbl):
        super().__init__(lbl)

        self.xor_gate = XorGate(lbl)

    def perform_gate_logic(self):
        c_prev = 0

        for i in range(8):
            (s, c) = super().perform_gate_logic()
            self.pin_a = c_prev
            self.pin_b = s 
            (out_s, new_c) = super().perform_gate_logic()
            self.xor_gate.pin_a = new_c
            self.xor_gate.pin_b = c
            out_c = self.xor_gate.perform_gate_logic()
            c_prev = out_c

            return (out_s, out_c)
