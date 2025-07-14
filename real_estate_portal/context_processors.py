from django.conf import settings

def google_maps_config(request):
    """
    Context processor to add Google Maps configuration to all templates.
    This makes Google Maps API key and Map ID available in all templates.
    """
    return {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'google_maps_map_id': settings.GOOGLE_MAPS_MAP_ID,
    }
