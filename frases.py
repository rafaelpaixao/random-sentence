from enum import Enum


class Categoria(Enum):
    Engracada = "Engraçada"
    Motivacional = "Motivacional"
    Outro = "Outro"


class Frase():
    def __init__(self,
        frase,
        autor=None,
        enviado_por=None,
        categorias=[]
    ):
        self.frase = frase
        self.autor = autor
        self.categorias = categorias
        self.enviado_por = enviado_por


frases = [
"Ficar louco de vez em quando é necessidade básica para permanecer são. (Osho)", #Nome
"Uma vez ao ano é lícito fazer loucuras. (Santo Agostinho)", #Nome
"Uma pessoa que nunca cometeu um erro nunca tentou algo de novo. (ALbert Einstein)", #Jheney Vilvok
"Nos chamam de loucos, num mundo em que os certos fazem bombas.", #Igor Froehner
"All that we are is the result of what we have thought. (Buddha)", #Luísa Kinas
"Eu prefiro morrer do que perder a vida!(Chaves)",#Vitor Bernstorff Clemes
"É um erro acreditar que é possível resolver qualquer problema importante usando batatas. (Douglas Adams)", #Lais,
"O sucesso é um mestre terrível. Convence às pessoas inteligentes a pensar que não vão perder. (Bill Gates)", #Eliton Machado da Silva
"Apesar de tudo eu ainda creio na bondade humana. (Anne Frank)", #Luciano Abreu
"Prefiro uma pedra no meu caminho que uma pedra nos meus rins", #Jaasiel Abner
"Babyyyyy Shark", # Rafael Pereira
"Gentílico de quem nasce em Tubarão-SC é Baby Shark.", #MuriloLoffi
"Simplicity is prerequisite for reliability.", #Vinicius Gasparini
"Baby Shark tuturu", #Murilo Oliveira
"Bota", # Rafael Granza
"Babyyyyy Shark",# Rafael Pereira
"Se tem uma coisa que acaba com meu dia, é a noite",#Natália Speck  
"A vida e feita de escolhas, e tem gente que nao sabe escolher... (GRANZA, Rafael)",# Danilo Steps
"Quando vires um homem bom, tenta imitá-lo; quando vires um homem mau, examina-te a ti mesmo. (Confúcio)", #None
"Babuinos bobócas balbuciando em bando", #Eduarda
"Jamais, em hipótese alguma, deixe um Vogon ler poesias para você. (O guia do mochileiro das galáxias)", #Eduarda
"It’s good to be scared. It means you still have something to lose. (Richard Webber, M.D, que é um médico fictício de Grey's Anatomy, mas que tem razão em algumas de suas falas fictícias)", #Rafaéla
"Líquidos assumem a forma do recipiente e o ser humano é 70% água.", #rafaelpaixao
]


# É necessário refatorar a lista de frases, mas enquanto isso segue a solução técnica de caráter provisório:
frases = [Frase(frase, categorias=[Categoria.Outro]) for frase in frases]
