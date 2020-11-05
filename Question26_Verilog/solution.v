module det_1011 ( input clk,
                  input rstn,
                  input in,
                  output out );
  
  parameter IDLE 	= 0,
  			S1 		= 1,
  			S10 	= 2,
  			S101 	= 3,
  			S1011 	= 4;
  
  reg [2:0] cur_state, next_state;
  
  assign out = cur_state == S1011 ? 1 : 0;
  
  always @ (posedge clk) begin
    if (!rstn)
      	cur_state <= IDLE;
     else 
     	cur_state <= next_state;
  end
  
  always @ (cur_state or in) begin
    case (cur_state)
      IDLE : begin
        if (in) next_state = S1;
        else next_state = IDLE;
      end
      
      S1: begin
`ifdef BUG_FIX        
        if (in) next_state = S1;
`else
        if (in) next_state = IDLE;
`endif        
        else 	next_state = S10;
      end
      
      S10 : begin
        if (in) next_state = S101;        
        else 	next_state = IDLE;
      end
      
      S101 : begin
        if (in) next_state = S1011;
`ifdef BUG_FIX        
		else 	next_state = S10;
`else        
        else 	next_state = IDLE;
`endif        
      end
      
      S1011: begin
        next_state = IDLE;
      end
    endcase
  end
endmodule


module tb;
  reg 			clk, in, rstn;
  wire 			out;
  reg [1:0] l_dly;
  reg 			tb_in;
  integer 	loop = 20;
  
  always #10 clk = ~clk;
  
  det_1011 u0 ( .clk(clk), .rstn(rstn), .in(in), .out(out) );
  
  initial begin
  	clk <= 0;
    rstn <= 0;
    in <= 0;
    
    repeat (5) @ (posedge clk);
    rstn <= 1;

`ifndef RANDOM
    @(posedge clk) in <= 1;
    @(posedge clk) in <= 0;
    @(posedge clk) in <= 1;
    @(posedge clk) in <= 0;
    @(posedge clk) in <= 1;
    @(posedge clk) in <= 1;
    @(posedge clk) in <= 0;
    @(posedge clk) in <= 1;
    @(posedge clk) in <= 0;
    @(posedge clk) in <= 1;
    @(posedge clk) in <= 1;

`else    
    for (int i = 0 ; i < loop; i ++) begin
      l_dly = $random;
      repeat (l_dly) @ (posedge clk);
      tb_in = $random;
      in <= tb_in;
    end
`endif    
    
    #100 $finish;
  end
  
  always @ (posedge clk) begin
    $strobe ("T=%0t in=%0b out=%0b", $time, in, out);
  end
  
  initial begin
    $dumpvars;
    $dumpfile("dump.vcd");
  end
endmodule
