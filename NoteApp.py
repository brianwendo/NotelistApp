class NotesApplication(object):
	notes_list = []
	
	def __init__(self, author):
		self.author = author
		self.notes_list = NotesApplication.notes_list

	def create (self, notes_content = None):
		#Creates a new note
		note_content = str(note_content)

		if notes_content != "None":
			self.note_list.append(notes_content)
			return self.notes_list
		else:
			return "Content cannot be empty"

	def list(self):
		#Generates a list of notes
			return self.notes_list
		

	def get(self, note_id):
		#gets a particular note in notes list
		try:
			return self.notes_list[note_id]
		except :
			return "Note not found"
			

	def search(self, search_text):
		#searches for notes and if not found returns msg
			for search_text in notes_list:
				if text.find(search_text) > -1:
					return ('Showing results for %s \n Note ID [%s] \n %s \n By Author [%s]'
				 %(search_text, self.notes_list.indexOf(text), text, self.author))
			else:
				return "Note not found"
			

	def delete(self, note_id):
		#deletes note and returns msg if note not found
		try:
			deleted_note = self.notes_list.pop([note_id])
			return deleted_note
		except:
			return" Note not found"
					


	def edit(self, note_id, new_content):
		#edits the note
		try:
			self.note_list.insert(notes_id, new_content)
			return notes_list
		except:
			return "Note not found "

