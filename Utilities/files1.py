# import docx 
# import os
# def getText(filename):
# 	doc = docx.Document(filename)
# 	fullText = []
# 	for para in doc.paragraphs:
# 		fullText.append(para.text)
# 	return '\n'.join(fullText)

# if __name__ == '__main__':
# 	foldername = r'C:\Users\Justice\Documents\Ebooks\Projects\Strength Book with contents'
# 	all_files = os.listdir(foldername)
# 	docx_files = [filename for filename in all_files if filename.endswith('.docx')]
	
	
# 	for docx_file in docx_files:
# 		fullText = getText(foldername+'\\'+docx_file)
# 		file = open(r'C:\Users\Justice\Documents\Ebooks\Projects\Strength Book with contents'+'\\' + docx_file[:-5] +'.txt','w',encoding='utf-8')
# 		file.write(fullText)
# 		file.close()


import fitz
import glob, os
os.chdir(r'C:\Users\gnl999935\Desktop\Project')
for path,dirs,files in os.walk('.'):
	for file in files:
		if file.endswith('pdf'):
			with fitz.open(file) as doc:
				text=''
				for page in doc:
					text+=page.getText()
				textfile = open(file+'.txt', 'a+', encoding = 'utf-8')
				textfile.write(file)
				textfile.write(text)



# os.chdir('')
# pdfs = []
# for file in glob.glob('.pdf'):
# 	with fitz.open(file) as doc:
# 		text = ''
# 		for page in doc:
# 			text+=page.getText()



# import fitz
# import glob, os
# os.chdir(r'C:\Users\Justice\Docs\Cover letters\01-A - Introduction to project ENGINEERING management')
# for path,dirs,files in os.walk('.'):
# 	for file in files:
# 		if file.endswith('ppt'):
# 			ppt2pdf.file


# mydict = {'jane':'sub','kalu':'eng'}

# print(mydict.items())
# for keys, values in mydict.items():
# 	print(keys,values)