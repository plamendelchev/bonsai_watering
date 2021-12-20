Module: MicroWebSrv2/

Mods: 
1) https://github.com/jczic/MicroWebSrv2/issues/38

2) MicroWebSrv2/microWebSrv2.py
```
def SetPacoConfig(self):
  self._validateChangeConf()
  self._backlog       = 4
  self._slotsCount    = 8
  self._slotsSize     = 768
  self._keepAlloc     = True
  self._maxContentLen = 16*1024
```
