## Example
#Tiesto's club life downloader

from internetarchive import get_files,get_item
fnames = [f.name for f in get_files('TiestosClubLife', glob_pattern='*ogg')]


index=input('Qual episodio voce quer? \n')

for i in fnames:
    if index in i:
        episodio=i

print('Episodio selecionado: '+episodio+'\n')
bole=input('Deseja baixar o arquivo?\n 0-Não\n 1-Sim\n')
if bool(bole):
    print('Baixando episodio: '+episodio)
    item=get_item('TiestosClubLife')
    item.download(episodio)
