#!/usr/bin/env python

class GeoPy(object):
	@classmethod
	def main(self, args):
		# Import list of yelp URLs from file
		print "Parsing urls from file..."
		file = open(args['f'])

		# Pull meta data and construct KML
		print "Getting Lat/Lng meta data from Yelp..."

		kml = ET.Element('kml')
		kml.attrib['xmlns'] = 'http://earth.google.com/kml/2.2'
		document = ET.SubElement(kml, 'Document')

		# Execute asynchronous requests
		def get_metadata(url):
			page = html.fromstring(urllib.urlopen(url).read())
			
			# Construct <name> node
			name = ET.Element('name')
			name.text = page.xpath("//meta[@property='og:title']/@content")[0]

			#Construct <Point><coordinates> nodes
			point = ET.Element('Point')
			coords = ET.SubElement(point, 'coordinates')
			lat = page.xpath("//meta[@property='place:location:latitude']/@content")[0]
			lng = page.xpath("//meta[@property='place:location:longitude']/@content")[0]
			coords.text = lng + ',' + lat

			#Construct <Placemark> node and append to <Document>
			placemark = ET.Element('Placemark')
			placemark.append(name)
			placemark.append(point)
			document.append(placemark)

		print "Spawning events..."
		jobs = [gevent.spawn(get_metadata, url) for url in file]
		print "Joining jobs..."
		gevent.joinall(jobs)

		print "Constructing KML..."
		rawXml = ET.tostring(kml)
		rawXml = minidom.parseString(rawXml)
		pXml = rawXml.toprettyxml(indent="    ")
		kmlFile = open("yelp.kml", 'w+')
		kmlFile.write(pXml.encode('utf8'))



if __name__ == '__main__':
	import sys, argparse, urllib, time, gevent
	import xml.etree.ElementTree as ET
	from lxml import html
	from xml.dom import minidom
	from gevent import monkey

	beginTime = int(round(time.time() *1000))
	monkey.patch_all()
    
	parser = argparse.ArgumentParser(description="Converts a list of Yelp businesses from a file to a KML Document", usage="%(prog)s [options]")
	parser.add_argument("--f", type=str, nargs="?", default="", help="Path to file containing Yelp urls", required=True)
	args = parser.parse_args()
	args = vars(args)

	YelpKml.main(args)

	endTime = int(round(time.time() * 1000))
	print "Run time:", endTime-beginTime
