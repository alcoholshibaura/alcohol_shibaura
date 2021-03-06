#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file center.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
center_spec = ["implementation_id", "center",
		 "type_name",         "center",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "VenderName",
		 "category",          "Controller",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class center
# @brief ModuleDescription
#
#
class center(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_hands = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._handsIn = OpenRTM_aist.InPort("hands", self._d_hands)
		self._d_people = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._peopleIn = OpenRTM_aist.InPort("people", self._d_people)
		self._d_content = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._contentOut = OpenRTM_aist.OutPort("content", self._d_content)
		self._d_move = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._moveOut = OpenRTM_aist.OutPort("move", self._d_move)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable

		# Set InPort buffers
		self.addInPort("hands",self._handsIn)
		self.addInPort("people",self._peopleIn)

		# Set OutPort buffers
		self.addOutPort("content",self._contentOut)
		self.addOutPort("move",self._moveOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):
		print("Activated")
		self.indata = [0,0]
		return RTC.RTC_OK

	##
	#
	# The deactivated action (Active state exit action)
	# former rtc_active_exit()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onDeactivated(self, ec_id):
		print("Deactivated")
		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#

	def onExecute(self, ec_id):
		if self._handsIn.isNew():
			self._d_hands = self._handsIn.read()
			self.indata[0] = self._d_hands.data
		
		if self._peopleIn.isNew():
			self._d_people = self._peopleIn.read()
			self.indata[1] = self._d_people.data
	
		print(self.indata)

		if self.indata[0] < 10:
			print('Go')
			self._d_content.data = 1  # 0:???????????? 1:???????????? 2:?????????????????????
			self._contentOut.write()
			time.sleep(10)
			self._d_move.data = 1
			self._moveOut.write()

		elif self.indata[1] == 1:
			print('Go')
			self._d_content.data = 2
			self._contentOut.write()
			self._d_move.data = 0
			self._moveOut.write()

		else:
			self._d_content.data =0
			self._contentOut.write()
			self._d_move.data =0
			self._moveOut.write()
		
		

		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def centerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=center_spec)
    manager.registerFactory(profile,
                            center,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    centerInit(manager)

    # Create a component
    comp = manager.createComponent("center")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

