#!/usr/bin/env python2
import os
import tarfile

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

def zeppelin_install():
	if os.path.exists('zeppelin-0.10.1-bin-all.tgz') :
		print("Download do Zeppelin ja existe")
	else :
		os.system('wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz')
		print("Download do Zeppelin Completo!")
		tar = tarfile.open('zeppelin-0.10.1-bin-all.tgz')
		tar.extractall()
		tar.close()

# Verifica se o wget existe na vm, se nao instala com yum
# Realiza o download do java no site da oracle e prosegue com a instalacao 
if os.system('wget') != 0 :
	os.system('yum -y install wget')
	java_install()
	zeppelin_install()
else :
	java_install()
	zeppelin_install()




