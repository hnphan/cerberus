from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.utils import timezone
#from marketplace.models import Package
from system.models import LocalPackage
from system.models import Message
from system import commands
from system import settings as systemsettings
import urllib2, json
import os
import math
import simplejson
from django.db import models
import time
import zipfile



PACKAGES_URL = 'http://cerberusserver.cloudapp.net/api/packages/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'downloads')
TEMP_DIR = os.path.join(DOWNLOAD_DIR, 'tmp')


def home(request):
	try:
		print "open url================"
		response = urllib2.urlopen(PACKAGES_URL)
		print "load json =================="
		data = json.load(response)
		print "HLLOOOOO--------->"
		return render(request, 'marketplace/index.html', {'packages':data, 'title':"marketplace"})

	except:
		print "Could not fetch packages data."
		return render(request,'marketplace/index.html', None)


def package_detail(request, package_id):
	try:
		this_package_url = PACKAGES_URL + package_id
		print "THIS PACKGAGE URL", this_package_url
		response = urllib2.urlopen(this_package_url)
		data = json.load(response)
		print data
		return render(request,'marketplace/detail.html', {'package':data})

	except:
		print "Could not fetch packages data."
		return render(request,'marketplace/detail.html', None)	


def download(request, package_id):
	'''
	Download file from url and save as file_name in DOWNLOAD_FOLDER
	'''
	
	if request.GET['command'] == "start_download":				
		packages = LocalPackage.objects.filter(pid = package_id)
		# if package has not been downloaded
		if (not packages):
			print "fresh download...."
			triggerDownload(package_id, None)
		else:
			# if package has been downloaded but not successfully installed
			# dowwnload again
			if packages[0].status != 2: 
				print "package downloaded but not installed..."
				triggerDownload(package_id, packages[0])
			else: 
				print "Package already download and installed"
		return HttpResponse(status=200)
	
	elif request.GET['command'] == "download_status":
		try: 
			package = LocalPackage.objects.get(pid=package_id)
			print simplejson.dumps({'status':package.download_status})
			return HttpResponse(simplejson.dumps({'status':package.status,'download_status':package.download_status}), 'application/json')
		except:
			# if the package object hasn't been stored in db
			return HttpResponse(simplejson.dumps({'status':-1}), 'application/json')


def triggerDownload(package_id, package_object):
	try:
		this_package_url = PACKAGES_URL + package_id
		print this_package_url
		response = urllib2.urlopen(this_package_url)
		data = json.load(response)
		url = data['location']

		if package_object==None:
			package_object = LocalPackage(pid=data['pid'],title=data['title'], developer=data['developer'], version=data['version'], status=0, location=TEMP_DIR, download_status=0)		
			package_object.save()

		req = urllib2.Request(url)

		downloaded_file = downloadChunks(url, package_object)
		# once finished downloading, send notification
		print "sending notification............................"
		commands.sendSystemMessage(content = "Cerberus has finished downloading " + package_object.title)
		print "Finished download. Start unzipping..." + systemsettings.LOCALPACKAGE_DIR
		package_object.status = 1
		package_object.save()


		filename = url.split('/')[-1].split('#')[0].split('?')[0]
		packageName = filename.split(".")[0]
		local_path = os.path.join(systemsettings.LOCALPACKAGE_DIR, packageName)	
		unzip(os.path.join(TEMP_DIR,filename), local_path)
		print "Finished unzipping...."
		package_object.location = local_path
		package_object.status = 2 # change package status to "installed"
		package_object.save()
		commands.sendSystemMessage(content = "Cerberus has installed " + package_object.title)

		#message = Message(content="Cerberus has finished downloading " + package_object.title, timestamp = timezone.now(), seen= False)
		#message.save()
		#return render(request,'marketplace/download.html', {'package':data})					
	
	except Exception as e:
		print "Exception" + e
		#return render(request,'marketplace/download.html', None)


def downloadChunks(url, package_object):
    """Helper to download large files
        the only arg is a url
       this file will go to a temp directory
       the file will also be downloaded
       in chunks and print out how much remains
    """
 
    baseFile = os.path.basename(url)
 
    #move the file to a more uniq path
    os.umask(0002)
    temp_path = TEMP_DIR
    try:
		file_ = os.path.join(temp_path,baseFile)
		req0 = urllib2.Request(url)
		req = urllib2.urlopen(req0)
		total_size = int(req.info().getheader('Content-Length').strip())
		print "total_size", total_size
		downloaded = 0
		CHUNK = 128 * 1024
		print "downloading....."
		with open(file_, 'wb') as fp:
		    print "downloading............."
		    while True:
		        chunk = req.read(CHUNK)
		        downloaded += len(chunk)
		        print "downloaded", math.floor( (float(downloaded) / float(total_size)) * 100 ), " %"
		        package_object.download_status = math.floor( (float(downloaded) / float(total_size)) * 100 )
		        package_object.save()
		        if not chunk: 
		        	break
		        print "before write"
		        fp.write(chunk)
		        print "after write"
    except urllib2.HTTPError, e:
        print "HTTP Error:",e.code , url
        return False
    except urllib2.URLError, e:
        print "URL Error:",e.reason , url
        return False
 
    return file_


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)	


