#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import random
import string
import click
from faker import Faker

fake = Faker()

class PortSwiggerTrial:
    def __init__(self, email):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://portswigger.net/burp/pro/trial',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'DNT': '1',
            'Sec-GPC': '1',
            'Priority': 'u=1',
            'TE': 'trailers'
        }
        self.email = email
        self.name = self.generate_fake_name()
        self.request_verification_token = None
        self.order_id = None

    def generate_fake_name(self):
        name = fake.name()
        return name

    def extract_token(self, response_text):
        soup = BeautifulSoup(response_text, 'html.parser')
        token_element = soup.find('input', {'id': 'RequestVerificationToken'})
        if not token_element:
            raise ValueError('RequestVerificationToken not found')
        return token_element['value']

    def extract_order_id(self, response_text):
        soup = BeautifulSoup(response_text, 'html.parser')
        order_id_element = soup.find('input', {'id': 'OrderId'})
        if not order_id_element:
            raise ValueError('OrderId not found')
        return order_id_element['value']

    def get_initial_token(self):
        response = self.session.get('https://portswigger.net/burp/pro/trial', headers=self.headers)
        self.request_verification_token = self.extract_token(response.text)
        print(f"RequestVerificationToken:\n{self.request_verification_token}")

    def first_post_request(self):
        response = self.session.post(
            'https://portswigger.net/burp/pro/trial',
            headers=self.headers,
            data={
                'Email': self.email,
                'RequestVerificationToken': self.request_verification_token
            }
        )
        self.order_id = self.extract_order_id(response.text)
        print("OrderId  =>", self.order_id)
        print("Name     =>", self.name)
        print("Emial    =>", self.email)

    def second_post_request(self):
        response = self.session.post(
            'https://portswigger.net/burp/pro/trial/welcome',
            headers=self.headers,
            data={
                'Name': self.name,
                'RequestVerificationToken': self.request_verification_token,
                'OrderId': self.order_id
            }
        )

    def third_post_request(self):
        objective = f'My name is {self.name} and I have been conducting security assessments and vulnerability analysis within various domains, and I believe that Burp Suite Pro would greatly enhance my capabilities in identifying and mitigating potential security threats. Its advanced features, such as its robust scanner and comprehensive toolset, align perfectly with the requirements of my research projects.'
        response = self.session.post(
            'https://portswigger.net/burp/pro/trial/objectives',
            headers=self.headers,
            data={
                'Objective': objective,
                'RequestVerificationToken': self.request_verification_token,
                'OrderId': self.order_id
            }
        )
        print(objective)

    def fourth_post_request(self):
        role = 'Practitioner'
        app_sec_experience = 'Intermediate'
        has_used_burp = 'Yes'
        response = self.session.post(
            'https://portswigger.net/burp/pro/trial/about-you',
            headers=self.headers,
            data={
                'Role': role,
                'AppSecExperience': app_sec_experience,
                'HasUsedBurp': has_used_burp,
                'RequestVerificationToken': self.request_verification_token,
                'OrderId': self.order_id
            }
        )

    def run(self):
        self.get_initial_token()
        self.first_post_request()
        self.second_post_request()
        self.third_post_request()
        self.fourth_post_request()

@click.command()
@click.option('--email', '-email', '-e', prompt='Enter your email', help='The email address to use for the trial. MUST BE WORK OR EDU EMAIL')
def main(email):
    trial = PortSwiggerTrial(email)
    trial.run()

if __name__ == "__main__":
    main()
