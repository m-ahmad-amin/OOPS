class Animal {
  speak() {
    console.log("speaks");
  }
}
// Animal.prototype = null;
// Object.setPrototypeOf(Animal.prototype, null);
class Dog extends Animal {
  barks() {
    console.log("barks");
  }
}

const d = new Dog();
