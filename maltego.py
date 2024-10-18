from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_TYPES

class SocialMediaTransform(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request, response):
        target_email = request.Value
        # Example transform logic to find social media profiles linked to an email
        social_profiles = find_social_profiles(target_email)  # Custom logic
        for profile in social_profiles:
            response.addEntity('maltego.SocialMedia', profile)
