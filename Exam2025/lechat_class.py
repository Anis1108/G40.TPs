class LeChat:

    def __init__(self, max_client, max_message_len, ip_address, port):

        self.max_client = max_client
        self.max_message_len = max_message_len
        self.ip_address = ip_address
        self.port = port

        self.clients = []
        self.total_score = 0
        self.nb_scores = 0
