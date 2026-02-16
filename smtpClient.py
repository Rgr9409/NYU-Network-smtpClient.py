from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        clientSocket.close()
        return

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    if recv1[:3] != '250':
        clientSocket.close()
        return

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mail_from = 'MAIL FROM:<alice@test.com>\r\n'
    clientSocket.send(mail_from.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2) 
    if recv2[:3] != '250':
        clientSocket.close()
        return
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt_to = 'RCPT TO:<bob@test.com>\r\n'
    clientSocket.send(rcpt_to.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    if recv3[:3] != '250':
        clientSocket.close()
        return
    #clientSocket.recv(1024)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data_command = 'DATA\r\n'
    clientSocket.send(data_command.encode())
    recv4 =  clientSocket.recv(1024).decode()
    #print(recv4)
    if recv4[:3] != '354':
        clientSocket.close()
        return
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        clientSocket.close()
        return
    #clientSocket.recv(1024)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_command = 'QUIT\r\n'
    clientSocket.send(quit_command.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '221':
        clientSocket.close()
        return
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')