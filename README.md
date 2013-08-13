# Ansible Star Wars brownbag

## Getting ready

**Quick, quick, quick we need to save time!**

Make sure you have:

- ```python```
- ```pip```
- ```virtualenv```
- ```vagrant```

I'll pass around the precise64.box somehow

Spin up the boxes straight-away (need to save time!), run:

```
vagrant up
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
10.0.0.2 han
10.0.0.3 luke
10.0.0.4 leia
```

Now run this to check that everything is fine:
```
ansible all -m ping -i hosts
```

## Playing with ansible

### The mongodb example

To be continued...
