from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "192.168.20.90", "port": "830",
          "username": "cisco", "password": "cisco"}
print(router["host"])
print(router["port"])
print(router["username"])
print(router["password"])

netconf_filter = "*"
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
 </filter>
"*"
