import scrapy
from faculty_scraper.items import FacultyItem

class FacultySpider(scrapy.Spider):
    name = "faculty"
    allowed_domains = ["daiict.ac.in"]
    
    start_urls = [
        "https://www.daiict.ac.in/faculty",
        "https://www.daiict.ac.in/adjunct-faculty",
        "https://www.daiict.ac.in/adjunct-faculty-international",
        "https://www.daiict.ac.in/distinguished-professor",
        "https://www.daiict.ac.in/professor-practice"
    ]

    def clean_list(self, values):
        """Helper to remove empty strings and whitespace from list of strings"""
        return [v.strip() for v in values if v and v.strip()]

    def parse(self, response):
        """
        Parse the main faculty listing pages
        """
        # Select the list items containing faculty info
        faculty_cards = response.css("div.facultyInformation ul li")

        for faculty in faculty_cards:
            # Combined selector to handle different class name variations on the site
            profile_link = faculty.css(
                "div.personalDetails h3 a::attr(href), "
                "div.personalDetail h3 a::attr(href), "
                "div.personalsDetails h3 a::attr(href)"
            ).get()

            name = faculty.css(
                "div.personalDetails h3 a::text, "
                "div.personalDetail h3 a::text, "
                "div.personalsDetails h3 a::text"
            ).get()

            if profile_link:
                yield response.follow(
                    profile_link,
                    callback=self.parse_faculty_profile,
                    meta={
                        "name": name.strip() if name else "Unknown", 
                        "profile_url": response.urljoin(profile_link)
                    }
                )

    def parse_faculty_profile(self, response):
        """
        Parse individual faculty profile page and ensure all data are strings for SQLite
        """
        item = FacultyItem()

        item["name"] = response.meta.get("name")
        item["profile_url"] = response.meta.get("profile_url")

        # -------- LEFT SIDE --------
        # Education: Join multiple degrees with a pipe |
        edu_raw = response.css(
            "div.contact-box-p.pb0.EducationIcon div.detail div.field-content div.field.field--name-field-faculty-name.field--type-string.field--label-hidden.field__item::text"
        ).getall()
        item["education"] = " | ".join(self.clean_list(edu_raw))

        item["email"] = response.css(
            "div.contact-box-p.emailIcon div.field__item::text"
        ).get()

        item["phone"] = response.css(
            "div.contact-box-p.pb0.mobileIcon div.detail div.field-content div.field.field--name-field-contact-no.field--type-string.field--label-hidden.field__item::text"
        ).get()

        item["address"] = response.css(
            "div.contact-box-p.pb0.addressIcon div.detail div.field-content div.field.field--name-field-address.field--type-string-long.field--label-hidden.field__item::text"
        ).get()

        item['faculty_web'] = response.css(
            "div.contact-box-p.facultyweb a::attr(href)"
        ).get()

        # -------- RIGHT SIDE --------
        # Biography: Join paragraphs with newlines
        bio_raw = response.css("div.about p::text").getall()
        item["biography"] = "\n".join(self.clean_list(bio_raw))

        # Specialization: Join with commas
        spec_raw = response.xpath("//div[@class='work-exp margin-bottom-20']//text()").getall()
        item["specialization"] = ", ".join(self.clean_list(spec_raw))

        # Teaching: Join with newlines
        teach_raw = response.xpath(
            "//div[contains(@class,'work-exp') "
            "and not(contains(@class,'margin-bottom-20')) "
            "and not(contains(@class,'work-exp1'))]"
            "//text()"
        ).getall()
        item["teaching"] = "\n".join(self.clean_list(teach_raw))

        # Publications: Processes list into a single string with newlines
        pub_list = [
            " ".join(self.clean_list(li.xpath(".//text()").getall()))
            for li in response.xpath(
                "//div[contains(@class,'education') and contains(@class,'overflowContent')]//ul/li | "
                "//div[contains(@class,'education') and contains(@class,'overflowContent')]//ol/li"
            )
        ]
        item["publications"] = "\n".join(self.clean_list(pub_list))

        # Research: Join with newlines
        res_raw = response.xpath("//div[@class='work-exp1']//text()").getall()
        item["research"] = "\n".join(self.clean_list(res_raw))

        yield item