from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    # 🔥 ADD THESE FIELDS
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def goal_difference(self):
        return self.goals_for - self.goals_against

    def __str__(self):
        return self.name
class Fixture(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    date = models.DateTimeField()

    STATUS_CHOICES = [
        ('UP', 'Upcoming'),
        ('LI', 'Live'),
        ('FT', 'Full Time'),
    ]

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='UP')

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
class TopScorer(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.team})"
@receiver(post_save, sender=Fixture)
def update_team_stats(sender, instance, **kwargs):

    home = instance.home_team
    away = instance.away_team

    # reset stats first (important to avoid duplication)
    for team in [home, away]:
        team.played = 0
        team.won = 0
        team.drawn = 0
        team.lost = 0
        team.goals_for = 0
        team.goals_against = 0
        team.points = 0
        team.save()

    # recalculate ALL matches
    all_matches = Fixture.objects.all()

    for match in all_matches:
        home = match.home_team
        away = match.away_team

        home.played += 1
        away.played += 1

        home.goals_for += match.home_score
        home.goals_against += match.away_score

        away.goals_for += match.away_score
        away.goals_against += match.home_score

        if match.home_score > match.away_score:
            home.won += 1
            home.points += 3
            away.lost += 1

        elif match.home_score < match.away_score:
            away.won += 1
            away.points += 3
            home.lost += 1

        else:
            home.drawn += 1
            away.drawn += 1
            home.points += 1
            away.points += 1

        home.save()
        away.save()