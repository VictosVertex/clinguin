elem(w,window,root).
elem(test_range, range, w).
when(test_range, input, context, (bound, _value)).

elem(lbl, button, w).
attr(lbl, label, "Set").
when(lbl, click, call, set_constant(min_kek,_context_value(bound_min, int,5))).
when(lbl, click, call, set_constant(max_kek,_context_value(bound_max, int,5))).

elem(lab, label, w).
attr(lab, label, @format("min: {}",min_kek)).

elem(lab2, label, w).
attr(lab2, label,  @format("max: {}",max_kek)).