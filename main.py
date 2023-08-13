from kivymd.app import MDApp
from kivy.lang import Builder
from joblib import load as loadModel
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget

#loading the model
model = loadModel("AI/savedModel.pkl")

#available symptoms
symptoms = ['itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting  urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload.1', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze']

prev_symptoms = symptoms[:]

# Main class
class MainApp(MDApp):

	def build(self):
		self.theme_cls.theme_style = 'Light'
		self.theme_cls.background_palette = 'DeepPurple'
		self.theme_cls.primary_palette = 'Cyan'
		return Builder.load_file("Design.kv")
	
	def on_start(self):
		for _,s in enumerate(symptoms):
			self.root.ids.container.add_widget(
				OneLineIconListItem(
					IconLeftWidget(
						icon = "ambulance"
					),
					text = s,
					font_style = "Button",
					theme_text_color = "Custom",
					text_color = (0,.5,1,1)
				)
			)
				
	def selectsymptom(self):
		global symptoms
		if self.root.ids.search_bar.text.lower() in symptoms:
			self.root.ids.sympt.text += f"• {self.root.ids.search_bar.text.upper()[0] + self.root.ids.search_bar.text.lower()[1:]}\n"
			symptoms[symptoms.index(self.root.ids.search_bar.text.lower())] = 1
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
		except Exception:
			self.root.ids.diagnosis.text = 'ER'
	
	def changeTheme(self,active):
		if active:
			self.theme_cls.theme_style = "Dark"
		else:
			self.theme_cls.theme_style = "Light"
			
	def clr(self):
		global symptoms
		symptoms = prev_symptoms[:]
		self.root.ids.diagnosis.text = 'NA' 
		self.root.ids.sympt.text = ''
		self.root.ids.search_bar.text = ''
		
if __name__ == '__main__':
	MainApp().run()