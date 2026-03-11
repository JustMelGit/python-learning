def gen_sch(database):
	print('CREATE DATABASE IF NOT EXISTS '+ database+';')
	print('USE '+ database + ';' )


def gen_table(tables,columns):
	for e in range(len(tables)):
		pkey=True
		print('CREATE TABLE IF NOT EXISTS ' + tables[e] +' (')
		for column in columns[e]:
			char ='VARCHAR() NOT NULL'
			if 'phone' in column:
				char = 'VARCHAR(11) NOT NULL'
			if pkey:
				print('\t'+column,char,'PRIMARY KEY,')
			else:
				print('\t'+column,char+',')
			pkey = False
		print(');')


 
# myTables = ('Student Course Enrols_in').split()
# c1 = ('ssn f_name l_name phone city zip').split()
# c2 = ('number name room').split()
# c3 = ('ssn class score').split()
# col = [c1,c2,c3]

# gen_sch('school db')
# gen_table(myTables,col)


def InsV(rows,table):
	command = 'INSERT IGNORE INTO '+table+' VALUES ('
	for i in rows:
		txt = command
		for e in  range(len(i)):
			try:
				i[e]+''
				txt += '"'+ i[e] +'"'
			except:
				txt+=str(i[e])
			if not e == len(i)-1:
				txt+=','
		txt+=');'
		print(txt)
		txt = ''



# InsV([['c1','Data analytics',1127]],'Student')
