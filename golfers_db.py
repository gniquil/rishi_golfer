class ScoreStore:

  def __init__(self, file_path):
    self._store = {}
    self.file_path = file_path
    self.load()

  def load(self):
    file_path = self.file_path
    file_contents = open(file_path).read().split("\n")
    for name, score in zip(*[iter(file_contents)]*2):
      self._store[name] = int(score)

  def get_score(self, name):
    if name in self._store:
      return self._store[name]
    else:
      return None

  def get_scores(self):
    return self._store.copy()

  def has_score(self, name):
    return name in self._store

  def update_score(self, name, score):
    if name in self._store:
      self._store[name] = score
      self.persist()
      return True
    else:
      return False

  def add_score(self, name, score):
    if name in self._store:
      return False
    else:
      self._store[name] = score    
      self.persist()
      return True

  def remove_score(self, name):
    if name in self._store:
      del self._store[name]
      self.persist()
      return True
    else:
      return False

  def persist(self):
    with open(self.file_path, 'w') as f: 
      for name, score in self._store.iteritems():
        f.write(name + "\n")
        f.write(str(score) + "\n")

class InvalidInputException(Exception): pass

class StoreRepl:

  def __init__(self, score_store):
    self.score_store = score_store
    self.commands = {
      "c": "make a change to one of the records",
      "a": "add a record",
      "r": "remove a record",
      "d": "displays all records",
      "s": "show the file content",
      "q": "time to quit the program",
    }
    self.should_continue = True

  def print_options(self):
    print("")
    print("Menu")
    print("d" + "  (" + self.commands["d"] + ")")
    print("a" + "  (" + self.commands["a"] + ")")
    print("r" + "  (" + self.commands["r"] + ")")
    print("c" + "  (" + self.commands["c"] + ")")
    print("s" + "  (" + self.commands["s"] + ")")
    print("q" + "  (" + self.commands["q"] + ")")

  def normalize_command(self, command):
    command = command.lower()
    if len(command) != 1 or command not in self.commands.keys():
      raise InvalidInputException("Invalid command!")
    return command

  def normalize_score(self, user_input):
    try:
      score = int(user_input)
      if score in range(1, 151):
        return score
      else:
        raise InvalidInputException("Invalid number, must be between 1 and 151!")
    except:
      raise InvalidInputException("Invalid score!")

  def run(self):
    score_store = self.score_store
    
    while self.should_continue:
      try:
        self.print_options()
        command = self.normalize_command(raw_input(">> "))
        print("")
        getattr(self, "handle_" + command)()
      except InvalidInputException as e:
        print("Invalid input, error message: " + e.message)
      except KeyboardInterrupt:
        print("\nInput interrupted!")


  def handle_c(self):
    name = raw_input("Enter the name of the golfer you want to change the score for: ")

    if not self.score_store.has_score(name): raise InvalidInputException("This golfer doesn't exist!")

    score = self.normalize_score(raw_input("Enter the score for the golfer: "))

    self.score_store.update_score(name, score)

    print("")
    print("score updated for " + name)

  def handle_a(self):
    name = raw_input("Enter the name of the golfer you want to add to the file: ")

    if self.score_store.has_score(name): raise InvalidInputException("This golfer already exists!")

    score = self.normalize_score(raw_input("Enter the score for the golfer: "))

    self.score_store.add_score(name, score)

    print("")
    print("score added for " + name)

  def handle_d(self):
    scores = self.score_store.get_scores()
    for name, score in scores.iteritems():
      print(name + ": " + str(score))

  def handle_r(self):
    name = raw_input("Enter the name of the golfer you want to remove from the file: ")

    if not self.score_store.has_score(name): raise InvalidInputException("This golfer doesn't exist!")

    self.score_store.remove_score(name)

    print("")
    print("score removed for " + name)

  def handle_s(self):
    file_content = open(self.score_store.file_path).read()
    print("File content below")
    print("------------------")
    print(file_content)
    print("------------------")

  def handle_q(self):
    self.should_continue = False
    print("Bye bye")


if __name__ == '__main__':
  StoreRepl(ScoreStore('golfers.txt')).run()