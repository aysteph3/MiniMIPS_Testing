  library ieee;
  library std;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use ieee.std_logic_textio.all; 
  use ieee.math_real.all;
  use std.textio.all;
  use work.pack_mips.all;
  USE work.my_package.ALL;

  entity testbench is 
  end testbench;

  architecture behaviour of testbench is 
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

      signal clock          : std_logic := '0';
      signal reset          : std_logic := '1';
      signal op1            : std_logic_vector(31 downto 0) := "00000000000000000000000000000000";
      signal op2            : std_logic_vector(31 downto 0) := "00000000000000000000000000000000";
      signal ctrl           : std_logic_vector(27 downto 0) := "0000000000000000000000000000";
      signal c              : std_logic_vector(27 downto 0) := "1000000000000000000000000000";
      signal res            : std_logic_vector(31 downto 0) := "00000000000000000000000000000000";
      signal overflow       : std_logic := '0';
      constant clk_period   : time := 10 ns;

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

        
        reset <= '0' after 10 ns;
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
       variable count_value   : integer := 0;
       file     out_file      : text open write_mode is "sim_generated_file/out.txt";
       file   input_file      : text;  --declare input file
       variable line_v        : line;
       variable line_num      : line;
       variable char          : character:='0';
       variable a, b          : string(1 to 32);
       variable num_1         : std_logic_vector (31 downto 0); -- num_1 and num_2 are declared as variable 
       variable num_2         : std_logic_vector (31 downto 0);
       begin 
        while (count_value < c'length) loop
          file_open(input_file, "sim_input/input.txt", read_mode);
          wait for 5 ns;
          f: loop 
            readline(input_file, line_num);
            read(line_num, a);
            read(line_num, b);
              for idx in 1 to 32 loop
                     char := a(idx);
                if(char = '0') then
                  num_1(32-idx) := '0';
                else
                  num_1(32-idx) := '1';
                end if;
              end loop;
        
              for id in 1 to 32 loop
                     char := b(id);
                if(char = '0') then
                  num_2(32-id) := '0';
                else
                  num_2(32-id) := '1';
                end if;
              end loop;

            op1       <= num_1;
            op2       <= num_2;
            ctrl <= std_logic_vector(signed(c) srl count_value);
            wait for 1 ns;
            write(line_v, to_bstring(ctrl)& " " & to_bstring(op1)& " " & to_bstring(op2)& " " & to_bstring(res));
            writeline(out_file, line_v);
            wait for 3 ns;
            exit f when endfile(input_file);
          end loop; -- end of f loop
          write(line_v, string'(""));
          writeline(out_file, line_v);
          wait for 1 ns;
          file_close(input_file);
          count_value := count_value + 1;
        end loop; -- end of while loop
        file_close(out_file);
       wait;
      end process;
  end;
