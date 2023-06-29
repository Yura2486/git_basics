def fortune(C):
    match C.rank:
        case cards.RankEnum.SIX:
            return 'Гармонійні стосунки з близькими людьми.'
        case cards.RankEnum.SEVEN:
            return 'Слухайте свою інтуїцію.'
        case cards.RankEnum.EIGHT:
            return 'Відносини різко зміняться.'
        case cards.RankEnum.NINE:
            return 'Успіх чи шлюб.'
        case cards.RankEnum.TEN:
            return 'Отримання бажаного.'
        case cards.RankEnum.JACK:
            return 'Молодий чоловік.'
        case cards.RankEnum.QUEEN:
            return 'Доросла жінка.'
        case cards.RankEnum.KING:
            return 'Дорослий чоловік.'
        case cards.RankEnum.ACE:
            return 'Нові відносини, закоханість.'

def getcards(D, N):
    l = list()
    for i in range(1, N+1):
        c = D.get_top()
        l.append(c)
    return l

def main(args):
    d = cards.Deck()
    d.shuffle()
    if len(args) <= 1:
        print("error: set number")
        return
    if int(args[1]) <= 0 or int(args[1]) > len(d):
        print(f'error: 1 <= N <= {len(d)}')
        return

    c = getcards(d, int(args[1]));
    for l in c:
        print(f'{l} = {fortune(l)}')
    return

if __name__ == '__main__':
    import sys
    import random
    import argparse
    import cards
    sys.exit(main(sys.argv))
