import websocket
import _thread
import time
import rel

def on_message(ws, message):

    if message == "ready;":
        print("ready...")
        ws.send('audio_samplerate:8000;')
        ws.send('AUDIO_STREAM_SAMPLE_TYPE:int16;')
        ws.send('audio_start:0;')
    #print(message)
    elif len(message) == 576:
        # audio received
        receiver = message[:4]
        sample_rate = int.from_bytes(message[4:8], "little")
        format = int.from_bytes(message[8:12], "little")
        codec = message[12:16]
        crc = message[16:20]
        audio_length = int.from_bytes(message[20:24], "little")
        type = int.from_bytes(message[24:28], "little")
        channel = int.from_bytes(message[28:32], "little")
        reserved = int.from_bytes(message[32:36], "little")
        data = message[36:]
        #print(type)
        if type > 1:
            print(type)
    elif message == "trx:0,true;":
        print(message)
        ws.send('audio_samplerate:8000;')
        ws.send('AUDIO_STREAM_SAMPLE_TYPE:int16;')
        ws.send('audio_start:0;')
        #ws.send(b'\x00\x00\x00\x00@\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00V\x00\x00\x00am_sample_type:int16;nection\xbc\x18\xbc\x18j\x0bj\x0bQ\x03Q\x03\xff\xda\xff\xda\x85\x18\x85\x18\xd2\x00\xd2\x00\x85\xde\x85\xde\xbb\x1e\xbb\x1e\x19\x04\x19\x04w\xd8w\xd8s\xe7s\xe7o\xf4o\xf4p\xc2p\xc2\xab\xe7\xab\xe7\xca\x06\xca\x06\x0e\xba\x0e\xba\x98\xfb\x98\xfb\xb0\xf0\xb0\xf0\xdb\xd7\xdb\xd7h\rh\rU\x01U\x01\' \' \xb0\x19\xb0\x19\xab/\xab/\x106\x106\xa6\x06\xa6\x06\x8e\x18\x8e\x18\x18\xfe\x18\xfe\x83\xfd\x83\xfdVYVYI/I/t\xe9t\xe9\x81\x11\x81\x11\xe7\xf2\xe7\xf2\x8f\x1e\x8f\x1e\x9a\xf6\x9a\xf6\n\x8f\n\x8f\x87#\x87#\xc9\x1e\xc9\x1e\xca\x1e\xca\x1e\x00M\x00M\\\xdd\\\xdd\x9d:\x9d:\xf1\x05\xf1\x05\xc8\xa3\xc8\xa3\xc2\x0b\xc2\x0b"\xde"\xdey\x06y\x06\xc68\xc68h/h/\x08:\x08:\xe5\x07\xe5\x07\x85\x03\x85\x03\xc7\xae\xc7\xae\xeb\xa6\xeb\xa6\x01\xe0\x01\xe0M\xf5M\xf5k(k(\xf6$\xf6$\xeb\x18\xeb\x18L\xbdL\xbd\x1f\xea\x1f\xea{&{&T\xd2T\xd2(\xbd(\xbd\x9d\xea\x9d\xea\x9ee\x9eeX>X>$)$)\n\x1f\n\x1f\x80\xe7\x80\xe7@\x0e@\x0ej\xdcj\xdc\x10\xdd\x10\xdd\x99\xcb\x99\xcbd d \xaa-\xaa-3\x023\x02\x1f%\x1f%\xb6\xaf\xb6\xafu%u%\x1b\xfe\x1b\xfe\xfa\xb5\xfa\xb5\t\x12\t\x12\xa0\xe5\xa0\xe5\xc9\x0e\xc9\x0e\xb2\r\xb2\r\xa4\x15\xa4\x15\xc9\xd8\xc9\xd8\xa3\xe3\xa3\xe3L\x0fL\x0fm\xe6m\xe6\xb6\x0e\xb6\x0e\x13\xd4\x13\xd4\x96\xea\x96\xea0\r0\r\xc2\xea\xc2\xea\x8a\xec\x8a\xec\xf1\xc9\xf1\xc9\xc9\x03\xc9\x03l\xf8l\xf8%\n%\n\x15\x0e\x15\x0et\xc3t\xc37\xf17\xf1\x9f\xf6\x9f\xf6I\x11I\x11T\x1eT\x1e\x92\x1b\x92\x1b\xee<\xee<\xe91\xe91\x9a\x05\x9a\x05i\x00i\x00\xf7\x00\xf7\x00Q\x10Q\x10\xbd\x1b\xbd\x1b\xa5\x03\xa5\x03v@v@\x1b*\x1b*\xa9$\xa9$\xf9\x17\xf9\x17\x80\xd9\x80\xd9\r\xfe\r\xfe\xca\xf3\xca\xf3(\x04(\x04;\xe9;\xe9r\xecr\xec[\n[\n')
    else:
        print(message)
    #ws.send(b'\x00\x00\x00\x00@\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\xe1\x02\x00\x00\x00\x00\x00\x00\x9f\xc0#\x00\x00\x1b\x90\x90\x90\x08\xd8D\x00\x00\x00x\xba.\x1f\x80\xbb\x9b\x8b\x9b\xee+\xee+k\x02k\x02[\xf8[\xf8\xcf\x1c\xcf\x1c\xe8/\xe8/\r\x11\r\x11\'\xd4\'\xd4\x8f\xea\x8f\xea\x01\xdb\x01\xdb!\xb2!\xb2=\xf8=\xf8\xba=\xba=\xf8\x17\xf8\x17\x96\xf9\x96\xf9Q\x04Q\x04\xce\xfb\xce\xfb\xe2\xe2\xe2\xe2\x11\xd1\x11\xd1(\x06(\x06\x0e\x1b\x0e\x1bP\xf8P\xf80 0 \xf2\x16\xf2\x16g\xfag\xfa\x96\xfb\x96\xfb\x1c\xcb\x1c\xcb\x16\x0c\x16\x0c\xbc:\xbc:\x15\x1f\x15\x1f\x9f\x1f\x9f\x1f\x00\xf8\x00\xf8\xdb\x0b\xdb\x0b\x98\r\x98\ro\xf7o\xf7{\xec{\xecF\xfaF\xfac"c"\xd3\x10\xd3\x10\xde$\xde$"%"%F\x05F\x05\xbc\xff\xbc\xff\x84\x0c\x84\x0c\xe4\xf4\xe4\xf4\x99\xc4\x99\xc4\xe0\xe4\xe0\xe4\xe1\x17\xe1\x17\x1c\xec\x1c\xec\xa9\x1c\xa9\x1c\x916\x916\xc5\xcf\xc5\xcf\xc5\x0e\xc5\x0e\xcb\xed\xcb\xed\xb1\xda\xb1\xda!1!1u\xf6u\xf6\xc7&\xc7&/\xf0/\xf0\xee\xba\xee\xba\xa5\x00\xa5\x00\x9a\xf0\x9a\xf0V8V8\x9d\xec\x9d\xec[\xca[\xca\xc6,\xc6,v\xedv\xed\xd3\xcf\xd3\xcf\xa7\xcd\xa7\xcd!\x0c!\x0c\x19<\x19<\x86\x0e\x86\x0e\x83\xe4\x83\xe4E\xb7E\xb7\x94\xfe\x94\xfe\x98\x08\x98\x08\xbb\xf8\xbb\xf8m5m5e\xf7e\xf7\xd6\xf1\xd6\xf1\xfe\x1b\xfe\x1b\x91#\x91#%\t%\t~\xab~\xab\x8a\xfe\x8a\xfe\x0f\x15\x0f\x15\xd7\xd0\xd7\xd0\xee\x17\xee\x17\xad\xcd\xad\xcd\x08\xe3\x08\xe3\xb6,\xb6,\xb6\xd4\xb6\xd4\xe1\x10\xe1\x10\x89\x04\x89\x04@\xcc@\xcct\xeat\xea:\xdf:\xdf\r\r\r\r\x1e\x14\x1e\x14\xe4\x0f\xe4\x0f\xcb#\xcb#\xab\t\xab\t\x05\x03\x05\x03f\x00f\x00\xa7\xdc\xa7\xdc\xcc\xe7\xcc\xe7\x88\x07\x88\x07\xbc\xef\xbc\xef\xa0\x10\xa0\x10\xf6\xf5\xf6\xf5\xd1\xd2\xd1\xd2\x9b\x10\x9b\x10\xb7\xe6\xb7\xe6\x07\xe3\x07\xe37\xfc7\xfcc\x10c\x10\xa51\xa51\x13,\x13,YOYO\xdf0\xdf0\x96\xec\x96\xec[\t[\t\x8d@\x8d@t\xfbt\xfbl\xecl\xec\xf2\xf3\xf2\xf3\n\xd4\n\xd4\x7f\xfb\x7f\xfbk(k(')

    """
    sample_rate = 8000
    audio_length = 1200
    data = bytes([0]) * 512

    testframe = bytearray(512+64)
    testframe[4:8] = sample_rate.to_bytes(4, byteorder="big")
    testframe[64:len(data)] = data

    ws.send(testframe)
    """
def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    #ws.send('IQ_SAMPLERATE:8000;')
    #ws.send('audio_samplerate:8000;')
    #ws.send('audio_start:0;')
    #ws.send('iq_start:0;')


if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:50001",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if con>
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()


from websocket import create_connection