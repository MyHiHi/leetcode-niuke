object Hello{
  implicit def man2Superman(man:Man):Superman=new Superman(man.name)
  class Man(val name:String){
    def eat(food:String)={
      println(s"I am a man called $name eating $food")
    }
  }
  class Superman(val name:String){
    def fly()={
      println(s"I am a superman called $name flying")
    }
  }
  def main(args: Array[String]): Unit = {
    val man=new Man("Leo");
    man.eat("西红柿");
    man.fly()
  }
}