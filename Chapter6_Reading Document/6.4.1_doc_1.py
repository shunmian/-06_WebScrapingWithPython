from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO


wordFileHandler = urlopen("http://pythonscraping.com/pages/AWordDocument.docx")
wordFileString = wordFileHandler.read()             #read String from wordFielHandler
worldFielByte = BytesIO(wordFileString)             #turn String into Bytes
docuement = ZipFile(worldFielByte)                  #unzip it, because all the .docx are zipped to save space
xml_content = docuement.read('word/document.xml')   #read the unzipped file into string
print(xml_content.decode('utf-8'))

# Output:
# <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 wp14"><w:body><w:p w:rsidR="00764658" w:rsidRDefault="00764658" w:rsidP="00764658"><w:pPr><w:pStyle w:val="Title"/></w:pPr><w:r><w:t>A Word Document on a Website</w:t></w:r><w:bookmarkStart w:id="0" w:name="_GoBack"/><w:bookmarkEnd w:id="0"/></w:p><w:p w:rsidR="00764658" w:rsidRDefault="00764658" w:rsidP="00764658"/><w:p w:rsidR="00764658" w:rsidRPr="00764658" w:rsidRDefault="00764658" w:rsidP="00764658"><w:r><w:t>This is a Word document, full of content that you want very much. Unfortunately, it’s difficult to access because I’m putting it on my website as a .</w:t></w:r><w:proofErr w:type="spellStart"/><w:r><w:t>docx</w:t></w:r><w:proofErr w:type="spellEnd"/><w:r><w:t xml:space="preserve"> file, rather than just publishing it as HTML</w:t></w:r></w:p><w:sectPr w:rsidR="00764658" w:rsidRPr="00764658"><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/><w:cols w:space="720"/><w:docGrid w:linePitch="360"/></w:sectPr></w:body></w:document>

