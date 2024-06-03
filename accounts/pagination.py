import urllib

from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.next_page_number()
        if page_number == 1:
            return None

        # Extract token from headers
        token = self.request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        # Construct curl command with token in headers
        curl_command = f'curl -X GET "{url}&page={page_number}" -H "Authorization: Bearer {token}"'
        # Encode the curl command string for URL
        encoded_curl_command = urllib.parse.quote(curl_command)

        next_url = f'{url}&page={page_number}&curl_command={encoded_curl_command}'
        return next_url
