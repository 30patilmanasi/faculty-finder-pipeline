# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class FacultyItem(scrapy.Item):
    # These MUST match the keys used in your spider exactly
    name = scrapy.Field()
    profile_url = scrapy.Field()
    education = scrapy.Field()  # This was missing!
    email = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    faculty_web = scrapy.Field()
    biography = scrapy.Field()
    specialization = scrapy.Field()
    teaching = scrapy.Field()
    publications = scrapy.Field()
    research = scrapy.Field()