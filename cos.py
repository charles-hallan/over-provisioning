# CoS_i: [MRth_i, Brv_i, Bu_i, Bav_i]

class CoS:
	def __init__(self, mrth, brv, bu):
		self.mrth = mrth
		self.brv = brv
		self.bu = bu
		self.bav = brv - bu;
		self.brv_min = brv

	def overprov(self, brq):
		bov = (self.bu / self.mrth) * (self.mrth - self.bu - brq)
		self.brv = bov + brq + self.brv
		if self.brv > self.mrth:
			self.brv = self.mrth;

	def bw_release(self):
		b_idx = (self.brv - self.bu) / self.brv
		th_idx = (self.mrth - self.brv) / self.mrth
		brl_mrth = ((b_idx + th_idx) / 2) * (self.mrth - self.brv)
		return brl_mrth;

	def bu_add(self, brq):
		self.bu = self.bu + brq;

	def bu_sub(self, brl):
		self.bu = self.bu - brl;

	def bav_sub(self):
		self.bav = self.brv - self.bu;

	def mrth_add(self,brl):
		self.mrth = self.mrth + brl;
