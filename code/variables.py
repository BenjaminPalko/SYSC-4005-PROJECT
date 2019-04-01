class ReplicationVariables(object):

    def __init__(self, logger):
        self.logger = logger
        self.service_times = {
            "inspector_1": [],
            "inspector_22": [],
            "inspector_23": [],
            "workstation_1": [],
            "workstation_2": [],
            "workstation_3": [],
        }
        self.idle_times = {
            1: [],
            2: [],
            3: [],
        }
        self.block_times = {
            1: [],
            2: [],
            3: []
        }
        self.products = {
            1: 0,
            2: 0,
            3: 0,
        }

    def add_insp_1_st(self, value):
        self.service_times["inspector_1"].append(value)

    def add_insp_22_st(self, value):
        self.service_times["inspector_22"].append(value)

    def add_insp_23_st(self, value):
        self.service_times["inspector_23"].append(value)

    def add_ws_1_st(self, value):
        self.service_times["workstation_1"].append(value)

    def add_ws_2_st(self, value):
        self.service_times["workstation_2"].append(value)

    def add_ws_3_st(self, value):
        self.service_times["workstation_3"].append(value)

    def add_insp_1_bt(self, value):
        self.block_times[1].append(value)

    def add_insp_22_bt(self, value):
        self.block_times[2].append(value)

    def add_insp_23_bt(self, value):
        self.block_times[3].append(value)

    def add_ws_1_it(self, value):
        self.idle_times[1].append(value)

    def add_ws_2_it(self, value):
        self.idle_times[2].append(value)

    def add_ws_3_it(self, value):
        self.idle_times[3].append(value)

    def add_product_1(self):
        self.products[1] += 1

    def add_product_2(self):
        self.products[2] += 1

    def add_product_3(self):
        self.products[3] += 1
