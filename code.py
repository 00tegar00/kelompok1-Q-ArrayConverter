from browser import document, alert

			bef = document["b_convertText"]
			aft = document["a_convertText"]

			def convertMain(e):
				if bef.value == '':
					alert("Silakan masukkan datanya")
					return

				addC = ''
				if document["dtop_none"].checked == True:
					addC = ''
				elif document["dtop_wq"].checked == True:
					addC = '"'
				elif document["dtop_q"].checked == True:
					addC = "'"

				nl = False
				for c in bef.value:
					if c == '\n':
						nl = True
						break
					aft.text = C4Py(bef.value, addC, nl)
			
			def C4C(data, addC, flag):
				enc = '{'
				if flag == True:
					enc += '\n	{ '
					for c in data:
						if c == '\n':
							enc = enc[:-2]
							enc += ' },\n	{ '
						else:
							enc += addC + c + addC + ', '
					enc = enc[:-2]
					enc += ' }\n}'
				elif flag == False:
					enc += ' '
					for c in data:
						enc += addC + c + addC + ', '
					enc = enc[:-2]
					enc += ' }'
				return enc
			def C4Py(data, addC, flag):
				enc = '['
				if flag == True:
					enc += '['
					for c in data:
						if c == '\n':
							enc = enc[:-2]
							enc += '], ['
						else:
							enc += addC + c + addC + ', '
					enc = enc[:-2]
					enc += ']]'
				elif flag == False:
					for c in data:
						enc += addC + c + addC + ', '
					enc = enc[:-2]
					enc += ']'
				return enc
			
			convertButton = document["convertButton"]
			convertButton.bind("click", convertMain)

			for value in vals:
				opt = document.createElement('option')
				opt.text = str(value)
				cell.appendChild(opt)