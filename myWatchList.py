import json
import os.path

class My_Drama_List:
    myWatch_list = {}
    def __init__(self):
        self.load() 
    def add(self,dName,dEp):
        q = 0
        if dName in self.myWatch_list:
            v = self.myWatch_list[dName]
            q = v + dEp
        else :
            q = dEp
        self.myWatch_list[dName] = q
        print(f'Added! Drama: {dName};  Episodes: {self.myWatch_list[dName]} ')
    def remove(self,dName,dEp):
        q = 0
        if dName in self.myWatch_list:
            v = self.myWatch_list[dName]
            q = v - dEp
        if q< 0:
            q = 0
        self.myWatch_list[dName] = q
        print(f'Remove! Drama: {dName};  Episodes: {self.myWatch_list[dName]} ')
    def display(self):
        print('-'*20)   
        for dName , value in self.myWatch_list.items():    
            print(f' Drama: {dName} ; Episodes: {value} ')
        print('-'*20)
    def save(self):
        print('Saving My Drama List..')
        with open('My_Drama_List.txt', 'w') as f:
            json.dump(self.myWatch_list,f)
        print('Saved!')
    def load(self):
        print('Loading My Drama List..')
        if not os.path.exists('My_Drama_List.txt'):
            print('Skipping , nothing to load..')
            return
        with open('My_Drama_List.txt', 'r') as f:
            self.myWatch_list = json.load(f)
        print('Loaded!')
        
def main():
    mdl = My_Drama_List()
    while True:
        cmd = input('Action: add, remove, list, save, exit: ')
        action = cmd.lower()
        if action == 'exit':
            break
        if action == 'add' or action == 'remove':
            DN = input('Enter Drama name: ')
            dName = DN.upper()
            dEp = int(input('Enter episode number: '))
            if action == 'add':
                mdl.add(dName,dEp)
            if action == 'remove':
                mdl.remove(dName,dEp)
        if action == 'list':
            mdl.display()
        if action == 'save':
            mdl.save()
    mdl.save()

if __name__ == "__main__":
    main()
