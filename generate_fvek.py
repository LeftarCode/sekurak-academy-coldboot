

#	AES_128_DIFFUSER    = 0x8000,
#	AES_256_DIFFUSER    = 0x8001,
#	AES_128_NO_DIFFUSER = 0x8002,
#	AES_256_NO_DIFFUSER = 0x8003,
#	AES_XTS_128         = 0x8004,
#	AES_XTS_256         = 0x8005,

enc_type = "0480"
first_key = "020c0a3e37db483bdf39a57db12690a8"
second_key = "4fedac6f63454e208488dc8771eb3172"

buf = bytearray.fromhex(enc_type + first_key + second_key)
with open("fvek.key", "wb") as file:
	file.write(buf)
print(buf)


