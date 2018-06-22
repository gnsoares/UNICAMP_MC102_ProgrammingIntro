# Funcao que verifica a validade de um email inserido
    # Retorna 0 se o email for valido
    # Retorna -1 caso contrario
def checkEmail(email):
    import re   
    # O email deve ter o formato usuario@servidor.dominio
    a = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+')
    m = a.search(email)
    if m is not None:
        # O dominio deve ter entre 2 e 4 caracteres
        dom = m.group().split('.')[-1]
        if len(dom) > 1 or len(dom) < 5:
            # Todos os criterios foram atendidos
            return 0
    # Algum criterio nao foi atendido
    return -1

# Funcao que verifica a validade de uma senha inserida
    # Retorna 0 se a senha for valida
    # Retorna -1 caso contrario        
def checkSenha(senha):
    import re
    # A senha deve ter um tamanho maior ou igual a 8
    if len(senha) < 8:
        return -1
    # A senha deve conter ao menos um caracter especial
    spe = ['!','@','#','$','&','*']
    for i in spe:
        a = re.compile(i)
        m = a.search(senha)
        if m is not None:
            break
    else:
        return -1
    # A senha deve conter ao menos 2 numeros
    a = re.compile(r'\d')
    m = a.findall(senha)
    if len(m) < 2:
        return -1
    # A senha deve conter ao menos 1 letra maiuscula
    a = re.compile(r'[A-Z]')
    m = a.findall(senha)
    if m == []:
        return -1
    # A senha deve conter ao menos 2 letras minusculas
    a = re.compile(r'[a-z]')
    m = a.findall(senha)
    if len(m) < 2:
        return -1
    # A senha e forte
    return 0

class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

class Repositorio:
    def __init__(self):
        self.alunos = []

    def adicionar(self, aluno):
        # Procura de algum aluno com o RA inserido
        for i in range(len(self.alunos)):
            if aluno.ra == self.alunos[i].ra:
                # Um aluno ja possui o RA inserido
                raise RAInvalido()
        # Verificacao se a senha e o email inserido sao validos
        if checkSenha(aluno.senha) != 0:
            raise SenhaFraca()
        if checkEmail(aluno.email) != 0:
            raise EmailInvalido()
        # Caso sejam validos o aluno e adicionado
        self.alunos.append(aluno)
        return None

    def alterar(self, aluno):
        # Procura do aluno com o RA inserido
        for i in range(len(self.alunos)):
            if aluno.ra == self.alunos[i].ra:
                # Com o aluno encontrado, e preciso verificar se a senha e o email inserido sao validos
                if checkSenha(aluno.senha) != 0:
                    raise SenhaFraca()
                else:
                    if checkEmail(aluno.email) != 0:
                        raise EmailInvalido()
                    else:
                        # Caso sejam validos os dados sao alterados
                        self.alunos[i].nome = aluno.nome
                        self.alunos[i].email = aluno.email
                        self.alunos[i].usuario = aluno.usuario
                        self.alunos[i].senha = aluno.senha
                return None
        # Nenhum dos alunos tem o RA inserido         
        raise RAInvalido()

    def achaAluno(self, ra):
        # Procura do aluno com o RA inserido
        for i in range(len(self.alunos)):
            if ra == self.alunos[i].ra:
                # O RA inserido foi encontrado e a funcao retorna os dados do aluno respectivo
                return self.alunos[i]
        # Nenhum dos alunos tem o RA inserido
        raise RAInvalido()

    def remover(self, ra):
        # Procura do aluno com o RA inserido
        for i in range(len(self.alunos)):
            if ra == self.alunos[i].ra:
               # O RA inserido foi encontrado e sera removido
               self.alunos.pop(i)
               return None
        # Nenhum dos alunos tem o RA inserido
        raise RAInvalido()

    def limparRepositorio(self):
        # O repositorio e inicializado novamente
        self.alunos = []
        return None
