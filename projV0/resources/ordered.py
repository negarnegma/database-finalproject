class Ordered:
    def __init__(self, ordered_id, os, ram, cores, disk, cpu_freq, bound_rate, ssh_id, owner_id, daily_cost,
                 offered_config_id):
        self.ordered_id = ordered_id
        self.os = os
        self.ram = ram
        self.cores = cores
        self.disk = disk
        self.cpu_freq = cpu_freq
        self.bound_rate = bound_rate
        self.ssh_id = ssh_id
        self.owner_id = owner_id
        self.daily_cost = daily_cost
        self.offered_config_id = offered_config_id