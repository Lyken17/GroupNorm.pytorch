int new_lib_add_forward(THFloatTensor *input1, THFloatTensor *input2,
		       THFloatTensor *output);
int new_lib_add_backward(THFloatTensor *grad_output, THFloatTensor *grad_input);
