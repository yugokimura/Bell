from watson_developer_cloud import SpeechToTextV1
import json

STT = SpeechToTextV1(
 	username = "4b01ef0b-1d88-4d81-8702-9e4d0c220322",
	password =  "BLbpaO6ImMP2",
	x_watson_learning_opt_out=False
)

with open('test1.wav', 'rb') as audio_file:
	r = STT.recognize(
		audio_file,
		model='ja-JP_NarrowbandModel',
		content_type='audio/wav',
		timestamps=True,
		word_confidence=True
	)


print json.dumps(r, indent=2)

data = json.loads(json.dumps(r, indent=2))
alt = data['results'][0]['alternatives']
i=0
for item in alt:
	print item['transcript']

	i += 1
