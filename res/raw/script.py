import android

droid = android.Android()

def show(text):
    extras = {}
    extras['ENCODE_TYPE'] = 'TEXT_TYPE'
    extras['ENCODE_DATA'] = text
    intent = droid.makeIntent('com.google.zxing.client.android.ENCODE', None, None, extras).result
    droid.startActivityIntent(intent)

if __name__ == '__main__':
    text = droid.dialogGetInput().result
    if text:
        show(text)
