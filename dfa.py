"""
This class implements a DFA structure. States, in Q, is a list of the possible states of the
DFA. Sigma is the alphabet that the DFA can accept. If a symbol not in the alphabet is provided
to the delta_hat function, it will issue an error message and abort execution. 
delta is a dictionary with keys of the model (state, symbol), and the content referenced by the
key is the state p resulting of delta(state, symbol). F is a list that contains the accepting states of the DFA, 
and q0, an one-character string, is the start state.
The delta_hat method takes in a string and evaluates whether it belongs to the DFA's language or not. 
The delta_hat_hat method iterates over a list of strings, for 
ease of use with larger amounts of input.
The show_automata method prints out the contents of the DFA.
"""
class DFA:
  def __init__(self, Q: list, Sigma: list, delta: dict, F: list, q0: str):
    self.Q = Q
    self.Sigma = Sigma
    self.delta = delta
    self.F = F
    self.q0 = q0

  def delta_hat(self, string: str):
    current_state = self.q0
    for symbol in string:
      if symbol not in self.Sigma:
        print(f"String contains symbol not in alphabet {self.Sigma}")
        return
      current_state = self.delta[(current_state, symbol)]
    if current_state in self.F:
      print(f"{string} belongs to the language of the DFA.")
    else:
      print(f"{string} does not belong to the language of the DFA.")

  def delta_hat_hat(self, string_list: list):
    for string in string_list:
      self.delta_hat(string)

  def show_automata(self):
    print(f"States: {self.Q}")
    print(f"Alphabet: {self.Sigma}")
    print(f"Transition Function: {self.delta}")
    print(f"Accepting States: {self.F}")
    print(f"Starting State: {self.q0}")


"""
Example usage of the class. This DFA accepts only strings ended by 01 or 00.
"""
def main():
  DFA_1 = DFA(
      ["A", "B", "C", "D"], ["0", "1"], {
          ("A", "0"): "B",
          ("A", "1"): "A",
          ("B", "0"): "C",
          ("B", "1"): "D",
          ("C", "0"): "C",
          ("C", "1"): "D",
          ("D", "0"): "B",
          ("D", "1"): "A"
      }, ["C", "D"], "A")

  string_list = [
      "00", "01", "0010", "0001001", "000000", "001110", "0110110", "00001"
  ]
  DFA_1.delta_hat_hat(string_list)


if __name__ == "__main__":
  main()
