function dice20(rand) {
    this.rand = (Math.floor(Math.random() * 20) + 1);
   }

function test() {
    console.clear();
    console.log("Init")
    let d1 = new dice20()["rand"];    

    if (d1 <= 10) {
        console.log ("Result : " + d1);
        $( "#result" ).append( (d1));
        console.log ("--> To F1");
        f1();        
     } else if (d1 > 10) {
        console.log("Result : " + d1);
        console.log ("--> To F2")
        f2();
     }  
}

function f1() {
    let d2 = new dice20()["rand"];

    if (d2 <= 10) {
        console.log("Result : " + d2);
        console.log ("--> To F11");
        f11();        
     } else if (d2 > 10) {
        console.log("Result : " + d2);
        console.log ("--> To F12")
        f12();
     }  
}

function f11() {
    let d4 = new dice20()["rand"];

    if (d4 <= 10) {
        console.log("Result : " + d4);
        console.log ("--> To F111");
        f111();        
     } else if (d4 > 10) {
        console.log("Result : " + d4);
        console.log ("--> To F112")
        f112();
     }  
}

function f111() {
    let d8 = new dice20()["rand"];
    console.log("Final result : " + d8);     
}

function f112() {
    let d9 = new dice20()["rand"];
    console.log("Final result : " + d9);       
}

function f12() {
    let d5 = new dice20()["rand"];

    if (d5 <= 10) {
        console.log("Result : " + d5);
        console.log ("--> To F121");
        f121();        
     } else if (d5 > 10) {
        console.log("Result : " + d5);
        console.log ("--> To F122")
        f122();
     }  
}

function f121() {
    let d10 = new dice20()["rand"];
    console.log("Final result : " + d10);     
}

function f122() {
    let d11 = new dice20()["rand"];
    console.log("Final result : " + d11);      
}

function f2() {
    let d3 = new dice20()["rand"];

    if (d3 <= 10) {
        console.log("Result : " + d3);
        console.log ("--> To F21");
        f21();        
     } else if (d3 > 10) {
        console.log("Result : " + d3);
        console.log ("--> To F22")
        f22();
     }  
}

function f21() {
    let d6 = new dice20()["rand"];

    if (d6 <= 10) {
        console.log("Result : " + d6);
        console.log ("--> To F211");
        f211();        
     } else if (d6 > 10) {
        console.log("Result : " + d6);
        console.log ("--> To F212")
        f212();
     }  
}

function f211() {
    let d12 = new dice20()["rand"];
    console.log("Final result : " + d12);     
}

function f212() {
    let d13 = new dice20()["rand"];
    console.log("Final result : " + d13);       
}

function f22() {
    let d7 = new dice20()["rand"];

    if (d7 <= 10) {
        console.log("Result : " + d7);
        console.log ("--> To F221");
        f221();        
     } else if (d7 > 10) {
        console.log("Result : " + d7);
        console.log ("--> To F222")
        f222();
     }  
}

function f221() {
    let d14 = new dice20()["rand"];
    console.log("Final result : " + d14);    
}

function f222() {
    let d15 = new dice20()["rand"];
    console.log("Final result : " + d15);       
}