Vagrant.configure("2") do |config|
  config.vm.define :luke do |luke|
    luke.vm.box = "precise64"
    luke.vm.network :private_network, ip: "10.0.0.2"
  end

  config.vm.define :han do |han|
    han.vm.box = "precise64"
    han.vm.network :private_network, ip: "10.0.0.3"
  end

  config.vm.define :leia do |leia|
    leia.vm.box = "precise64"
    leia.vm.network :private_network, ip: "10.0.0.4"
  end
end
