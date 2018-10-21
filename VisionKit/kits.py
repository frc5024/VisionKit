""" Define various avalible kits"""
import cv2

class PresetKit(object):
	""" Uses GRIP Pipelines to do simple vision tasks """
	def __init__(self, logging: bool = True) -> None:
		self.logging_enabled = logging
		self.camera = 0
		self.pipeline = None
	
	def setCam(self, cam_id: int) -> None:
		self.__LOG("Creating CV2 camera")
		self.camera = cv2.VideoCapture(cam_id)
	
	def getData(self) -> dict:
		new_frame, frame = self.camera.read()
		if new_frame:
			output = self.pipeline.process(frame)
			output["success"] = True
			return output
		else:
			return {"success": False"}
	
	def __LOG(self, text: str) -> None:
		""" Optional logging to stdout """
		if self.logging_enabled:
			print(text)