from internetarchive import get_files,get_item


print('Bem vindo ao IA downloader!!')

repositorio= input('Qual o nome do repositorio que deseja baixar?')
extensão= input('Qual a extensão do arquivo que deseja baixar?')

print(f"Listando arquivos no repositorio {repositorio} no formato *{extensão} abaixo: ")

fnames = [f.name for f in get_files(repositorio, glob_pattern=f"*{extensão}")]
print(fnames)

index=input('Qual arquivo voce quer? \n')

for i in fnames:
    if index in i:
        arquivo=i

print('Arquivo selecionado: '+arquivo+'\n')
bole=input('Deseja baixar o arquivo?\n 0-Não\n 1-Sim\n')
if bool(bole):
    print('Baixando arquivo: '+arquivo)
    item=get_item('TiestosClubLife')
    item.download(arquivo)
else:
    print('exit')