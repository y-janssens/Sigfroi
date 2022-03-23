/*

const rank = document.getElementById('rank').value;
    const forValue = document.getElementById('For').value;
    const endValue = document.getElementById('End').value;
    const habValue = document.getElementById('Hab').value;
    const charValue = document.getElementById('Char').value;
    const intValue = document.getElementById('Int').value;
    const iniValue = document.getElementById('Ini').value;
    const attValue = document.getElementById('Att').value;
    const parValue = document.getElementById('Par').value;
    const tirValue = document.getElementById('Tir').value;
    const naValue = document.getElementById('Na').value;
    const pvValue = document.getElementById('Pv').value;

    function setValues() {       
        if (rank == 1) {
            let for1Value = document.getElementById('For1V').value;
            let end1Value = document.getElementById('End1V').value;
            let hab1Value = document.getElementById('Hab1V').value;
            let char1Value = document.getElementById('Char1V').value;
            let int1Value = document.getElementById('Int1V').value;
            let ini1Value = document.getElementById('Ini1V').value;
            let att1Value = document.getElementById('Att1V').value;
            let par1Value = document.getElementById('Par1V').value;
            let tir1Value = document.getElementById('Tir1V').value;
            let na1Value = document.getElementById('Na1V').value;
            let pv1Value = document.getElementById('Pv1V').value;

            document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(for1Value))
            document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(end1Value))
            document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(hab1Value))
            document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(char1Value))
            document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(int1Value))
            document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(ini1Value))
            document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(att1Value))
            document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(par1Value))
            document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(tir1Value))
            document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(na1Value))
            document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(pv1Value))
            
        } else if (rank == 2) {
            let for1Value = document.getElementById('For2V').value;
            let end1Value = document.getElementById('End2V').value;
            let hab1Value = document.getElementById('Hab2V').value;
            let char1Value = document.getElementById('Char2V').value;
            let int1Value = document.getElementById('Int2V').value;
            let ini1Value = document.getElementById('Ini2V').value;
            let att1Value = document.getElementById('Att2V').value;
            let par1Value = document.getElementById('Par2V').value;
            let tir1Value = document.getElementById('Tir2V').value;
            let na1Value = document.getElementById('Na2V').value;
            let pv1Value = document.getElementById('Pv2V').value;

            document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(for1Value))
            document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(end1Value))
            document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(hab1Value))
            document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(char1Value))
            document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(int1Value))
            document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(ini1Value))
            document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(att1Value))
            document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(par1Value))
            document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(tir1Value))
            document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(na1Value))
            document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(pv1Value))

        } else if (rank == 3) {
            let for1Value = document.getElementById('For3V').value;
            let end1Value = document.getElementById('End3V').value;
            let hab1Value = document.getElementById('Hab3V').value;
            let char1Value = document.getElementById('Char3V').value;
            let int1Value = document.getElementById('Int3V').value;
            let ini1Value = document.getElementById('Ini3V').value;
            let att1Value = document.getElementById('Att3V').value;
            let par1Value = document.getElementById('Par3V').value;
            let tir1Value = document.getElementById('Tir3V').value;
            let na1Value = document.getElementById('Na3V').value;
            let pv1Value = document.getElementById('Pv3V').value;

            document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(for1Value))
            document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(end1Value))
            document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(hab1Value))
            document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(char1Value))
            document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(int1Value))
            document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(ini1Value))
            document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(att1Value))
            document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(par1Value))
            document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(tir1Value))
            document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(na1Value))
            document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(pv1Value))

        } else if (rank == 4) {
            let for1Value = document.getElementById('For4V').value;
            let end1Value = document.getElementById('End4V').value;
            let hab1Value = document.getElementById('Hab4V').value;
            let char1Value = document.getElementById('Char4V').value;
            let int1Value = document.getElementById('Int4V').value;
            let ini1Value = document.getElementById('Ini4V').value;
            let att1Value = document.getElementById('Att4V').value;
            let par1Value = document.getElementById('Par4V').value;
            let tir1Value = document.getElementById('Tir4V').value;
            let na1Value = document.getElementById('Na4V').value;
            let pv1Value = document.getElementById('Pv4V').value;

            document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(for1Value))
            document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(end1Value))
            document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(hab1Value))
            document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(char1Value))
            document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(int1Value))
            document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(ini1Value))
            document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(att1Value))
            document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(par1Value))
            document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(tir1Value))
            document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(na1Value))
            document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(pv1Value))
        }
        
    }
    
    window.onload = setValues();

    document.querySelectorAll('.changeInput').forEach(item => {
        item.addEventListener('change', e => {
            if (e.target.id == "For1V") {        
                document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(e.target.value))    
                   
            } else if (e.target.id == "End1V") {        
                document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(e.target.value))
        
            } else if (e.target.id == "Hab1V") {        
                document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Char1V") {        
                document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(e.target.value))   
        
            } else if (e.target.id == "Int1V") {        
                document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Ini1V") {        
                document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Att1V") {        
                document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Par1V") {        
                document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Tir1V") {        
                document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Na1V") {        
                document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Pv1V") {        
                document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(e.target.value))

            } else if (e.target.id == "For2V") {        
                document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(e.target.value))    
                   
            } else if (e.target.id == "End2V") {        
                document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(e.target.value))
        
            } else if (e.target.id == "Hab2V") {        
                document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Char2V") {        
                document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(e.target.value))   
        
            } else if (e.target.id == "Int2V") {        
                document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Ini2V") {        
                document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Att2V") {        
                document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Par2V") {        
                document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Tir2V") {        
                document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Na2V") {        
                document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Pv2V") {        
                document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(e.target.value))      

            } else if (e.target.id == "For3V") {        
                document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(e.target.value))    
                   
            } else if (e.target.id == "End3V") {        
                document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(e.target.value))
        
            } else if (e.target.id == "Hab3V") {        
                document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Char3V") {        
                document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(e.target.value))   
        
            } else if (e.target.id == "Int3V") {        
                document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Ini3V") {        
                document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Att3V") {        
                document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Par3V") {        
                document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Tir3V") {        
                document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Na3V") {        
                document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Pv3V") {        
                document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(e.target.value))   

            } else if (e.target.id == "For4V") {        
                document.getElementById('For').setAttribute('value', parseInt(forValue) + parseInt(e.target.value))    
                   
            } else if (e.target.id == "End4V") {        
                document.getElementById('End').setAttribute('value', parseInt(endValue) + parseInt(e.target.value))
        
            } else if (e.target.id == "Hab4V") {        
                document.getElementById('Hab').setAttribute('value', parseInt(habValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Char4V") {        
                document.getElementById('Char').setAttribute('value', parseInt(charValue) + parseInt(e.target.value))   
        
            } else if (e.target.id == "Int4V") {        
                document.getElementById('Int').setAttribute('value', parseInt(intValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Ini4V") {        
                document.getElementById('Ini').setAttribute('value', parseInt(iniValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Att4V") {        
                document.getElementById('Att').setAttribute('value', parseInt(attValue) + parseInt(e.target.value))    
        
            } else if (e.target.id == "Par4V") {        
                document.getElementById('Par').setAttribute('value', parseInt(parValue) + parseInt(e.target.value))  
        
            } else if (e.target.id == "Tir4V") {        
                document.getElementById('Tir').setAttribute('value', parseInt(tirValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Na4V") {        
                document.getElementById('Na').setAttribute('value', parseInt(naValue) + parseInt(e.target.value)) 
        
            } else if (e.target.id == "Pv4V") {        
                document.getElementById('Pv').setAttribute('value', parseInt(pvValue) + parseInt(e.target.value))       
            }
        })
      })

*/