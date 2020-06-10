class FlagMachine:
    def __init__(self):
        self.stack = []
        self.instructions = []
        self.pointer = 0
        self.opcodes = {
            "PSH": lambda x: self.stack.append(int(x)),
            "POP": lambda: self.stack.pop(),
            "ADD": lambda: self.stack.append(self.stack.pop() + self.stack.pop()),
            "SUB": lambda: self.stack.append(self.stack.pop() - self.stack.pop()),
            "MUL": lambda: self.stack.append(self.stack.pop() * self.stack.pop()),
            "DIV": lambda: self.stack.append(self.stack.pop() / self.stack.pop()),
            "XOR": lambda: self.stack.append(self.stack.pop() ^ self.stack.pop()),
            "CLN": lambda: self.stack.extend([self.stack.pop()] * 2),
            "SWP": lambda: self.stack.extend([self.stack.pop(), self.stack.pop()]),
            "GET": lambda x: self.stack.append(self.stack[int(x)]),
            "JLT": self.jlt,
            "JMT": self.jmt,
            "JET": self.jet,
            "JMP": self.jmp,
            "DEL": lambda: None if self.stack.pop() else None,
            "DMP": lambda: print(self.stack),
            "###": lambda x: None
        }

    def jlt(self, x):
        a = self.stack.pop()
        b = self.stack.pop()
        if a - b > 0:
            self.pointer = self.findinst(x) - 1

    def jmt(self, x):
        a = self.stack.pop()
        b = self.stack.pop()
        if a - b < 0:
            self.pointer = self.findinst(x) - 1

    def jet(self, x):
        a = self.stack.pop()
        b = self.stack.pop()
        if a == b:
            self.pointer = self.findinst(x) - 1

    def jmp(self, x):
        self.pointer = self.findinst(x) - 1

    def findinst(self, j):
        return [i for i, x in enumerate(self.instructions) if x.strip() == "LA" + j][0]

    def execute(self, op, args):
        if op[:2] == "LA":
            return
        if len(args) != 0:
            return self.opcodes[op](args)
        else:
            return self.opcodes[op]()

    def run(self, instructions):
        print("Running...")
        self.instructions = instructions
        while self.pointer < len(instructions):
            instruction = instructions[self.pointer]
            instruction = instruction.strip()
            op = instruction[:3]
            args = instruction[3:]
            res = self.execute(op, args)
            if res is not None:
                print(chr(res))
            self.pointer += 1


if __name__ == '__main__':
    FlagMachine().run(open("flag", "r").readlines())
