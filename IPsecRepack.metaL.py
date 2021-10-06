## @file
## @brief meta: IPsecRepack

from metaL import *

p = Project(
    title='''IPsecRepack''',
    about='''
* https://drive.google.com/file/d/1d6pkysbiEaGQ_-65Bi0jCbcluIJRUjs5/view

There is IPSEC encrypted channel. Traffic contains big UDP packets that must be
fragmented before transmitting. By default, Linux encrypts packets and then
performs fragmentation of the encrypted packet. So we get fragmented ESP packets
on output. Equipment on the other channel side does not understand fragmented
ESP packets.

1. Create kernel module (kernel v3.10) that fragments packets before encryption
   to get all ESP packets are not fragmented.
2. Allow to enable/disable from user-space using `/sys` or `/proc` FS

## Driver writing

* https://www.youtube.com/watch?v=4tgluSJDA_E
''') \
    | Rust() \
    | Kernel()

p.driver_br // (Sec()
                // 'BR2_LINUX_KERNEL_CUSTOM_VERSION=y'
                // 'BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE="3.10.108"'
                // 'BR2_GCC_VERSION_8_X=y'
                )

p.sync()
