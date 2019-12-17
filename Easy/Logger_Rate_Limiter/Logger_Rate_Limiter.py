        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        #hash_message= hash(message)
        if message in self.log_dict:
            if (timestamp - self.log_dict[message]) < 10:
                return False
            else :
                self.log_dict[message] = timestamp 
                return True
        else:
            self.log_dict[message] = timestamp
            return True

            
