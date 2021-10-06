#  ![logo](doc/logo.png) `IPsecRepack`
## IPsecRepack

(c) Dmitry Ponyatov <<dponyatov@gmail.com>> 2020 All rights reserved

github: https://github.com/ponyatov/IPsecRepack/

# <a href="rust/IPsecRepack/index.html">rustdoc</a>


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

<hr>
powered with [metaL](https://github.com/ponyatov/metaLgen)
