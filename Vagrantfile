Vagrant.configure("2") do |config|
  config.vm.define :luke do |luke|
    luke.vm.box = "precise32"
    luke.vm.network :forwarded_port, guest: 22, host: 3001
  end

  config.vm.define :han do |han|
    han.vm.box = "precise32"
    han.vm.network :forwarded_port, guest: 22, host: 3002
  end

  config.vm.define :leia do |leia|
    leia.vm.box = "precise32"
    leia.vm.network :forwarded_port, guest: 22, host: 3003
  end
end
