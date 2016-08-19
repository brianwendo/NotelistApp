class NotesApplication(object):
	notes_list = []
	
	def __init__(self, author):
		self.author = author
		self.notes_list = NotesApplication.notes_list

	def create (self, notes_content = None):
		#Creates a new note
		if notes_list != "":
			self.note_list.append(notes_content)
			return notes_content
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
		try:

			for search_text in notes_list:
				return "Search results %s"%notes_list
		except:
			return "Note not found"
			

	def delete(self, note_id):
		#deletes note and returns msg if note not found
		try:
			deleted = self.notes_list.pop([note_id])
			return " Note deleted %s" %deleted
		except:
			return" Note not found"
					


	def edit(self, note_id, new_content):
		#edits the note
		try:
			self.note_list.insert(notes_id, new_content)
			return notes_list
		except:
			return "Note not found "

