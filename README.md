This is a minimal IPC library that can be used to support the programming assignment of the QuCrypto class.
It simulates a Classical Authenticated Channel.
In order to run the library you have to:
- run ipcServer.py as a separate process
- for each player in the game, create an instance of ipcCacClient and use its methods to send and receive classical data to/from the other players.

You can some examples about using the ipcCacClient in the unit testing files.

Notes:
- This library provides only the bare minimum set of features required by the programming assignment
- It was designed to be easy to implement and to use.
- It was *not* designed for optimal performances or to teach other people how to write software.
- It is working fine in my simple bb84 protocol simulation, but there may still be bugs I have not found.

Updates:
Jan 22, 2018
Added ability for each node to peek at messages on the channel.
A node has to call startPeeking() to start collecting the messages on the channel.
Any call to peekMessage() then returns a tuple containing the name of thew sender node, the name of the destination node and the message.


