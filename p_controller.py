##################################################################################
# Your goal is to follow the comments and complete the tasks asked of you.
# Take this time to try and understand the workings of the empty class structure.
# The following quizzes will assume a understanding of a working class strucutre.
#
# Good luck designing your proportional controller!
#
##################################################################################

class P_Controller:
    def __init__(self, kp = 0.0, start_time = 0):

        # The P controller can be initalized with a specific kp value
        self.kp_ = float(kp)

        # Create internal class variables for
        # set_point_ and set it to 0.0, and start_time_
        # and set it to the start_time variable.
        ########################################


        ########################################

        # Store last timestamp
        self.last_timestamp_ = 0.0

        # Control effort history
        self.u_p = [0]

    # Set the altitude set point
    def setTarget(self, target):
        self.set_point_ = float(target)

    def setKP(self, kp):
        # Set the internal kp_ value with the provided variable
        # See setTarget if you are confused on how to do so
        ########################################

        ########################################

    def update(self, measured_value, timestamp):
        # Calculate delta_time using the last_timestamp_
        # and the provided timestamp argument
        ########################################

        ########################################

        if delta_time == 0:
            # Delta time is zero
            return 0

        # Calculate the error as the differnce between
        # the set_point_ and the measured_value
        ########################################

        ########################################

        # Set the last_timestamp_ to current timestamp
        ########################################

        ########################################

        # Calculate the proportional error here. Be sure to access the
        # the internal Kp class variable
        ########################################
        p = None
        ########################################

        # Set the control effort
        # u is the sum of all your errors. In this case it is just
        # the proportional error.
        ########################################
        u = None
        ########################################

        # Here we are storing the control effort history for post control
        # observations.
        self.u_p.append(p)

        return u
