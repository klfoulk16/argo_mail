"""Fixtures and other wonderful things I'll set up for testing"""
import pytest
from main import reformat_csv

@pytest.fixture
def file_contents():
    # Contents of file id "1HZxhz0ot6FUDD6gDQ29MzE7C73PX30Rt" in my drive
    return b'id,provider,uid,encrypted_password,reset_password_token,reset_password_sent_at,allow_password_change,remember_created_at,sign_in_count,current_sign_in_at,last_sign_in_at,current_sign_in_ip,last_sign_in_ip,confirmation_token,confirmed_at,confirmation_sent_at,unconfirmed_email,first_name,last_name,username,image,email,tokens,created_at,updated_at,push_token,lat,lng,heading\r\n12945,facebook,1.02E+16,$2a$11$.55gAUuULd9UmTbWRUF1XebyHiys2BH.3JvpA.Ggjvp9Zjt2pMM5u,,,FALSE,,2,2020-06-27 00:20:12 UTC,2020-05-27 04:58:23 UTC,96.58.186.169,96.58.186.169,,2020-05-27 04:58:23 UTC,,,Dorian,Angello,dorian_angello,https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=10222660769883302&height=50&width=50&ext=1593147503&hash=AeRpv6k_34yxVJEe,magicmock@mock.com,"{""T5jmndFWgHBtBTCMSbVPIQ""=>{""token""=>""$2a$10$qj9o.C3XYvNY5WxN0V9I/.Sf9ydqGRRgutKH4VZJPMjafFh7a1yIW"", ""expiry""=>1594426812}}",2020-05-27 04:58:23 UTC,2020-06-27 00:20:12 UTC,,,,\r\n12939,google,1.16E+20,$2a$11$UhTWsY82J3OaF2bWydNQW..a2n2l3fEl5uFNmg3aCuV.55TndKcv6,,,FALSE,,1,2020-05-29 19:40:35 UTC,2020-05-29 19:40:35 UTC,96.27.94.47,96.27.94.47,,2020-05-29 19:40:35 UTC,,,Terence,Filipiak,terence_filipiak,https://lh3.googleusercontent.com/a-/AOh14GiCDv2W3AwDBtPxiGUN3vFy1grXqebdRywUpkgL=s128,magicmock2@mock.com,"{""NvZD82dFUMN7GE3pSaqCtw""=>{""token""=>""$2a$10$0RVEMGOkQITfgTuV08HvbuyTIOK4MCrw44o1LoV9x6zwJAXWys97."", ""expiry""=>1591990835}}",2020-05-29 19:40:35 UTC,2020-06-08 19:11:28 UTC,,41.674117,-86.238385,261.2177774\r\n12941,email,sshani33@verizon.net,$2a$11$qzfe48Pz6755cqIv3pKKXuzZUJsLRgE/Z.xhWJooQm6qAuidov1YW,,,FALSE,,0,,,,,dntL2sXficRVDaLHrmcx,,2019-03-05 21:33:50 UTC,,Sharone,Shani,Sshani,,magicmock3@mock.com,{},2019-03-05 21:33:50 UTC,2019-03-05 21:33:50 UTC,,,,\r\n12948,email,lex9615@icloud.com,$2a$11$niHHm3bua.JIZpOjmOtjFOt6i/6FxIFC.Hhl6JJxXDzkK3R3s3duy,,,FALSE,,0,,,,,jmCdByp36fuJ79H34GLx,,2020-05-24 13:22:44 UTC,,Lexie,Williams,lex9615,,magicmock4@mock.com,{},2020-05-24 13:22:44 UTC,2020-05-24 13:22:44 UTC,,,,\r\n12952,google,1.02E+20,$2a$11$isNIPN8pMnBYLXpLlAwUIeigNehAwAlmR7/V8GMxzAUyK6S48aHae,,,FALSE,,1,2020-01-29 15:03:15 UTC,2020-01-29 15:03:15 UTC,162.129.252.233,162.129.252.233,,2020-01-29 15:03:15 UTC,,,Brian,Burrows,brian_burrows,https://lh3.googleusercontent.com/a-/AAuE7mBomQjVHWEG6NuyZi8X_APJGyOT_l08tD2VXt-u5A=s96-c,magicmock5@mock.com,"{""mTtgCdqur5bKmJUFnuiYEA""=>{""token""=>""$2a$10$TqOyilsMQW4MQnkh6rD7B.luvWJpbMKCq896Fw75WcPMwKWbL11me"", ""expiry""=>1581519795}}",2020-01-29 15:03:15 UTC,2020-02-01 02:57:52 UTC,,39.151551,-76.466789,0\r\n12943,email,sof\xc3\xadaalvarado39@yahoo.com,$2a$11$fRjFsave/6m9lQPE0Y.pe.6Vk9yps0sI4Bnw8ObeLODs2p3dkoSka,,,FALSE,,0,,,,,cSzq7f85kdsTjzTJ-V6Z,,2020-07-11 18:40:23 UTC,,Sof\xc3\xada ,Mart\xc3\xadnez,sofiaalva20,,magicmock6@mock.com,{},2020-07-11 18:40:23 UTC,2020-07-11 18:40:23 UTC,,,,\r\n12944,google,1.02E+20,$2a$11$pv0pN4X6yi5Kx2VcY6S82uQcJlh8GxzL1OukV.D7C6iviWlWVJ.lS,,,FALSE,,2,2019-03-22 14:31:10 UTC,2019-03-06 18:54:41 UTC,174.205.8.161,174.205.16.99,,2019-03-06 18:54:41 UTC,,,Sharone,Shani,sharone_shani,https://lh3.googleusercontent.com/a-/AAuE7mC4nn2vF-aPqw3dB7seaTMBUxSmnWlGHpH1rEI,magicmock7@mock.com,"{""emZzWzhJSAHfMbKzWqQreg""=>{""token""=>""$2a$10$MdpnFC1A.ukrWG4uZ8Kxvej8uFqi0/kc5LdPoAqVBB3I/bu7.Yz12"", ""expiry""=>1557224882}, ""4Z_DWdp6kAGobjCJ_je5Cg""=>{""token""=>""$2a$10$YnRnSyWLcPwoi9hFdNidPO1EWUOOY18ngvChgjtHfsOyU1/AwVj/6"", ""expiry""=>1557239728}, ""p1CPP8Xb0loGKw3xwh6NZg""=>{""token""=>""$2a$10$pP.3QRw6QlP5IQTDajdlb.zOmpKVrIIeezPrQQb9pXiDAEa4nMRUi"", ""expiry""=>1558191508}}",2019-03-06 18:54:41 UTC,2019-05-04 14:58:28 UTC,,,,\r\n12938,email,mb@mbwd.us,$2a$11$TKKwPozjHDh4I/XDXcZDe.SWuaqIGWJBG335OxHKiD56rOI5WVZg6,Y6W784scsRVBQi6ezwQm,2020-01-05 13:02:36 UTC,TRUE,,2,2019-10-01 03:13:56 UTC,2019-10-01 03:10:49 UTC,174.205.14.250,174.205.14.250,vpw1yy_xvYFBXzqHe4QE,2019-10-01 03:10:49 UTC,2019-10-01 03:09:37 UTC,,Michael,Barlow,driller,,magicmock8@mock.com,"{""FgUAaYdhe8So0IiboOvNlw""=>{""token""=>""$2a$10$jqwqehtiBh5QCQ6WXh4iSe264G8KaX9r/uF6vNOJ5nmTkgsQBbEZS"", ""expiry""=>1579439155}}",2019-10-01 03:09:37 UTC,2020-01-05 13:05:55 UTC,,39.330087,-76.776818,249.3891323\r\n12946,email,bugsymc@verizon.net,$2a$11$233/AGEn3AUrHPPcRrH9uOstir8p.Rny1Sv7hb2bylVur4LG0eGyS,151ba65ac3330e931b07f02d3316741677a825645293ea9a7508dd2def125d70,2020-03-14 19:06:55 UTC,FALSE,,0,,,,,s8-VnU2smpP49kKQCxRS,,2020-01-25 19:20:29 UTC,,Captin,Hook,gillagan,,magicmock9@mock.com,{},2020-01-25 19:20:29 UTC,2020-03-14 19:06:55 UTC,,,,\r\n12951,email,cwlrainbow@aol.com,$2a$11$tFPES5OEcCEbjID7p9awsu5y7eW9yMtE08tjpWNOFuK.K7wrc1Lky,,,FALSE,,1,2020-08-02 22:38:33 UTC,2020-08-02 22:38:33 UTC,107.77.203.39,107.77.203.39,4UvGnRsigMQpQPaXwdod,2020-08-02 22:34:08 UTC,2020-08-02 22:31:33 UTC,,Craig,Laudenslager,PABoatBoy,,magicmock10@mock.com,"{""z03LZ8KrcMGVpXFxLn7h6Q""=>{""token""=>""$2a$10$g94qyJ0SVaYIkVvYE2tVqu81rv3o0mINfVv9mKnFzwdS6f42JWI1."", ""expiry""=>1597617513}}",2020-08-02 22:31:33 UTC,2020-08-03 02:53:55 UTC,,40.296893,-76.116531,0\r\n12940,email,poppopgarry123@gmail.com,$2a$11$LDMXIqsR/Xa5WhD8O15ktuBkHu7fpmJMYPwJW1LMeqOlNO0JBjCf2,,,FALSE,,0,,,,,oiBStvs2S2Z4h8oVAoax,,2019-11-22 20:20:15 UTC,,Garry,Harman,poppopgarry123,,magicmock11@mock.com,{},2019-11-22 20:20:15 UTC,2019-11-22 20:20:15 UTC,,,,\r\n12950,email,paigemalban@gmail.com,$2a$11$G9ItjECotev1ZTDRzs7QVOO7I.6yuiMOn.7Tyadx9m/C12yuAdnAe,,,FALSE,,1,2019-09-19 20:59:02 UTC,2019-09-19 20:59:02 UTC,204.126.204.12,204.126.204.12,j4CyyzUaet3eSxHUzXbk,2019-09-19 20:59:02 UTC,2019-09-19 20:57:40 UTC,,Paige,Hi,random,,magicmock12@mock.com,"{""AR4WK4y4LiMkli90OW48Fg""=>{""token""=>""$2a$10$jVvZs8ngSZ7MJ.PMSibtRuPhtXXIA9tJ0BsiPPoDmzTjoY7A1etsm"", ""expiry""=>1570136342}}",2019-09-19 20:57:40 UTC,2019-09-19 20:59:02 UTC,,,,\r\n12949,email,nkurek84@gmail.com,$2a$11$dK5Dg47/gAAun1E0.rwsxe/dWlzAHyTQfW1LYv5AA14qlAGZ9Q5/O,,,FALSE,,2,2019-08-26 00:18:14 UTC,2019-08-26 00:17:46 UTC,73.213.73.45,73.213.73.45,4kH_ckZYDyBZ8vSoMNaS,2019-08-26 00:17:45 UTC,2019-08-26 00:17:29 UTC,,Nathan,Kurek,Nathan_Kurek,,magicmock13@mock.com,"{""_p35rHrcoCt1nHoaUCCrFA""=>{""token""=>""$2a$10$B96G.0LCP2DaNpXPrF7ha.VdKJt.Ok5XHptgZ1E4yOlKrgTRkm6M."", ""expiry""=>1567988265}, ""fswCsTXZCFktNXN5LMzQ2g""=>{""token""=>""$2a$10$8L8stoUuOvKtKQHWsmsUuen42X1Ra3n9zrawLeR1wUAT7f8w5BrEC"", ""expiry""=>1567988294}}",2019-08-26 00:17:29 UTC,2019-09-01 17:49:26 UTC,,39.577064,-76.219505,212.8245164\r\n12947,email,poppopgarry1113@gail.com,$2a$11$fXxDEUtx.LkvRSor8VeTzugE/qDed2NRkg.mIOuOOozm9hI/CA8D.,,,FALSE,,0,,,,,yUWU6kVVVeJSHcuuZreW,,2019-11-22 20:24:04 UTC,,Garry,Harman,poppopgarry,,magicmock14@mock.com,{},2019-11-22 20:24:04 UTC,2019-11-22 20:24:04 UTC,,,,\r\n12942,email,kathleen@bytelion.com,$2a$11$Hx3RzMFwyhUhiuswHMZ9Z.3sDeFshhTJwk7NI9hMxGXGAd4rxNayy,,,FALSE,,2,2019-09-16 18:56:47 UTC,2019-09-16 18:56:20 UTC,174.205.3.14,73.129.80.4,LW26sXpZiTzyvz7HznFP,2019-09-16 18:56:20 UTC,2019-09-16 18:55:29 UTC,,Kathleen,Cesar,kcesar,,magicmock15@mock.com,"{""JTePlK0iG-BO10QOp1CBPg""=>{""token""=>""$2a$10$0v8rHZB3FMjEarw821UOYugZM0yE3Al5GEWNAogaprvD0uNyf19p6"", ""expiry""=>1569869780}, ""RYVpV7ydIeYP0vX_La9OLw""=>{""token""=>""$2a$10$xiLacNkJcpGlzA2erjlf5eAjzEfwXI5gPlUr9.8p2N8qDfokCcEEa"", ""expiry""=>1569869807}}",2019-09-16 18:55:29 UTC,2019-09-16 19:10:03 UTC,,39.493285,-76.660561,150.3932972'

@pytest.fixture
def df(file_contents):
    return reformat_csv(file_contents, 12950)

@pytest.fixture
def long_df(file_contents):
    df = reformat_csv(file_contents, 0)
    return df.append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True).append(df, ignore_index=True)

@pytest.fixture
def subscribe_response():
    return {
    "new_members": [
        {
        "id": "string",
        "email_address": "string",
        "unique_email_id": "string",
        "email_type": "string",
        "status": "subscribed",
        "merge_fields": {
            "property1": null,
            "property2": null
        },
        "interests": {
            "property1": true,
            "property2": true
        },
        "stats": {
            "avg_open_rate": 0,
            "avg_click_rate": 0
        },
        "ip_signup": "string",
        "timestamp_signup": "2019-08-24T14:15:22Z",
        "ip_opt": "string",
        "timestamp_opt": "2019-08-24T14:15:22Z",
        "member_rating": 0,
        "last_changed": "2019-08-24T14:15:22Z",
        "language": "string",
        "vip": true,
        "email_client": "string",
        "location": {
            "latitude": 0,
            "longitude": 0,
            "gmtoff": 0,
            "dstoff": 0,
            "country_code": "string",
            "timezone": "string"
        },
        "last_note": {
            "note_id": 0,
            "created_at": "2019-08-24T14:15:22Z",
            "created_by": "string",
            "note": "string"
        },
        "tags_count": 0,
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "list_id": "string",
        "_links": [
            {
            "rel": "string",
            "href": "string",
            "method": "GET",
            "targetSchema": "string",
            "schema": "string"
            }
        ]
        }
    ],
    "updated_members": [
        {
        "id": "string",
        "email_address": "string",
        "unique_email_id": "string",
        "email_type": "string",
        "status": "subscribed",
        "merge_fields": {
            "property1": null,
            "property2": null
        },
        "interests": {
            "property1": true,
            "property2": true
        },
        "stats": {
            "avg_open_rate": 0,
            "avg_click_rate": 0
        },
        "ip_signup": "string",
        "timestamp_signup": "2019-08-24T14:15:22Z",
        "ip_opt": "string",
        "timestamp_opt": "2019-08-24T14:15:22Z",
        "member_rating": 0,
        "last_changed": "2019-08-24T14:15:22Z",
        "language": "string",
        "vip": true,
        "email_client": "string",
        "location": {
            "latitude": 0,
            "longitude": 0,
            "gmtoff": 0,
            "dstoff": 0,
            "country_code": "string",
            "timezone": "string"
        },
        "last_note": {
            "note_id": 0,
            "created_at": "2019-08-24T14:15:22Z",
            "created_by": "string",
            "note": "string"
        },
        "tags_count": 0,
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "list_id": "string",
        "_links": [
            {
            "rel": "string",
            "href": "string",
            "method": "GET",
            "targetSchema": "string",
            "schema": "string"
            }
        ]
        }
    ],
    "errors": [
        {
        "email_address": "string",
        "error": "string",
        "error_code": "ERROR_CONTACT_EXISTS"
        }
    ],
    "total_created": 42,
    "total_updated": 42,
    "error_count": 42,
    "_links": [
        {
        "rel": "string",
        "href": "string",
        "method": "GET",
        "targetSchema": "string",
        "schema": "string"
        }
    ]
    }