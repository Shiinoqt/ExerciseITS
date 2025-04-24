def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
    blocchi_occupati = 0

    for file in files:
        if file > spazio_totale_blocchi * 512:
            print(f'Non è possibile memorizzare il file di {file} byte. Spazio insufficiente.')
            break
        
        else:
            fileCompressed = file * 0.8
            blocchi_occupati = round(fileCompressed / 512)
            spazio_totale_blocchi -= blocchi_occupati
            print(f'File di {file} byte compresso in {fileCompressed} byte e memorizzato. Blocchi usati: {blocchi_occupati}. Blocchi rimanenti: {spazio_totale_blocchi}.')
    return