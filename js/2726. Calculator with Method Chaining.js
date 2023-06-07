class Calculator {
  
  /** 
   * @param {number} value
   */
  constructor(value) {
      this.ans = value;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */
  add(value){
      this.ans+=value;
      return this;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */
  subtract(value){
      this.ans-=value;
      return this;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */  
  multiply(value) {
      this.ans*=value;
      return this;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */
  divide(value) {
      if(value == 0){
          throw new Error("Division by zero is not allowed");
      }
      this.ans/=value;
      return this;
  }
  
  /** 
   * @param {number} value
   * @return {Calculator}
   */
  power(value) {
      this.ans**=value;
      return this;
  }
    
  /** 
   * @return {number}
   */
  getResult() {
      return this.ans;
  }
}
