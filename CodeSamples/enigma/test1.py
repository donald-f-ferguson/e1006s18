from enigma.machine import EnigmaMachine

# setup machine according to specs from a daily key sheet:

machine = EnigmaMachine.from_key_sheet(
       rotors='II IV V',
       reflector='B',
       ring_settings=[1, 20, 11],
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

# set machine initial starting position
machine.set_display('WXC')

# decrypt the message key
msg_key = machine.process_text('KCH')

# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)

ciphertext = 'NIBLFMYMLLUFWCASCSSNVHAZ'
plaintext = machine.process_text(ciphertext)
print(plaintext)

machine.set_display('XYZ')
c1 = machine.process_text("THESEXAREXTIMESXTHATXTRYXMENSXSOULS")
print("C1 = ", c1)
machine.set_display('XYZ')
c3 = machine.process_text(c1)
print(c3)

x = c3.find("ARE")
print(x)
