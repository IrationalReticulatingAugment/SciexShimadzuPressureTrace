import frida
import sys
import time
import datetime

# Replace this file path with your own if you want pressure logs to be saved somewhere else.
# keep your path inside the quotes.
filepath = ""

session = frida.attach("analyst.exe")

script = session.create_script(
"""
// Find base address of viutlu...
baseAddr = Module.findBaseAddress('viutlu.dll');
console.log('viutlu.dll baseAddr: '+ baseAddr);

// Our offset of the GetStatus function, determined via debugger
var getstatusoffset = 0x00050380;
var funcaddress = baseAddr.add(getstatusoffset);
console.log('get status address: ' + funcaddress);

Interceptor.attach(funcaddress, {
            onEnter: function (args) {
				// 0x25 is the switch value that gets pump a pressure, determined via debugger
                if (args[0] == 0x25) {
                    this.Arg0 = args[0]
                    // console.log('arg0 ' + args[0]);
                    // console.log('arg1 ' + args[1]);
                }
            },
            onLeave: function (retval) {
                if (this.Arg0 == 0x25) {
                    // send communicates with our python function
                    send(Memory.readDouble(this.context.edx));
                    // console.log('retval: ' + this.context.edx);
                }
            }
        });
""")

if __name__ == "__main__":
    dated_filepath = filepath + "Pressure Log " + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")) + ".txt"
    log_file = open(dated_filepath,"w")

    log_file.write("Datetime, Pressure \n")
    def on_message(message, data):
        log_file.write(str(datetime.datetime.now()).split('.')[0] + "," + str(format(message['payload'], '.2f')) + "\n")
        # flushing the data to the file lets us open the file with another application while still collecting pressure.
        log_file.flush()

    script.on('message', on_message)
    script.load()

    #print("Collecting Pressure data. Press ctrl-d to stop collecting data.")
    #sys.stdin.read()
    input("Collecting Pressure data. Press enter to stop.")
    session.detach()
    print("Detached")
    log_file.close()
    print("File Closed")
