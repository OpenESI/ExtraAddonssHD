from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from xml.dom import Node
from xml.dom import minidom
import os
from Components.Button import Button
from Components.ScrollLabel import ScrollLabel
from enigma import *
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from twisted.web.client import downloadPage
from twisted.web.client import getPage
import urllib
from Components.Label import Label
import base64
import urllib2
from Components.config import config, ConfigSelection, getConfigListEntry, NoSave, ConfigText, ConfigDirectory


#EDIT LULULLA -no remove please :)
import glob
config.misc.picon_path = ConfigText(default='/media/usb')
if os.path.exists('%s' % config.misc.picon_path.value) is False:
    config.misc.picon_path.value = '/media/usb'
fold = str(config.misc.picon_path.value)
folder = fold + '/picon'
if not os.path.exists(folder):
    os.system('mkdir ' + folder)
currversion = '1.0'
global hostxml, HD
host = 'aHR0cDovL3d3dy5vcGVuZXNpLmV1L3BhbmVsYWRkb25zcy54bWw='
hostxml = base64.b64decode(host)
print 'host : ', hostxml
ipkurl = 'aHR0cDovL3d3dy5vcGVuZXNpLmV1L2FkZG9ucy9FeHRyYUFkZG9uc3N1cGRhdGUvTmV3UGFuZWwuaXBr'
ipk = base64.b64decode(ipkurl)

# SETTINGS
PLUGIN_PATH = '/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss'
SKIN_PATH = PLUGIN_PATH
HD = getDesktop(0).size()
    
#EDIT LULULLA end






def updateable():
    try:
        data_upd = 'aHR0cDovL3d3dy5vcGVuZXNpLmV1L2FkZG9ucy9FeHRyYUFkZG9uc3N1cGRhdGUvdXBkYXRlZXh0cmEudHh0'
        extra = base64.b64decode(data_upd)
        fp = urllib.urlopen(extra)
        count = 0
        s1 = fp.readline()
        s1 = s1.strip()
        version = s1
        fp.close()
        if version == currversion:
            return False
        return True
    except:
        return False


updateable()

class addonsupdatesScreen(Screen):
    skinFhd = '''
    <screen name="addonsupdatesScreen" position="0,0" size="1920,1080" title="ExtraAddonss" backgroundColor="transparent" flags="wfNoBorder">
    <widget name="text" position="90,115" size="1020,640" font="Regular;28" />
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/fhd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="1110,529" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="1586,78" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">
        <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1243,78" size="340,37" transparent="1" zPosition="1" font="Regular; 30" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <eLabel name="" position="1674,848" size="145,50" font="Regular; 28" valign="center" halign="right" text="Exit" zPosition="2" transparent="1" />
    </screen>

    '''
    
    skinHd = '''
    <screen name="addonsupdatesScreen" position="center,center" size="1280,720" title="ExtraAddonss" backgroundColor="transparent" flags="wfNoBorder">
    <widget name="text" position="50,59" size="694,429" font="Regular;22" />
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="576,364" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="942,82" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="911,57" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <eLabel name="" position="1072,561" size="145,50" font="Regular; 24" valign="center" halign="right" text="Exit" zPosition="2" transparent="1" />
    </screen>
   
   
    '''

    def __init__(self, session):

        
        if HD.width() > 1280:
            self.skin = addonsupdatesScreen.skinFhd
        else:
            self.skin = addonsupdatesScreen.skinHd        
        
        Screen.__init__(self, session)
        
        info = ''
        self['text'] = ScrollLabel(info)
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions'], {'right': self['text'].pageDown,
         'ok': self.close,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown,
         'cancel': self.close,
         'left': self['text'].pageUp}, -1)
        try:
            fp = urllib.urlopen('http://openesi.eu/addons/ExtraAddonss/News.txt')
            count = 0
            self.labeltext = ''
            while True:
                s = fp.readline()
                count = count + 1
                self.labeltext = self.labeltext + str(s)
                if s:
                    continue
                else:
                    break
                    continue

            fp.close()
            self['text'].setText(self.labeltext)
        except:
            self['text'].setText('unable to download updates')


class AboutScreen(Screen):
    skinFhd = '''
    <screen flags="wfNoBorder" name="AboutScreen" position="0,0" size="1920,1080" title="ExtraAddonss" backgroundColor="transparent">
    <widget name="text" position="90,115" size="1020,604" font="Regular;28" zPosition="1" />
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/fhd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="1110,529" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="1586,78" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">
        <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1243,78" size="340,37" transparent="1" zPosition="1" font="Regular; 30" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <eLabel name="" position="1686,849" size="145,50" font="Regular; 28" valign="center" halign="right" text="Exit" zPosition="2" transparent="1" />
    </screen>

    '''
    
    skinHd = '''
    <screen flags="wfNoBorder" name="AboutScreen" position="center,center" size="1280,720" title="ExtraAddonss" backgroundColor="transparent">
    <widget name="text" position="50,59" size="694,429" font="Regular;22" />
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="576,364" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="942,82" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="911,57" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <eLabel name="" position="1072,561" size="145,50" font="Regular; 24" valign="center" halign="right" text="Exit" zPosition="2" transparent="1" />
    </screen>
    '''
    def __init__(self, session):

        if HD.width() > 1280:
            self.skin = AboutScreen.skinFhd
        else:
            self.skin = AboutScreen.skinHd        
        
        Screen.__init__(self, session)
        
        info = '\n ExtraAddonss Panel for OpenESI \n ------------------------------------------ \n e-mail: support @ openesi.eu \n ------------------------------------------ \n ExtraAddonss Panel for OpenESI Your New Addons Manager \n ------------------------------------------------------------------------------------ \n wwww.openesi.eu \n ------------------------------------------ \n OpenESI Team'
        self['text'] = ScrollLabel(info)
        self['actions'] = ActionMap(['SetupActions'], {
         'cancel': self.close,
         'ok': self.close}, -1)


class AddonsGroups(Screen):
    skinFhd = '''
    <screen name="AddonsGroups" position="0,0" size="1920,1080" title="ExtraAddonss" backgroundColor="transparent" flags="wfNoBorder">
    <widget source="Title" render="Label" position="1110,529" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="1586,78" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">
        <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1243,78" size="340,37" transparent="1" zPosition="1" font="Regular; 30" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <widget name="key_red" position="1502,849" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 32" transparent="1" />
    <widget name="key_yellow" position="1503,892" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 32" transparent="1" foregroundColor="white" />
    <widget name="key_blue" position="1505,933" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 32" transparent="1" foregroundColor="white" />
    <widget font="Regular; 32" foregroundColor="white" halign="center" name="" position="1298,990" size="329,45" transparent="1" valign="center" zPosition="5" backgroundColor="black" />
    <widget name="list" position="90,115" size="1020,604" font="Regular;28" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />
    <widget name="info" position="62,742" zPosition="4" size="400,45" font="Regular; 28" foregroundColor="white" transparent="1" halign="right" valign="center" />
    <widget name="fspace" position="463,741" zPosition="5" size="786,45" font="Regular; 28" foregroundColor="white" transparent="1" halign="left" valign="center" />
    <ePixmap position="0,0" size="1920,1080" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/fhd/AddonsGroups.png" transparent="1" alphatest="on" />
    </screen>

    '''
    
    skinHd = '''
    <screen name="AddonsGroups" position="center,center" size="1280,720" title="ExtraAddonss" backgroundColor="transparent" flags="wfNoBorder">
    <widget name="text" position="50,59" size="694,429" font="Regular;22" />
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/AddonsGroups.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="576,364" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="942,82" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="911,57" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <widget name="key_red" position="888,562" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 24" transparent="1" foregroundColor="white" />
    <widget name="key_yellow" position="888,588" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 24" transparent="1" foregroundColor="white" />
    <widget name="key_blue" position="888,614" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 24" transparent="1" foregroundColor="white" />
    <widget font="Regular; 32" foregroundColor="white" halign="center" name="" position="29,649" size="329,45" transparent="1" valign="center" zPosition="5" backgroundColor="black" />
    <widget name="list" position="50,59" size="694,429" font="Regular;24" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />
    <widget name="info" position="32,532" zPosition="4" size="307,32" font="Regular; 22" foregroundColor="white" transparent="1" halign="right" valign="center" />
    <widget name="fspace" position="338,532" zPosition="5" size="600,32" font="Regular;22" foregroundColor="white" transparent="1" halign="left" valign="center" />
    </screen>
    '''
    
    def __init__(self, session):

        if HD.width() > 1280:
            self.skin = AddonsGroups.skinFhd
        else:
            self.skin = AddonsGroups.skinHd        
        
        Screen.__init__(self, session)
        
        self['key_red'] = Button(_('Exit'))
        # self['key_green'] = Button(_('Update'))
        self['key_yellow'] = Button(_('News'))
        self['key_blue'] = Button(_('About'))
        self.list = []
        self['list'] = MenuList([])
        self['info'] = Label()
        self['fspace'] = Label()
        self.addon = 'emu'
        self.icount = 0
        self.downloading = False
        self['info'].setText('ExtraAddonss are starting')
        self.timer = eTimer()
        self.timer.callback.append(self.downloadxmlpage)
        self.timer.start(100, 1)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'blue': self.ShowAbout,
         'ok': self.okClicked,         
         'yellow': self.shownews,
         'green': self.pluginupdate,
         'cancel': self.close,
         'red': self.close}, -2)

    def ShowAbout(self):
        self.session.open(AboutScreen)

    def shownews(self):
        self.session.open(addonsupdatesScreen)

    def pluginupdate(self):
        global ipk
        softupdate = updateable()
        if softupdate == True:
            com = ipk
            dom = 'ExtraAddonss Last Version Update'
            self.session.open(Console, _('downloading-installing: %s') % dom, ['opkg install -force-overwrite %s' % com])
            return
        else:
            self.session.open(MessageBox, 'Latest Version Installed', MessageBox.TYPE_WARNING, 2)
            return

    def downloadxmlpage(self):
        # global hostxml
        url = hostxml
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Addons Download Failure, No internet connection or server down !')
        self.downloading = False

    def _gotPageLoad(self, data):
        self.xml = data
        try:
            if self.xml:
                xmlstr = minidom.parseString(self.xml)
                self.data = []
                self.names = []
                icount = 0
                list = []
                xmlparse = xmlstr
                self.xmlparse = xmlstr
                for plugins in xmlstr.getElementsByTagName('plugins'):
                    self.names.append(plugins.getAttribute('cont').encode('utf8'))

                self.list = list
                self['info'].setText('')
                self['list'].setList(self.names)
                self.downloading = True
            else:
                self.downloading = False
                self['info'].setText('Addons Download Failure, No internet connection or server down !')
                return
        except:
            self.downloading = False
            self['info'].setText('Error processing server addons data')

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['list'].getCurrent())
                self.session.open(IpkgPackages, self.xmlparse, selection)
            except:
                return


class IpkgPackages(Screen):
    skinFhd = '''
    <screen name="IpkgPackages" position="0,0" size="1920,1080" title="ExtraAddonss Panel" flags="wfNoBorder" backgroundColor="transparent">
    <widget source="Title" render="Label" position="1110,529" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="1586,78" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">
        <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1243,78" size="340,37" transparent="1" zPosition="1" font="Regular; 30" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <widget name="key_red" position="1502,850" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 32" transparent="1" />
    <widget name="countrymenu" position="90,115" size="1020,604" font="Regular;28" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />
    <ePixmap position="1074,968" zPosition="4" size="607,61" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/extra.png.png" transparent="1" alphatest="on" />
    <!--
    <ePixmap position="0,0" zPosition="-10" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/fhd/Addons.png" transparent="1" alphatest="on" />
    -->
    <ePixmap position="0,0" size="1920,1080" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/fhd/Addons_news.png" transparent="1" alphatest="on" />
    </screen>

    '''
    
    skinHd = '''
    <screen name="IpkgPackages" position="center,center" size="1280,720" title="www.openesi.eu" flags="wfNoBorder" backgroundColor="transparent">
    <ePixmap position="0,0" size="1280,720" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="576,364" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="942,82" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="911,57" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <widget name="key_red" position="888,562" zPosition="5" size="329,45" valign="center" halign="right" font="Regular; 24" transparent="1" foregroundColor="white" />
    <widget name="countrymenu" position="50,59" size="694,429" font="Regular; 24" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />
    </screen>
    '''
    
    def __init__(self, session, xmlparse, selection):
    
        if HD.width() > 1280:
            self.skin = IpkgPackages.skinFhd
        else:
            self.skin = IpkgPackages.skinHd        
        
        Screen.__init__(self, session)
        
        self.xmlparse = xmlparse
        self.selection = selection
        list = []
        for plugins in self.xmlparse.getElementsByTagName('plugins'):
            if str(plugins.getAttribute('cont').encode('utf8')) == self.selection:
                for plugin in plugins.getElementsByTagName('plugin'):
                    list.append(plugin.getAttribute('name').encode('utf8'))

                continue

        list.sort()
        self['countrymenu'] = MenuList(list)
        self['key_red'] = Button(_('Exit'))  
        self['actions'] = ActionMap(['SetupActions'], {
         'cancel': self.close,
         'ok': self.message}, -2)

    def message(self):
        self.session.openWithCallback(self.selclicked, MessageBox, _('Do you want to install?'), MessageBox.TYPE_YESNO)

    def selclicked(self, result):
        if result:
            try:
                selection_country = self['countrymenu'].getCurrent()
            except:
                return

            for plugins in self.xmlparse.getElementsByTagName('plugins'):
                if str(plugins.getAttribute('cont').encode('utf8')) == self.selection:
                    for plugin in plugins.getElementsByTagName('plugin'):
                        if plugin.getAttribute('name').encode('utf8') == selection_country:
                            urlserver = str(plugin.getElementsByTagName('url')[0].childNodes[0].data)
                            pluginname = plugin.getAttribute('name').encode('utf8')
                            self.prombt(urlserver, pluginname)
                            continue
                        else:
                            continue

                    continue

    def prombt(self, com, dom):
        global folder
        self.com = com
        self.dom = dom
        print 'self.com', self.com
        if self.selection == 'Skins':
            self.session.openWithCallback(self.callMyMsg, MessageBox, _('Do not install any skin unless you are sure it is compatible with your image.Are you sure ?'), MessageBox.TYPE_YESNO)
        if self.com.endswith('.ipk'):
            self.timer = eTimer()
            self.session.open(Console, _('Installing: %s') % self.dom, ['opkg install -force-overwrite -force-depends %s' % self.com])
            self.timer.callback.append(self.deletetmp)
            self.timer.start(1000, 1)
        elif self.com.endswith('.tar.gz'):
            self.timer = eTimer()
            self.session.open(Console, _('Installing: %s') % self.dom, ['tar -xzvf ' + '/tmp/download.tar.gz' + ' -C /'])
            self.timer.callback.append(self.deletetmp)
            self.timer.start(1000, 1)
            os.system('wget %s -O /tmp/download.tar.gz > /dev/null' % self.com)
            self.mbox = self.session.open(MessageBox, _('Installation performed successfully!'), MessageBox.TYPE_INFO, timeout=5)
        elif self.com.endswith('.tar.bz2'):
            self.timer = eTimer()
            os.system('wget %s -O /tmp/download.tar.bz2 > /dev/null' % self.com)
            self.timer.callback.append(self.deletetmp)
            self.timer.start(1000, 1)
            self.session.open(Console, _('Installing: %s') % self.dom, ['tar -xyvf ' + '/tmp/download.tar.bz2' + ' -C /'])
            self.mbox = self.session.open(MessageBox, _('Installation performed successfully!'), MessageBox.TYPE_INFO, timeout=5)
        elif self.com.endswith('.tbz2'):
            self.timer = eTimer()
            os.system('wget %s -O /tmp/download.tbz2 > /dev/null' % self.com)
            self.timer.callback.append(self.deletetmp)
            self.timer.start(1000, 1)
            self.session.open(Console, _('Installing: %s') % self.dom, ['tar -xyvf ' + '/tmp/download.tbz2' + ' -C /'])
            self.mbox = self.session.open(MessageBox, _('Installation performed successfully!'), MessageBox.TYPE_INFO, timeout=5)
        elif self.com.endswith('.tbz'):
            self.timer = eTimer()
            os.system('wget %s -O /tmp/download.tbz > /dev/null' % self.com)
            self.timer.callback.append(self.deletetmp)
            self.timer.start(1000, 1)
            self.session.open(Console, _('Installing: %s') % self.dom, ['tar -xyvf ' + '/tmp/download.tbz' + ' -C /'])
            self.mbox = self.session.open(MessageBox, _('Installation performed successfully!'), MessageBox.TYPE_INFO, timeout=5)
        elif self.com.endswith('.zip'):
            if 'picon' in self.dom.lower() and self.com.endswith('.zip'):
                self.folder = folder
                self.timer = eTimer()
                os.system('wget %s -O /tmp/download.zip > /dev/null' % self.com)
                self.timer.callback.append(self.deletetmp)
                self.timer.start(1000, 1)
                checkfile = '/tmp/download.zip'
                if os.path.exists(checkfile):
                    os.system('unzip -o /tmp/download.zip -d %s' % self.folder)
                    os.system('rm -rf /tmp/download.zip')
                    self.mbox = self.session.open(MessageBox, _('Installation performed successfully!'), MessageBox.TYPE_INFO, timeout=5)
            else:
                self.timer = eTimer()
                self.timer.start(1000, True)
                downplug = self.dom.replace(' ', '') + '.zip'
                os.system('wget %s -O /tmp/%s > /dev/null' % (self.com, downplug))
                self.mbox = self.session.open(MessageBox, _('Download file in /tmp successful!'), MessageBox.TYPE_INFO, timeout=5)
        else:
            self.mbox = self.session.open(MessageBox, _('Download failed!'), MessageBox.TYPE_INFO, timeout=5)

    def deletetmp(self):
        os.system('rm -f /tmp/*.ipk;rm -f /tmp/*.tar;rm -f /tmp/*.zip;rm -f /tmp/*.tar.gz;rm -f /tmp/*.tar.bz2;rm -f /tmp/*.tar.tbz2;rm -f /tmp/*.tar.tbz')

    def callMyMsg(self, result):
        if result:
            dom = self.dom
            com = self.com
            self.session.open(Console, _('downloading-installing: %s') % dom, ['ipkg install -force-overwrite %s' % com])


def main(session, **kwargs):
    session.open(AddonsGroups)


def Plugins(**kwargs):
    return PluginDescriptor(description=_('ExtraAddonss V1.0'), fnc=main, icon='plugin.png', name='OpenESI Addons Panel', where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU])