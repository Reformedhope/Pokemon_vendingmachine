class Coin {
  constructor(value) {
    this.value = value
  }
}

class Dime extends Coin {
  constructor() {
    super(0.10)
  }
}

class Register {
  constructor() {
    this.drawer = {
      pennies: [],
      nickles: [],
      dimes: [],
      quarters: [],
    }

    while (this.drawer.dimes < 5) {
      const new_dime = new Dime()
      this.drawer.dimes.push(new_dime)
    }
  }
}

class Culvers {
  constructor() {
    this.registers = []

    for (let i = 0; i < 7; i++) {
      this.registers.push(new Register())
    }
  }
}
