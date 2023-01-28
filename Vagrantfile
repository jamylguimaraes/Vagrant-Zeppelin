# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.disksize.size = '50GB'
  config.vm.box = "centos/7" 
  config.vm.network "private_network", ip: "192.168.56.10"  

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 1
  end

  # SSH Config
  config.ssh.forward_agent = true


  # Network Config	
  #config.vm.network "forwarded_port", guest: 8080, host: 9000, auto_correct: true

  # Upload user's ssh key into box
  ssh_key_path = "~/.ssh/"
  file_dir = "files/"
  config.vm.provision "shell", inline: "mkdir -p /home/vagrant/.ssh"
  config.vm.provision "shell", inline: "mkdir -p /home/vagrant/files"
  config.vm.provision "shell", inline: "sudo chown vagrant:vagrant /home/vagrant/files"
  config.vm.provision "file", source: "#{ ssh_key_path + 'id_rsa' }", destination: "/home/vagrant/.ssh/id_rsa"
  config.vm.provision "file", source: "#{ ssh_key_path + 'id_rsa.pub' }", destination: "/home/vagrant/.ssh/id_rsa.pub"
  config.vm.provision "file", source: "#{ file_dir + 'lab1.py' }", destination: "/home/vagrant/files/"
  config.vm.provision "file", source: "#{ file_dir + 'java_home.sh' }", destination: "/home/vagrant/files/"

end
