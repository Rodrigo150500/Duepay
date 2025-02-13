def loading(descompacting = False, cleaning = False, extract_data_csv = False, extract_data_xml = False, export_to_excel = False) -> str:

    print(
        f"""
        Descompactando XMLS: {"OK" if descompacting == True else ""}
        Limpando arquivo compactado: {"OK" if cleaning == True else ""}
        Extraindo dados da planilha: {"OK" if extract_data_csv == True else ""}
        Extraindo dados dos XMLS: {"OK" if extract_data_xml == True else ""}
        Exportando para excel: {"OK" if export_to_excel == True else ""}
        """
    )