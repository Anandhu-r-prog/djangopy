from django.contrib import admin
from .models import Event, EventBooking, LoginRecord, UserMessage, SignupData, UserSuggestion, BeachWeddingBooking

admin.site.register(BeachWeddingBooking)
admin.site.register(Event)
admin.site.register(LoginRecord)
admin.site.register(UserMessage)
admin.site.register(SignupData)
admin.site.register(EventBooking)  
admin.site.register(UserSuggestion)  # Assuming userSuggestion is defined in models.py
 


