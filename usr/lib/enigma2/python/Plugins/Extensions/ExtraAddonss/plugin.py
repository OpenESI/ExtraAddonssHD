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
config.misc.picon_path = ConfigText(default='/media/usb')
if os.path.exists('%s' % config.misc.picon_path.value) is False:
    config.misc.picon_path.value = '/media/usb'
fold = str(config.misc.picon_path.value)
folder = fold + '/picon'
if not os.path.exists(folder):
    os.system('mkdir ' + folder)
currversion = '1.0'
host = 'aHR0cDovL3d3dy5vcGVuZXNpLmV1L3BhbmVsYWRkb25zcy54bWw='
hostxml = base64.b64decode(host)
ipkurl = 'aHR0cDovL3d3dy5vcGVuZXNpLmV1L2FkZG9ucy9FeHRyYUFkZG9uc3N1cGRhdGUvTmV3UGFuZWxIRC5pcGs='
ipk = base64.b64decode(ipkurl)

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
    skin = '''
    <screen name="addonsupdatesScreen" position="center,center" size="1280,720" title="ExtraAddonss" backgroundColor="transparent" flags="wfNoBorder">
    <widget name="text" position="84,149" size="787,475" font="Regular;22" />
    <ePixmap position="70,35" size="1149,646" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="142,61" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="959,70" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="80,87" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <eLabel name="" position="134,635" size="145,50" font="Regular; 28" valign="center" halign="center" text="Exit" zPosition="2" transparent="1" />
    </screen>

    '''
#skin fhd
#    skin = '<screen name="addonsupdatesScreen" position="center,center" size="1920,1080" title="ExtraAddonss" backgroundColor="transparent">\n<widget name="text" position="235,150" size="1020,640" font="Regular;22" />\n<ePixmap position="center,0" size="1500,880" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/Addons_news.png" transparent="1" alphatest="on" />\n<widget source="Title" render="Label" position="506,60" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />\n<widget source="global.CurrentTime" render="Label" position="1460,62" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n<widget source="global.CurrentTime" render="Label" position="235,78" size="340,37" transparent="1" zPosition="1" font="Regular; 26" valign="center" halign="left">\n      <convert type="ClockToText">Date</convert>\n    </widget>\n <eLabel name="" position="299,827" size="145,50" font="Regular; 28" valign="center" halign="center" text="Exit" zPosition="2" transparent="1" />\n</screen>'

    def __init__(self, session):
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
    skin = '''
    <screen flags="wfNoBorder" name="AboutScreen" position="center,center" size="1280,720" title="ExtraAddonss" backgroundColor="transparent">
    <widget name="text" position="84,149" size="787,475" font="Regular;22" zPosition="1" />
    <ePixmap position="70,35" size="1149,646" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/Addons_news.png" transparent="1" alphatest="on" />
    <widget source="Title" render="Label" position="142,61" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="959,70" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="80,87" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <eLabel name="" position="134,635" size="145,50" font="Regular; 28" valign="center" halign="center" text="Exit" zPosition="2" transparent="1" />
    </screen>
    '''
#skin fhd
#    skin = '<screen flags="wfNoBorder" name="AboutScreen" position="center,center" size="1920,1080" title="ExtraAddonss" backgroundColor="transparent">\n<widget name="text" position="235,150" size="1020,640" font="Regular;32" zPosition="1" />\n<ePixmap position="center,0" size="1500,880" zPosition="-10" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/Addons_news.png" transparent="1" alphatest="on" />\n<widget source="Title" render="Label" position="506,60" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />\n<widget source="global.CurrentTime" render="Label" position="1460,62" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n<widget source="global.CurrentTime" render="Label" position="235,78" size="340,37" transparent="1" zPosition="1" font="Regular; 26" valign="center" halign="left">\n      <convert type="ClockToText">Date</convert>\n    </widget>\n <eLabel name="" position="299,827" size="145,50" font="Regular; 28" valign="center" halign="center" text="Exit" zPosition="2" transparent="1" />\n </screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        info = '\n ExtraAddonss Panel for OpenESI \n ------------------------------------------ \n e-mail: support @ openesi.eu \n ------------------------------------------ \n ExtraAddonss Panel for OpenESI Your New Addons Manager \n ------------------------------------------------------------------------------------ \n wwww.openesi.eu \n ------------------------------------------ \n OpenESI Team'
        self['text'] = ScrollLabel(info)
        self['actions'] = ActionMap(['SetupActions'], {'cancel': self.close,
         'ok': self.close}, -1)


class AddonsGroups(Screen):
    skin = '''
    <screen name="AddonsGroups" position="0,0" size="1280,720" title="ExtraAddonss" backgroundColor="transparent" flags="wfNoBorder">
    <widget source="Title" render="Label" position="142,61" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="959,70" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="80,87" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <widget name="key_red" position="52,639" zPosition="5" size="329,45" valign="center" halign="center" font="Regular; 32" transparent="1" />
    <widget name="key_yellow" position="329,636" zPosition="5" size="329,45" valign="center" halign="center" font="Regular; 32" transparent="1" foregroundColor="white" />
    <widget name="key_blue" position="617,635" zPosition="5" size="329,45" valign="center" halign="center" font="Regular; 32" transparent="1" foregroundColor="white" />
    <widget font="Regular; 32" foregroundColor="white" halign="center" name="" position="872,585" size="329,45" transparent="1" valign="center" zPosition="5" backgroundColor="black" />
    <widget name="list" position="84,149" size="782,442" font="Regular;24" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />
    <widget name="info" position="82,596" zPosition="4" size="307,32" font="Regular; 22" foregroundColor="white" transparent="1" halign="right" valign="center" />
    <widget name="fspace" position="388,596" zPosition="5" size="600,32" font="Regular;22" foregroundColor="white" transparent="1" halign="left" valign="center" />
    <ePixmap position="70,35" size="1149,646" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/AddonsGroups.png" transparent="1" alphatest="on" />
    </screen>
    '''
    
#skin fhd    
    #skin = '<screen name="AddonsGroups" position="center,center" size="1920,1080" title="ExtraAddonss" backgroundColor="transparent">\n<widget source="Title" render="Label" position="506,60" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />\n<widget source="global.CurrentTime" render="Label" position="1460,62" size="226,74" font="Regular; 60" valign="center" halign="right" transparent="1" zPosition="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n<widget source="global.CurrentTime" render="Label" position="235,78" size="340,37" transparent="1" zPosition="1" font="Regular; 26" valign="center" halign="left">\n      <convert type="ClockToText">Date</convert>\n    </widget>\n      \t                <widget name="key_red" position="233,823" zPosition="5" size="329,45" valign="center" halign="center" font="Regular; 32" transparent="1" />\n\t\t\t<widget name="key_yellow" position="610,823" zPosition="5" size="329,45" valign="center" halign="center" font="Regular; 32" transparent="1" foregroundColor="white" />\n\t\t\t<widget name="key_blue" position="984,823" zPosition="5" size="329,45" valign="center" halign="center" font="Regular; 32" transparent="1" foregroundColor="white" />\n                        <widget font="Regular; 32" foregroundColor="white" halign="center" name="" position="1365,823" size="329,45" transparent="1" valign="center" zPosition="5" backgroundColor="black" />\n\t\t\t<widget name="list" position="235,150" size="1020,604" font="Regular;28" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />\t\t\t\n\t\t\t<widget name="info" position="235,770" zPosition="4" size="400,32" font="Regular; 28" foregroundColor="white" transparent="1" halign="center" valign="center" />\n\t\t        <widget name="fspace" position="655,770" zPosition="5" size="600,32" font="Regular;26" foregroundColor="white" transparent="1" halign="right" valign="center" />\n\t                <ePixmap position="center,0" size="1500,880" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/AddonsGroups.png" transparent="1" alphatest="on" />\n</screen>'

    def __init__(self, session):
        self.skin = AddonsGroups.skin
        Screen.__init__(self, session)
        self['key_red'] = Button(_('Exit'))
        self['key_green'] = Button(_('Update'))
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
        global hostxml
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
    skin ='''
    <screen name="IpkgPackages" position="center,center" size="1280,720" title="www.openesi.eu" flags="wfNoBorder" backgroundColor="transparent">
    <widget source="Title" render="Label" position="142,61" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />
    <widget source="global.CurrentTime" render="Label" position="959,70" size="226,74" font="Regular; 40" valign="center" halign="right" transparent="1" zPosition="1">
    <convert type="ClockToText">Format:%H:%M</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="80,87" size="340,37" transparent="1" zPosition="1" font="Regular; 24" valign="center" halign="left">
        <convert type="ClockToText">Date</convert>
    </widget>
    <widget name="countrymenu" position="84,149" size="658,482" font="Regular; 24" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />
    <ePixmap position="381,684" zPosition="4" size="607,61" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/extra.png.png" transparent="1" alphatest="on" />\n\t                  <ePixmap zPosition="-10" position="70,35" size="1149,646" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/hd/Addons.png" transparent="1" alphatest="on" />
    </screen>   
    '''
#skin fhd
#    skin = '<screen name="IpkgPackages" position="center,center" size="1920,1080" title="www.openesi.eu" flags="wfNoBorder" backgroundColor="transparent">\n<widget source="Title" render="Label" position="506,102" size="916,63" font="Regular; 48" transparent="1" halign="center" valign="center" zPosition="11" />\n<widget source="global.CurrentTime" render="Label" position="1627,109" size="226,74" font="Regular; 65" valign="center" halign="right" transparent="1">\n      <convert type="ClockToText">Format:%H:%M</convert>\n    </widget>\n<widget source="global.CurrentTime" render="Label" position="65,129" size="340,37" transparent="1" zPosition="1" font="Regular; 26" valign="center" halign="left">\n      <convert type="ClockToText">Date</convert>\n    </widget>\n\t\t\t  <widget name="countrymenu" position="65,210" size="1020,720" font="Regular;28" itemHeight="40" scrollbarMode="showOnDemand" zPosition="1" />\n\t                  <ePixmap position="65,936" zPosition="4" size="607,61" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/extra.png.png" transparent="1" alphatest="on" />\n\t                  <ePixmap position="0,0" zPosition="-10" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/ExtraAddonss/Addons.png" transparent="1" alphatest="on" />\n        \t</screen>'

    def __init__(self, session, xmlparse, selection):
        self.skin = IpkgPackages.skin
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
        self['actions'] = ActionMap(['SetupActions'], {'cancel': self.close,
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
