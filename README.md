# Ansible Brownbag

## Getting ready

**Quick, quick, quick we need to save time!**

Make sure you have:

- python
- pip
- virtualenv
- vagrant

I'll pass around the precise64.box somehow

Straight-away (need to save time!), run:

```
vagrant box add precise64 precise64.box # Add the precise64 vm image to vagrant
vagrant up # Spin up the three boxes
```

Then in another terminal, run:

```
# Create a python virtualenv to install ansible into (a bit like virtualenv)
virtualenv .
# Enter the virtualenv
source bin/activate
# Install ansible (and it's dependancies)
pip install ansible
```

Put this in your ```/etc/hosts``` file:

```
127.0.0.1 han
127.0.0.1 luke
127.0.0.1 leia
```

Now run this to check that everything is fine:
```
ansible all -m ping -i hosts
```

## Playing with ansible

To be continued...
