from django.shortcuts import render
from django.utils import timezone
from .models import Team, Fixture, TopScorer


# ---------------- HOME ----------------
def home(request):
    latest_matches = Fixture.objects.all().order_by('-date')[:5]
    top_players = TopScorer.objects.all().order_by('-goals')[:5]

    return render(request, 'home.html', {
        'matches': latest_matches,
        'players': top_players
    })


# ---------------- TEAMS ----------------
def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})


# ---------------- FIXTURES ----------------
def fixtures(request):
    matches = Fixture.objects.all()

    for match in matches:
        if match.status == 'LI':
            now = timezone.now()
            diff = now - match.date
            minutes = int(diff.total_seconds() // 60)
            match.live_time = f"{max(minutes, 0)}'"

        elif match.status == 'FT':
            match.live_time = "FT"
        else:
            match.live_time = "Upcoming"

    return render(request, 'fixtures.html', {'matches': matches})


# ---------------- TABLE ----------------
def table(request):
    teams = Team.objects.all()

    table_data = []

    for team in teams:
        played = wins = draws = losses = points = 0
        goals_for = goals_against = 0

        matches = Fixture.objects.filter(home_team=team) | Fixture.objects.filter(away_team=team)

        for match in matches:
            played += 1

            if match.home_team == team:
                goals_for += match.home_score
                goals_against += match.away_score

                if match.home_score > match.away_score:
                    wins += 1
                    points += 3
                elif match.home_score == match.away_score:
                    draws += 1
                    points += 1
                else:
                    losses += 1
            else:
                goals_for += match.away_score
                goals_against += match.home_score

                if match.away_score > match.home_score:
                    wins += 1
                    points += 3
                elif match.away_score == match.home_score:
                    draws += 1
                    points += 1
                else:
                    losses += 1

        gd = goals_for - goals_against

        table_data.append({
            'team': team,
            'played': played,
            'wins': wins,
            'draws': draws,
            'losses': losses,
            'gf': goals_for,
            'ga': goals_against,
            'gd': gd,
            'points': points
        })

    table_data = sorted(table_data, key=lambda x: (x['points'], x['gd']), reverse=True)

    return render(request, 'table.html', {'table': table_data})


# ---------------- TOP SCORERS ----------------
def topscorers(request):
    players = TopScorer.objects.all().order_by('-goals')
    return render(request, 'topscorers.html', {'players': players})