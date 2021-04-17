import requests

_API_HOST = 'http://localhost:8080'


def run():

    quit = False
    while not quit:
        try:
            line = input('trellish> ')
            if line:
                inputs = line.strip().lower().split()
                command = inputs[0]
                if command == 'exit':
                    quit = True
                else:
                    process_command(command, inputs[1:])
        except EOFError:
            quit = True
            print()
        except Exception as e:
            print(f'ERROR - {e}')


def process_command(comm, args):
    
    if comm == 'help':
        print('Commands:')
        print(' show-lists')
        print(' show-list <ID>')
        print(' show-cards <ID>')
        print(' show-card <ID> <ID>')
        print(' delete-list <ID>')
        print(' delete-card <ID>')
        print(' new-list')
        print(' new-card <ID>')
        print(' help')
        print(' exit')
        
    elif comm == 'show-lists':
        result = requests.get(f'{_API_HOST}/lists').json()
        print('----------------------------------------')
        for r in result['lists']:
            print(f"{r['id']}: {r['name']}")
        print('----------------------------------------')
        
    elif comm == 'new-list':
        name = input('Name: ')
        body = {'name': name}
        result = requests.post(f'{_API_HOST}/lists', json=body).json()
        print(f"Created with ID {result['id']}")
        
    elif comm == 'show-list':
        id = args[0]
        result = requests.get(f'{_API_HOST}/lists/{id}').json()
        print('----------------------------------------')
        for k in result:
            print(f'{k}: {result[k]}')
        print('----------------------------------------')
        
    elif comm == 'delete-list':
        id = args[0]
        result = requests.delete(f'{_API_HOST}/lists/{id}').text
        print(result)
        
    elif comm == 'show-cards':
        list_id = args[0]
        result = requests.get(f'{_API_HOST}/lists/{list_id}/cards').json()
        print('----------------------------------------')
        for r in result['cards']:
            print(f"{r['id']}: {r['name']}")
        print('----------------------------------------')
        
    elif comm == 'new-card':
        list_id = args[0]
        name = input('Name: ')
        descr = input('Description: ')
        priority = input('Priority: ')
        due_date = input('Due date: ')
        body = {'name': name,
                'description': descr,
                'priority': priority,
                'due_date': due_date}
        result = requests.post(f'{_API_HOST}/lists/{list_id}/cards', json=body).json()
        print(f"Created with ID {result['id']}")
        
    elif comm == 'show-card':
        list_id = args[0]
        card_id = args[1]
        result = requests.get(f'{_API_HOST}/lists/{list_id}/cards/{card_id}').json()
        print('----------------------------------------')
        for k in result:
            print(f'{k}: {result[k]}')
        print('----------------------------------------')
        
    elif comm == 'delete-card':
        list_id = args[0]
        card_id = args[1]
        result = requests.delete(f'{_API_HOST}/lists/{list_id}/cards/{card_id}').text
        print(result)
        
    else:
        print('Unknown command')

        
if __name__ == '__main__':
    run()
