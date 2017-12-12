from django.contrib import admin

from .models import Game, Move


#class GameAdmin(admin.ModelAdmin):
#   list_display = ['first_player', 'second_player', 'status']
#admin.site.register(Game, GameAdmin)
# or...
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_player', 'second_player', 'status')
  list_editable = ('status',)


admin.site.register(Move)
