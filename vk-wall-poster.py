# -*- coding: utf-8 -*-
import requests

vk_key = '39cf5a71b460238d50ece941a7a8671b48e0e285c6l72e9cab1ad5ece479cd5b80a87q02d2b35ce9fd2b2'  # токен
group_id = 777777  # group/public vk ID


def vk_photo_post(filename, text):
    url = 'https://api.vk.com/method/photos.getWallUploadServer?group_id=%d&v=5.28&access_token=%s' % (
        group_id, vk_key)
    upload_url = requests.get(url).json()['response']['upload_url']
    files = {'file1': open(filename, 'rb')}
    r = requests.post(upload_url, files=files).json()
    url = 'https://api.vk.com/method/photos.saveWallPhoto?group_id=%s&server=%s&photo=%s&hash=%s&v=5.28&access_token=%s' % (
        group_id, r['server'], r['photo'], r['hash'], vk_key)
    r = requests.get(url).json()['response'][0]
    atts = 'photo%s_%s' % (r['owner_id'], r['id'])
    url = 'https://api.vk.com/method/wall.post?owner_id=%s&from_group=1&message=%s&attachments=%s&v=5.28&access_token=%s' % (
        -group_id, text, atts, vk_key)
    return requests.get(url).json()


def main():
	vk_photo_post('test.jpg', 'Text just for test')


if __name__ == '__main__':
    main()
