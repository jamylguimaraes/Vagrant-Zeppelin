#!/usr/bin/env python2
import os

def java_install():
	os.system('wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.rpm')
	print("Download do Java Completo!")
	os.system('yum -y localinstall jdk-17_linux-x64_bin.rpm')
	print("Instalacao do Java Completa!")
	os.system('cp java_home.sh /etc/profile.d/')
	os.system('source ~/.bash_profile')	

# Verifica se o wget existe na vm, se nao instala com yum
# Realiza o download do java no site da oracle e prosegue com a instalacao 
if os.system('wget') != 0 :
	os.system('yum -y install wget')
	java_install()
else :
	java_install()




