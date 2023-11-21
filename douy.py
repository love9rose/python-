import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support import expected_conditions as EC  # 等待所有标签加载完毕
from selenium.webdriver.support.wait import WebDriverWait
import json
from lxml import etree
import json
from jsonpath import jsonpath
class Douy():
    def __init__(self):
        # self.url='https://www.douyin.com/aweme/v1/web/general/search/single/'
        self.url='https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=0&publish_time=0&keyword=%E5%BE%90%E5%B7%9E%E4%B9%A1%E6%9D%91%E6%B8%B8&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=15&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=2048&screen_height=1152&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7303052201974646283&msToken=NR9qoR2IjiArDIzxMHhw0i4lpWypTi9no08TqTMU5uu18MXpTqzao0aHV31vDSGsPzlp0mZCQtzXNJN9NyZLOhwZG1ByKZYj8TtMjMXgcWSuan9G1-hdrQdiQ6aD&X-Bogus=DFSzswVOupzANtOstmelEKXAIQ59'
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Cookie':'ttwid=1%7CHziCx9X9n-KpTvUTUKU4pHUZQ2VD2zo6h2Da50glfx4%7C1700374359%7C45d'
                     '2b2151c280d863330a04a1a1eea1cff6138d4fdf6a5bb7360c27c42969c95; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1152%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; passport_csrf_token=9861c37c5bd28ff082a5d76e512cf261; passport_csrf_token_default=9861c37c5bd28ff082a5d76e512cf261; strategyABtestKey=%221700374361.27%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.6%7D; s_v_web_id=verify_lp52zqiv_ulQ4ogpV_iEq5_4xYa_AVcZ_jJfcUULWszV1; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; ttcid=2c7d6571ebbc47c89e8fdb39eb49ca0b11; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1700993009529%2C%22type%22%3A1%7D; xgplayer_user_id=309996907726; download_guide=%223%2F20231119%2F0%22; pwa2=%220%7C0%7C3%7C0%22; __ac_signature=_02B4Z6wo00f01OMVdxAAAIDBgB-3ehNeA3DjNXOAAF2ihC6Ry4LkFoDrSc6UyflNNBX28UhvCLXmbOMryVIRZ41sESd474.J6H21KXGTo10zre4g0Je'
                     'tUmbDgKfLgNSyC5MxSl6fPEzEW9WP1d; SEARCH_RESULT_LIST_TYPE=%22single%22; n_mh=fBBs00AwjjgouQPrOre_5crOchZOT9l6wRGKcfZn0Mw; publish_badge_show_info=%220%2C0%2C0%2C1700391228788%22; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; csrf_session_id=b7fed091e83f24677d9b67f17a3b0873; store-region=cn-gx; store-region-src=uid; passport_assist_user=CkFJDp-sb6jwJAPJt2j77npQFrAIEnd8pSjdKcizlSPCZ-cQPKxJfZ1bgbGQrLMqwt9myolTZMIV1lABRVOxMzxrXRpKCjwg9EM0lN3kBSDQVzeQNEH1wlpqeJScHkMtiN6iXecZhSHs5M3VkmXEsFgJwW4HKLvoxd5xE-y5L7L-xxUQv9rBDRiJr9ZUIAEiAQM3Czo2; sso_uid_tt=64778b533c98aeae9b2948e051cd6c0a; sso_uid_tt_ss=64778b533c98aeae9b2948e051cd6c0a; toutiao_sso_user=1738bf80bed0c1839a10e0d2d99f6655; toutiao_sso_user_ss=1738bf80bed0c1839a10e0d2d99f6655; sid_ucp_sso_v1=1.0.0-KGQ4NTk0ZmU2MmI3Mjc3M2U1MmM4NzRmODhmNTM0MzI3MWM4ZTQzYTEKHwiX1tCm2YzoBBCF3ueqBhjvMSAMMIal5YIGOAZA9AcaAmhsIiAxNzM4YmY4MGJlZDBjMTgzOWExMGUwZDJkOTlmNjY1NQ; ssid_ucp_sso_v1=1.0.0-KGQ4NTk0ZmU2MmI3Mjc3M2U1MmM4NzRmODhmNTM0MzI3MWM4ZTQzYTEKHwiX1tCm2YzoBBCF3ueqBhjvMSAMMIal5YIGOAZA9AcaAmhsIiAxNzM4YmY4MGJlZDBjMTgzOWExMGUwZDJkOTlmNjY1NQ; passport_auth_status=afe9a254e461cebcd3a3b58e132330a2%2C696044ecae32798dc0b5553b05ef52c7; passport_auth_status_ss=afe9a254e461cebcd3a3b58e132330a2%2C696044ecae32798dc0b5553b05'
                     'ef52c7; uid_tt=c0ded422c1be445d6c0526696da23bfc; uid_tt_ss=c0ded422c1be445d6c0526696da23bfc; sid_tt=eb506656156f6443ef003266cfb92fdb; sessionid=eb506656156f6443ef003266cfb92fdb; sessionid_ss=eb506656156f6443ef003266cfb92fdb; _bd_ticket_crypt_cookie=0da1b8bcac61a8b0cde68191598ac6d5; sid_guard=eb506656156f6443ef003266cfb92fdb%7C1700393665%7C5183047%7CThu%2C+18-Jan-2024+11%3A18%3A32+GMT; sid_ucp_v1=1.0.0-KDBjNGRjNmUwMzNmM2ZjNDE4MDc5NzZmN2M3NDMyODdmNmM5MDllNzYKGwiX1tCm2YzoBBDB5eeqBhjvMSAMOAZA9AdIBBoCbGYiIGViNTA2NjU2MTU2ZjY0NDNlZjAwMzI2NmNmYjkyZmRi; ssid_ucp_v1=1.0.0-KDBjNGRjNmUwMzNmM2ZjNDE4MDc5NzZmN2M3NDMyODdmNmM5MDllNzYKGwiX1tCm2YzoBBDB5eeqBhjvMSAMOAZA9AdIBBoCbGYiIGViNTA2NjU2MTU2ZjY0NDNlZjAwMzI2NmNmYjkyZmRi; LOGIN_STATUS=1; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA_efwusVPpPYQNOJmSX398gFOJpmCu39vVLyM3PgfdlwKIeAXL7ajYsTrkb7EdC9H%2F1700409600000%2F0%2F1700393908704%2F0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=06559f593009ce168724e; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQt'
                     'Z3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT3A1U3NwaWxhQ3NMeWZ2Tll6dFFGS24vcjNxeFJaVzBEdWZKNHg3WTFuSkg0VGtuaFVWQXFsdG5meWNnM0NQTnM4MUJYQmJRV2JXdGlMTVc1cTcxWVk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=e5e254c9cdc9206c7084db800e6686fc8eb4db78d4bfe527214b83e8a52d30f5e0ca1206066c7c65c132ba1dcc2038b4; tt_scid=8vsQmbPuvWVkoZaXdpph4eNyi.lzI4TeUDQvh8M2U-nLUc1xHlb6A1oMXr0AQf6s8696; msToken=yx49FQ6DxRnzc88VdSW6bAN7GBPh49nr74koH6azRWmKJWDBkmklUUyLLKnv5hwVcmamAclWxKSmxYlOoH0kmyAFDfdMsrNQULIg_sr1MdDHFXGFgtQ=; msToken=H8iwRx6_yRfVxDkz6Yd5i7XiFw2tWZa_MNT5EydTSFwLgUlhL-rxfRVJwtrekdMLvgtIlXV_6dK0fvEqbS8OPYxSCRiR_foZN42lP7CrP97fxxyRjNI=; passport_fe_beating_status=false; home_can_add_dy_2_desktop=%220%22; IsDouyinActive=true',
            'Referer':'https://www.douyin.com/search/%E5%BE%90%E5%B7%9E%E4%B9%A1%E6%9D%91%E6%B8%B8?aid=92233653-5f18-4a4d-9e73-ce23e2f4d5a7&publish_time=0&sort_type=0&source=normal_search&type=general'
        }
        self.params={
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'search_channel': 'aweme_general',
            'sort_type': '0',
            'publish_time': '0',
            'keyword': '徐州乡村游',
            'search_source': 'normal_search',
            'query_correct_type': '1',
            'is_filter_search': '0',
            'from_group_id': '',
            'offset': '0',
            'count': '15',
            'pc_client_type': '1',
            'version_code': '190600',
            'version_name': '19.6.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1152',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '119.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '119.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': '20',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '50',
            'webid': '7303052201974646283',
            'msToken': 'NR9qoR2IjiArDIzxMHhw0i4lpWypTi9no08TqTMU5uu18MXpTqzao0aHV31vDSGsPzlp0mZCQtzXNJN9NyZLOhwZG1ByKZYj8TtMjMXgcWSuan9G1-hdrQdiQ6aD',
            'X-Bogus': 'DFSzswVOupzANtOstmelEKXAIQ59'
        }
    def get_url(self):
        response=requests.get(self.url,headers=self.headers)
        json_data=response.json()
        # print(json_data)
        url_ids=jsonpath(json_data,'$..aweme_info.aweme_id')
        fy_ids=jsonpath(json_data,'$..impr_id')
        print(len(url_ids),len(fy_ids))
        for url in url_ids:
            link='https://www.douyin.com/video/'+url
            print(link)
            self.params_url(link)
    def params_url(self,url):
        response=requests.get(url,headers=self.headers)
        response.encoding = response.apparent_encoding
        # json_data=response.json()
        data=response.text


    def run(self):
        self.get_url()

if __name__ == '__main__':
    douy=Douy()
    douy.run()















