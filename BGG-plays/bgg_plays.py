#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import datetime
import sys

from boardgamegeek.api import BoardGameGeek

query = sys.argv[1]


def main(query):

    args = query.split(' ')

    username = args[0]
    mindate = datetime.strptime(args[1], '%Y-%m-%d')
    maxdate = datetime.strptime(args[2], '%Y-%m-%d')

    bgg = BoardGameGeek()
    plays = bgg.plays(name=username, min_date=mindate, max_date=maxdate)

    final = []
    games = defaultdict(int)

    for play in plays:
        games[play.game_name] += 1

    for game in sorted(games):
        if games[game] > 1:
            final.append(u'{game} ({cnt})'.format(game=game, cnt=games[game]))
        else:
            final.append(u'{game}'.format(game=game))

    try:
        final = [f.encode('utf8') for f in final]
        print ', '.join(final)
    except Exception:
        print final


if __name__ == '__main__':
    main(query)
