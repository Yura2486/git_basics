
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __repr__(self):
        return f'{self.name}'

class Worker(Person):
    def __init__(self, name, id, position):
        super().__init__(name)
        self.id = id
        self.position = position

    def __repr__(self):
        return f'{self.get_name()} the {self.position}'

class Company:
    def __init__(self, name):
        self.name = name
        self.workers = []

    def add_worker(self, name, position):
        worker = Worker(name, len(self.workers), position)
        self.workers.append(worker)

    def del_worker(self, id):
        for ind in self.workers:
            if ind.id == id:
                self.workers.remove()
                return

    def get_workers(self):
        return self.workers

    def __repr__(self):
        return f'{self.name} {len(self.workers)}'

if __name__ == '__main__':
    company = Company("John & co.")

    company.add_worker("Adam", "Programmer")
    company.add_worker("John", "HR")
    company.add_worker("Will", "Engineer")

    print(company)
    workers = company.get_workers()

    print('worker list:')
    for mnb in workers:
        print(f'\t{mnb}')

