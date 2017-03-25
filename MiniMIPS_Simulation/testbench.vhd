  library ieee;
  library std;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use ieee.std_logic_textio.all; 
  use ieee.math_real.all;
  use std.textio.all;
  use work.pack_mips.all;

  entity testbecnch is 
  end testbecnch;

  architecture behaviour of testbecnch is 
  	-- component declaration 
  		component alu is
  			port(
  					clock : in bus1;
   					reset : in bus1;
   					op1 : in bus32;            -- Operand 1
   					op2 : in bus32;            -- Operand 2
   					ctrl : in alu_ctrl_type;   -- Opearator control

   					res : out bus32;           -- The result is 32 bit long
   					overflow : out bus1        -- Overflow of the result
  				);
  		end component;

  		signal clock 			    : std_logic := '0';
  		signal reset 			    : std_logic := '1';
  		signal op1 				    : std_logic_vector(31 downto 0) := "00000000000000000000000000000000";
  		signal op2 				    : std_logic_vector(31 downto 0) := "00000000000000000000000000000000";
  		signal ctrl 	        : std_logic_vector(27 downto 0) := "0000000000000000000000000000";
  		signal c              : std_logic_vector(27 downto 0) := "1000000000000000000000000000";
      signal res 				    : std_logic_vector(31 downto 0) := "00000000000000000000000000000000";
  		signal overflow 		  : std_logic := '0';
  		constant clk_period 	: time := 10 ns;

  		begin 
  			uut: alu port map(
  					clock => clock,
  					reset => reset,
  					op1 => op1,
  					op2 => op2,
  					ctrl => ctrl,
  					res => res,
  					overflow => overflow
  				);

  			
  			reset <= '0' after 1 ns;
clk_process:
  			process
  			 begin
  			     clock <= '0';
  			     wait for clk_period/2;  --for 5 ns signal is '0'.
  			     clock <= '1';
  			     wait for clk_period/2;  --for next 5 ns signal is '1'.
  			end process;

monitor:
 			process
       variable count_value : integer := 0;
 			 begin 
        while (count_value < c'length) loop
          --wait for 2 ns;
 			    op1 			<= "00000000000000000000000000000010";
 			    op2 			<= "00000000000000000000000000000001";
 			    --ctrl 	<= "1000000000000000000000000000";
          ctrl <= std_logic_vector(signed(c) srl count_value);
          --wait for 2 ns;
          count_value := count_value + 1;
          wait for 3 ns;
          --ctrl  <= ctrl (26 downto 0) & '0';
        end loop;
 			 wait;
 			end process;
  end;