class DLLNode:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = self.prev = None

class DLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def removeNode(self, node):
		if node.prev or node.next:
			node.prev.next = node.next
			node.next.prev = node.prev
			node.next = node.prev = None
		return node

	def moveToHead(self, node):
		if self.head==node:
			return
		node=self.removeNode(node)
		if not self.head:
			self.head = self.tail = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
		return

	def removeTail(self):
		node = self.tail
		self.tail = node.prev
		self.tail.next = None
		del node

class LRUCache:
	def __init__(self,max_count):
		self.data = DLL()
		self.cache = {}
		self.max_count = max_count

	def put(self, key, value):
		if key in cache:
			node = cache[key]
			self.data.moveToHead(node)
		else:
			self.cache[key] = node = DLLNode(key, val)
			self.data.moveToHead(node)
			self.max_count -= 1
			if self.max_count < 0:
				self.data.removeTail()

	def get(self, key):
		if key in cache:
			node = cache[key]
			self.data.moveToHead(node)
			return node.value
		else:
			raise KeyException('key '+key+' not found')
