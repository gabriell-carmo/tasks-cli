frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")      
frutas.remove("banana")       
print(frutas)                 
print(frutas[0])              
print(len(frutas))        

# Dicionário — chave e valor

pessoa = {"nome": "Gabriel", "idade": 24, "cidade": "São José do Rio Preto"}
print(pessoa["nome"])         
pessoa["profissao"] = "Dev"   
del pessoa["idade"]           
print(pessoa)

# Simulando um banco de dados

usuarios = [
    {"id": 1, "nome": "Ana", "ativo": True},
    {"id": 2, "nome": "Bruno", "ativo": False},
    {"id": 3, "nome": "Carlos", "ativo": True}
]

for u in usuarios:
    print(u["nome"])

ativos = [u for u in usuarios if u["ativo"]]
print(ativos)

def buscar_por_id(id):
    return next((u for u in usuarios if u["id"] == id), None)

print(buscar_por_id(2)) 
print(buscar_por_id(9))