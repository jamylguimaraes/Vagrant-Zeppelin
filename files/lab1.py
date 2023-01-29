#!/usr/bin/env python2
import os
import tarfile
import xml.etree.ElementTree as ET

def java_install():
	if os.path.exists('jdk-17_linux-x64_bin.rpm') :
		print("Download do JDK ja existe")
	else :
		os.system('wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.rpm')
		print("Download do Java Completo!")
		os.system('yum -y localinstall jdk-17_linux-x64_bin.rpm')
		print("Instalacao do Java Completa!")
		os.system('cp java_home.sh /etc/profile.d/')
		os.system('source ~/.bash_profile')	

def zeppelin_xml_update():
	tree = ET.parse('/opt/zeppelin/conf/zeppelin-site.xml.template')
	root = tree.getroot()
	ip = root[0][1]
	ip.text = '192.168.56.10'
	tree.write('/opt/zeppelin/conf/zeppelin-site.xml')

def zeppelin_install():
	if os.path.exists('zeppelin-0.10.1-bin-all.tgz') :
		print("Download do Zeppelin ja existe")
	else :
		os.system('wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz')
		print("Download do Zeppelin Completo!")
		tar = tarfile.open('zeppelin-0.10.1-bin-all.tgz')
		tar.extractall()
		tar.close()
		os.system('mv zeppelin-0.10.1-bin-all/ /opt/zeppelin')
		os.system('adduser -d /opt/zeppelin -s /sbin/nologin zeppelin')
		os.system('chown -R zeppelin:zeppelin /opt/zeppelin')
		os.system('cp systemd/zeppelin.service /etc/systemd/system/')
		zeppelin_xml_update()

# Verifica se o wget existe na vm, se nao instala com yum
# Realiza o download do java no site da oracle e prosegue com a instalacao 
if os.system('wget') != 0 :
	os.system('yum -y install wget')
	java_install()
	zeppelin_install()
else :
	java_install()
	zeppelin_install()




