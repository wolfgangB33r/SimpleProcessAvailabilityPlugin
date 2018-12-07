import requests
import json
import logging
import random
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name
from ruxit.api.selectors import HostSelector
from ruxit.api.selectors import ExplicitSelector
from ruxit.api.selectors import EntityType

logger = logging.getLogger(__name__)

PROCESS_NAME = "YourProcess.exe"
EVENT_TITLE = PROCESS_NAME + " not running"
EVENT_DESCRIPTION = PROCESS_NAME + " process is required, but not running on this host"

# 
class AvPlugin(BasePlugin):
    def query(self, **kwargs):
        # we search for running process group with a given name
        pg_list = self.find_all_process_groups(pgi_name(PROCESS_NAME))
        if len(pg_list) < 1:
            logger.info('Alarm process not found')
            self.results_builder.report_availability_event(description = EVENT_DESCRIPTION, title = EVENT_TITLE, properties = {}, entity_selector = HostSelector())
    
        logger.info('AvPlugin is executing: ' + str(len(pg_list)))
        
        

