# Simple Process Availability Plugin
Simple Dynatrace Python plugin that alerts on not running process

Please be aware that this plugin only runs on Dynatrace OneAgent versions greater than 156.

Just to remind myself on how to manually install the plugin:

- Create a new folder with the name of the plugin 'av_plugin' within the folder /opt/dynatrace/oneagent/plugin_deployment (need elevated user rights for doing that)
- Copy plugin.json and av_plugin.py into that folder
- Zip both files and upload it to your Dynatrace monitoring environment under Settings / Extensions
- Check in the local OneAgent log folder ( /var/log/dynatrace/oneagent/plugin/) if the plugin started to run: 
  grep av_plugin logfile
  

