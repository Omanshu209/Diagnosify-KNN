import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from kivymd.app import MDApp
from kivy.lang import Builder

#preparing the data
df = pd.read_csv('training.csv')
df = df.drop('Unnamed: 133',axis=1)
X = df.drop('prognosis',axis = 1).copy().values
y = df['prognosis'].copy().values

#training the model using the collected data
model = KNeighborsClassifier(n_neighbors = 7)
model.fit(X,y)

#available symptoms
symptoms = ['itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting  urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload.1', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze']

prev_symptoms = symptoms[:]

#kivy design language
KV = """
MDScreen:
	
	MDTextField:
		id:search_bar
		mode:'round' 
		hint_text:'Enter Symptom...'
		icon_left:'hospital-box' 
		pos_hint:{'center_y':.96}
		size_hint:.9,None
		padding:15
		on_text:
			app.selectsymptom()
			
	MDRoundFlatButton:
		text:'Clear' 
		pos_hint:{'center_x':.95,'center_y':.96}
		size_hint:.09,.004
		on_release: 
			app.clr()
	
	MDCard:
		id:patient_symptoms
		size_hint:.25,.6
		pos_hint:{'center_x':.45,'center_y':.57}
		elevation:7
		padding:25
		spacing:25
		orientation:'vertical'
		
		Image:
			source:"assets/symptoms.png"
			size_hint_y:.4

		MDScrollView:
			do_scroll_x:False
			do_scroll_y:True
			
			MDLabel:
				id:sympt
				size_hint_y: None
				height: self.texture_size[1]
				text_size: self.width, None
				padding: 10, 10
				bold:True 
				color:(0,0,0.6,1)
				text:''
				halign:'center' 
	MDCard:
		size_hint:.35,.78
		pos_hint:{'center_x':.8,'center_y':.47}
		elevation:7
		padding:25
		spacing:25
		orientation:'vertical'
		
		Image:
			source:"assets/diagnosis.png"
			size_hint_y:.4

		MDScrollView:
			do_scroll_x:False 
			do_scroll_y:True
			
			MDLabel:
				id:diagnosis
				size_hint_y: None
				height: self.texture_size[1]
				text_size: self.width, None
				padding: 10, 10
				bold:True 
				color:(0,0,0.6,1)
				text:'NA'
				halign:'center' 

	MDRoundFlatButton:
		text:'Diagnose' 
		size_hint:.22,.15
		pos_hint:{'center_x':.45,'center_y':.16}
		on_release:app.diagnose()
	
	MDCard:
		id:all_symptoms
		size_hint:.25,.78
		pos_hint:{'center_x':.14,'center_y':.47}
		elevation:7
		padding:25
		spacing:25
		orientation:'vertical'
		
		MDRoundFlatIconButton:
			icon:'hospital-box' 
			size_hint_y: None 
			text:' | Symptoms..'
			bold:True 
			color:(1,.5,0,1)
			on_release:app.showsymptoms()

		MDScrollView:
			do_scroll_x:False 
			do_scroll_y:True
			
			MDLabel:
				id:symp
				size_hint_y: None
				height: self.texture_size[1]
				text_size: self.width, None
				padding: 10, 10
				bold:True 
				text:'Press The Button Above'
				halign:'center' 
	
	MDRectangleFlatButton:
		text:'D   e   v   e   l   o   p   e   d       B   y       O   m   a   n   s   h   u' 
		pos_hint:{'center_x':.5,'center_y':0.03}
		size_hint:1,.03
		bold:True
"""

class MainApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = 'Light' 
		self.theme_cls.primary_palette = 'Cyan'
		return Builder.load_string(KV)
		
	def showsymptoms(self):
		self.root.ids.symp.text = "Symptoms You Can Enter in the Search Bar : \n"
		for i,s in enumerate(symptoms):
			if s != 1:
				self.root.ids.symp.text += f"{i+1} ) {s}\n"
				
	def selectsymptom(self):
		global symptoms
		if self.root.ids.search_bar.text in symptoms:
			self.root.ids.sympt.text += f"•{self.root.ids.search_bar.text}\n"
			symptoms[symptoms.index(self.root.ids.search_bar.text)] = 1
			self.root.ids.search_bar.text = ""
			
	def diagnose(self):
		global symptoms
		for i,s in enumerate(symptoms):
			if s != 1:
				symptoms[i] = 0
		try:
			self.root.ids.diagnosis.text = str(model.predict([symptoms])[0])
			for i,s in enumerate(symptoms):
				if s != 1:
					symptoms[i] = prev_symptoms[i]
		except:
			self.root.ids.diagnosis.text = 'ER' 
			
	def clr(self):
		global symptoms
		symptoms = prev_symptoms[:]
		self.root.ids.diagnosis.text = 'NA' 
		self.root.ids.sympt.text = ''
		self.root.ids.search_bar.text = ''
		self.root.ids.symp.text = 'Press The Button Above'
		
if __name__ == '__main__':
	MainApp().run()