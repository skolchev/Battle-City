from Tank import Tank


class EnemyTank(Tank):

	# self, x, y, width, height, resources, speed, armor, attack, object_id
	def __init__(self, x, y, width, height, resources, speed, armor, attack):
		super(EnemyTank, self).__init__(x, y, width, height, resources, speed, armor, attack)
