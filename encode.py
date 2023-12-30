def getUrlFromMediaId(media_id):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    shortened_id = ''

    while media_id:
        media_id, remainder = divmod(media_id, 64)
        shortened_id = alphabet[remainder] + shortened_id

    print(shortened_id)

getUrlFromMediaId(3260617099286381188)

def getMediaIdFromUrl(shortened_id):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    media_id = 0

    for char in shortened_id:
        media_id = media_id * 64 + alphabet.index(char)

    print(media_id)

getMediaIdFromUrl('CytLNXGBGYs')