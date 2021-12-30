# python
Programas python


Para estudar:

[Ontem 16:05] Josue Telles Correa
https://fluentvalidation.net/FluentValidation • HomeA popular .NET validation library for building strongly-typed validation rules.
FluentValidation • Home
A popular .NET validation library for building strongly-typed validation rules.

[Ontem 16:09] Josue Telles Correa
https://israelaece.com/2017/04/06/introducao-ao-mediatr/
Introdução ao MediatR
Ao trabalhar com CQRS, o primeiro passo é criar a infraestrutura de mensagens para suportar os comandos, consultas e eventos que a aplicação tenha. Somente a partir daí é que passamos a nos preocup…

[Ontem 16:31] Josue Telles Correa
//HEXAGONAL + EVENT DRIVEN

[Ontem 16:37] Josue Telles Correa
//SAGAS PATTERN

[Ontem 16:46] Josue Telles Correa
https://microservices.io/patterns/data/saga.html
Microservices Pattern: Sagas
Implement transactions using a saga, which is sequence of local transactions

[Ontem 16:48] Josue Telles Correa
https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/integration-event-based-microservice-communications
Implementing event-based communication between microservices (integration events)
.NET Microservices Architecture for Containerized .NET Applications | Understand integration events to implement event-based communication between microservices.

[Ontem 16:48] Josue Telles Correa
https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Event Sourcing pattern - Cloud Design Patterns
Use an append-only store to record the full series of events that describe actions taken on data in a domain.

[Ontem 16:48] Josue Telles Correa
http://www.andreavallotti.tech/en/2018/01/event-sourcing-and-cqrs-in-c/
Event Sourcing and CQRS in C#
As promised in my previous post, in this article I examine practical aspects related to DDD and, in particular to CQRS and Event Sourcing patterns.
The main goal of my experiment is to implement an...

[Ontem 16:48] Josue Telles Correa
https://martinfowler.com/eaaDev/EventSourcing.html
Event Sourcing
Capture all changes to an application state as a sequence of events.


Mega sena:

import random
from builtins import range

print('Quantas deszenas?')
dezenas = range(int(input()))

print('Quantos jogos?')
qtd = int(input())

sortArray = []
for item0 in range(qtd):
    for idx, item in enumerate(dezenas):
        r1 = random.randint(1, 60)
        sortArray.append(r1)
    sortArray.sort()
    for idx, n in enumerate(sortArray):
        if idx < len(dezenas) - 1:
            print(str(n).zfill(2), end='-')
        else:
            print(str(n).zfill(2))
    sortArray = []
