# Ansible Brownbag

## Getting ready

Make sure you have:

- python
- pip
- virtualenv
- vagrant

Straight-away, run:

```
vagrant up
```

Then in another terminal, run:

```
virtualenv .
source bin/activate
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

## 
