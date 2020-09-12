module rw2(clk, d, 1out, 2out);
	input clk;
	input[3..0] d,c;
	output[3..0] 1out, 2out;
	reg[3..0] 1out;
	reg[3..0] 2out;
	assign 2out = d & ~out1;
	always@(posedge clk)
		begin
			2out <= (d==c)?4'hFF:4'd18;
		end
endmodule
