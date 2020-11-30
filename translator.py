#!/usr/bin/env python3
import json
import sys, getopt
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apki-key}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')
def procura(arquivo, documentos):
    for majorkey, subdict in documentos.items():
        for subkey in subdict:
                jkey=json.loads(json.dumps(subkey))
                if jkey['filename'] == arquivo:
                    return jkey 
                else:
                    return 0

def main(argv):

    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv,"h:g:p:l:",["get=","put="])
    except getopt.GetoptError:
      print("error")
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('translator.py -p subtitle.str -l en-pt')
         print('translator.py --put=subtitle.str -l en-pt')
         print('translator.py -g subtitle.str')
         print('translator.py --get=subtitle.str')
         sys.exit()
      elif opt in ("-p", "--put"):
         inputfile = arg
      elif opt in ("-g", "--get"):
         outputfile = arg
      elif opt in ("-l"):
         language = arg

    documentos = language_translator.list_documents().get_result()

    duplicado = 0 

    if len(inputfile) > 1: 
        dirname, arquivo = os.path.split(inputfile)
        existe = procura(arquivo,documentos)
        if existe: 
            duplicado = 1 
            print("Arquivo " + arquivo + " e duplicado, envie outro arquivo ou baixe o existente no servidor")
        if duplicado==0:
            with open(inputfile, 'rb') as file:
                result = language_translator.translate_document(
                    file=file,
                    file_content_type='text/plain',
                    filename=arquivo,
                    model_id='en-pt').get_result()
                print(json.dumps(result, indent=2))

    if len(outputfile) > 1: 
        dirname, arquivo = os.path.split(outputfile)
        existe = procura(arquivo,documentos)
        if existe: 
            print("Baixando " + arquivo + " com o nome: " + existe['filename'])
            with open(outputfile, 'wb') as f:
                result = language_translator.get_translated_document(
                    document_id=existe['document_id'],
                    accept='text/plain').get_result()
                f.write(result.content)        
            print("Removendo do Watson: " + arquivo + " com o ID: " + existe['document_id'])
            language_translator.delete_document(document_id=existe['document_id'])

    print(json.dumps(documentos, indent=2))

if __name__ == "__main__":
   main(sys.argv[1:])
