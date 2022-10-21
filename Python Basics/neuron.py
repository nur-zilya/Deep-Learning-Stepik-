class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        s = sum([w1 * x1 for w1, x1 in list(zip(self.w, self.x))])
        res = self.f(s)
        return res

    def backlog(self):
        return self.x