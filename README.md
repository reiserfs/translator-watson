# translator-watson

Thiago <ReiserFS> Melo :: thiago@oxente.org

Python Script to translate multiple files using IBM Watson Cloud API

Usage:

 - Create an IBM cloud account in https://cloud.ibm.com/
 - Create a Language Translator-y0 resource in https://www.ibm.com/watson/services/language-translator/
 - In the Manage section copy the API key and the URL
 - Change the {api-key} and {url} variables with  your credentials
 
 - run #python3 translator.py -p subtitle.str -l en-pt 
 - It will submmit a file to the cloud you can type (#python3 translator.py) to check the status
{
  "documents": [
    {
      "document_id": "dbc14021-ae7a-4ad8-b75b-daf3b68bfa4c",
      "filename": "teste.srt",
      "model_id": "en-pt",
      "source": "en",
      "target": "pt",
      "status": "processing",
      "created": "2020-11-30T18:56:12Z",
    }
  ]
}

 - When status is avaliable:
{
  "documents": [
    {
      "document_id": "dbc14021-ae7a-4ad8-b75b-daf3b68bfa4c",
      "filename": "teste.srt",
      "model_id": "en-pt",
      "source": "en",
      "target": "pt",
      "status": "available",
      "created": "2020-11-30T18:56:12Z",
      "completed": "2020-11-30T18:56:14Z",
      "word_count": 5332,
      "character_count": 27054
    }
  ]
}

 - You can download with  #python3 translator.py -g subtitle.str


 - Submmit multiple files with: for z in /folder/folder/*.srt; do ./translator.py -p "$z"; done

 - Tou can use subtitle-me to create the srt files https://github.com/cavatron/subtitle-me 


