from classes.interfaces import Interface  as IF

class Test():
    def __init__(self):
        self.resultados = {}
        pass

    def main(self):
        if self.criar_dfs('dfs/test/'): self.resultados['dfs'] = True
        else: self.resultados['dfs'] = False

        if self.test_01(): self.resultados['test_01'] = True
        else:self.resultados['test_01'] = False
        
        return self.resultados

    def criar_dfs(self, dfs_path):
        return True

    def test_01(self):
        return True

