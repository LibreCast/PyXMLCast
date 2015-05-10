from lxml import etree

class PyXMLCast(object):
    def __init__(self, xmlFile):
        self.channel = etree.parse(xmlFile).find('channel')

    def getChannelName(self):
        return self.channel.find('title').text

    def getChannelDescription(self):
        return self.channel.find('description').text

    def getChannelURL(self):
        return self.channel.find('link').text

    def getAllVideos(self):
        items = self.channel.findall('item')
        videos = []
        
        for item in items:
            video = {
                'title':item.find('title').text,
                'description':item.find('itunes:summary',namespaces={
                    'itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd'
                }).text
            }

            if item.find('magnet') is not None:
                video['magnet'] = item.find('magnet').text

            if item.find('enclosure') is not None:
                video['enclosure'] = item.find('enclosure').attrib['url']

            videos += [video]

        return videos
