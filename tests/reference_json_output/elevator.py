import json


class Elevator:
    @classmethod
    def get_reference_json(cls):
        json_dict = {
            "id": "root",
            "type": "root",
            "parent": "root",
            "attributes": [],
            "callbacks": [],
            "children": [
                {
                    "id": "window",
                    "type": "window",
                    "parent": "root",
                    "attributes": [
                        {"id": "window", "key": "height", "value": "800"},
                        {"id": "window", "key": "width", "value": "300"},
                        {"id": "window", "key": "child_layout", "value": "absstatic"},
                    ],
                    "callbacks": [],
                    "children": [
                        {
                            "id": "elevator",
                            "type": "container",
                            "parent": "window",
                            "attributes": [
                                {
                                    "id": "elevator",
                                    "key": "child_layout",
                                    "value": "grid",
                                }
                            ],
                            "callbacks": [],
                            "children": [
                                {
                                    "id": "elevator_row(1)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(1)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(1)",
                                            "key": "grid_row",
                                            "value": "10",
                                        },
                                        {
                                            "id": "elevator_row(1)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(1)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(1)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "background_color",
                                                    "value": '"#C1E5AE"',
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [
                                                {
                                                    "id": "elevator_occ_mi(1,wait)",
                                                    "type": "dropdown_menu_item",
                                                    "parent": "elevator_floor(1)",
                                                    "attributes": [
                                                        {
                                                            "id": "elevator_occ_mi(1,wait)",
                                                            "key": "label",
                                                            "value": "wait",
                                                        }
                                                    ],
                                                    "callbacks": [
                                                        {
                                                            "id": "elevator_occ_mi(1,wait)",
                                                            "action": "click",
                                                            "policy": "assume_and_step(occ(wait,1))",
                                                        }
                                                    ],
                                                    "children": [],
                                                },
                                                {
                                                    "id": "elevator_occ_mi(1,down)",
                                                    "type": "dropdown_menu_item",
                                                    "parent": "elevator_floor(1)",
                                                    "attributes": [
                                                        {
                                                            "id": "elevator_occ_mi(1,down)",
                                                            "key": "label",
                                                            "value": "down",
                                                        }
                                                    ],
                                                    "callbacks": [
                                                        {
                                                            "id": "elevator_occ_mi(1,down)",
                                                            "action": "click",
                                                            "policy": "assume_and_step(occ(down,1))",
                                                        }
                                                    ],
                                                    "children": [],
                                                },
                                                {
                                                    "id": "elevator_occ_mi(1,up)",
                                                    "type": "dropdown_menu_item",
                                                    "parent": "elevator_floor(1)",
                                                    "attributes": [
                                                        {
                                                            "id": "elevator_occ_mi(1,up)",
                                                            "key": "label",
                                                            "value": "up",
                                                        }
                                                    ],
                                                    "callbacks": [
                                                        {
                                                            "id": "elevator_occ_mi(1,up)",
                                                            "action": "click",
                                                            "policy": "assume_and_step(occ(up,1))",
                                                        }
                                                    ],
                                                    "children": [],
                                                },
                                            ],
                                        },
                                        {
                                            "id": "elevator_call(1)",
                                            "type": "label",
                                            "parent": "elevator_row(1)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(1)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(1),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(10)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(10)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(10)",
                                            "key": "grid_row",
                                            "value": "1",
                                        },
                                        {
                                            "id": "elevator_row(10)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(10)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(10)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(10)",
                                            "type": "label",
                                            "parent": "elevator_row(10)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(10)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(10),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(9)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(9)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(9)",
                                            "key": "grid_row",
                                            "value": "2",
                                        },
                                        {
                                            "id": "elevator_row(9)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(9)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(9)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(9)",
                                            "type": "label",
                                            "parent": "elevator_row(9)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(9)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(9),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(8)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(8)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(8)",
                                            "key": "grid_row",
                                            "value": "3",
                                        },
                                        {
                                            "id": "elevator_row(8)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(8)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(8)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(8)",
                                            "type": "label",
                                            "parent": "elevator_row(8)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(8)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(8),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(7)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(7)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(7)",
                                            "key": "grid_row",
                                            "value": "4",
                                        },
                                        {
                                            "id": "elevator_row(7)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(7)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(7)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(7)",
                                            "type": "label",
                                            "parent": "elevator_row(7)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(7)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(7),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(6)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(6)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(6)",
                                            "key": "grid_row",
                                            "value": "5",
                                        },
                                        {
                                            "id": "elevator_row(6)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(6)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(6)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(6)",
                                            "type": "label",
                                            "parent": "elevator_row(6)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "foreground_color",
                                                    "value": "red",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "background_color",
                                                    "value": '"#E5C2AE"',
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(5)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(5)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(5)",
                                            "key": "grid_row",
                                            "value": "6",
                                        },
                                        {
                                            "id": "elevator_row(5)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(5)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(5)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(5)",
                                            "type": "label",
                                            "parent": "elevator_row(5)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(5)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(5),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(4)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(4)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(4)",
                                            "key": "grid_row",
                                            "value": "7",
                                        },
                                        {
                                            "id": "elevator_row(4)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(4)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(4)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(4)",
                                            "type": "label",
                                            "parent": "elevator_row(4)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(4)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(4),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(3)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(3)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(3)",
                                            "key": "grid_row",
                                            "value": "8",
                                        },
                                        {
                                            "id": "elevator_row(3)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(3)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(3)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(3)",
                                            "type": "label",
                                            "parent": "elevator_row(3)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(3)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(3),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(2)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(2)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(2)",
                                            "key": "grid_row",
                                            "value": "9",
                                        },
                                        {
                                            "id": "elevator_row(2)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(2)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(2)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(2)",
                                            "type": "label",
                                            "parent": "elevator_row(2)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(2)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(2),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(0)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(0)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(0)",
                                            "key": "grid_row",
                                            "value": "11",
                                        },
                                        {
                                            "id": "elevator_row(0)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(0)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(0)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(0)",
                                            "type": "label",
                                            "parent": "elevator_row(0)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(0)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(0),0))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "info",
                            "type": "container",
                            "parent": "window",
                            "attributes": [
                                {"id": "info", "key": "pos_x", "value": "140"},
                                {"id": "info", "key": "pos_y", "value": "0"},
                                {"id": "info", "key": "child_layout", "value": "grid"},
                            ],
                            "callbacks": [],
                            "children": [
                                {
                                    "id": "info_find_l",
                                    "type": "button",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_find_l",
                                            "key": "label",
                                            "value": '"Find plan"',
                                        },
                                        {
                                            "id": "info_find_l",
                                            "key": "grid_row",
                                            "value": "1",
                                        },
                                        {
                                            "id": "info_find_l",
                                            "key": "width",
                                            "value": "120",
                                        },
                                        {
                                            "id": "info_find_l",
                                            "key": "height",
                                            "value": "70",
                                        },
                                    ],
                                    "callbacks": [
                                        {
                                            "id": "info_find_l",
                                            "action": "click",
                                            "policy": "find_plan",
                                        }
                                    ],
                                    "children": [],
                                },
                                {
                                    "id": "info_steps_l",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_steps_l",
                                            "key": "grid_row",
                                            "value": "4",
                                        },
                                        {
                                            "id": "info_steps_l",
                                            "key": "label",
                                            "value": '"History:"',
                                        },
                                        {
                                            "id": "info_steps_l",
                                            "key": "font_size",
                                            "value": "18",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_find_goal",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_find_goal",
                                            "key": "grid_row",
                                            "value": "0",
                                        },
                                        {
                                            "id": "info_find_goal",
                                            "key": "font_size",
                                            "value": "20",
                                        },
                                        {
                                            "id": "info_find_goal",
                                            "key": "foreground_color",
                                            "value": "red",
                                        },
                                        {
                                            "id": "info_find_goal",
                                            "key": "label",
                                            "value": '"✕"',
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                            ],
                        },
                    ],
                }
            ],
        }

        return json.loads(json.dumps(json_dict))

    @classmethod
    def post_find_plan(cls):
        json_dict = {
            "id": "root",
            "type": "root",
            "parent": "root",
            "attributes": [],
            "callbacks": [],
            "children": [
                {
                    "id": "window",
                    "type": "window",
                    "parent": "root",
                    "attributes": [
                        {"id": "window", "key": "height", "value": "800"},
                        {"id": "window", "key": "width", "value": "300"},
                        {"id": "window", "key": "child_layout", "value": "absstatic"},
                    ],
                    "callbacks": [],
                    "children": [
                        {
                            "id": "elevator",
                            "type": "container",
                            "parent": "window",
                            "attributes": [
                                {
                                    "id": "elevator",
                                    "key": "child_layout",
                                    "value": "grid",
                                }
                            ],
                            "callbacks": [],
                            "children": [
                                {
                                    "id": "elevator_row(6)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(6)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(6)",
                                            "key": "grid_row",
                                            "value": "5",
                                        },
                                        {
                                            "id": "elevator_row(6)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(6)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(6)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "background_color",
                                                    "value": '"#C1E5AE"',
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(6)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [
                                                {
                                                    "id": "elevator_occ_mi(6,serve)",
                                                    "type": "dropdown_menu_item",
                                                    "parent": "elevator_floor(6)",
                                                    "attributes": [
                                                        {
                                                            "id": "elevator_occ_mi(6,serve)",
                                                            "key": "label",
                                                            "value": "serve",
                                                        }
                                                    ],
                                                    "callbacks": [
                                                        {
                                                            "id": "elevator_occ_mi(6,serve)",
                                                            "action": "click",
                                                            "policy": "assume_and_step(occ(serve,6))",
                                                        }
                                                    ],
                                                    "children": [],
                                                }
                                            ],
                                        },
                                        {
                                            "id": "elevator_call(6)",
                                            "type": "label",
                                            "parent": "elevator_row(6)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "foreground_color",
                                                    "value": "red",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "background_color",
                                                    "value": '"#E5C2AE"',
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(6)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(10)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(10)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(10)",
                                            "key": "grid_row",
                                            "value": "1",
                                        },
                                        {
                                            "id": "elevator_row(10)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(10)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(10)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(10)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(10)",
                                            "type": "label",
                                            "parent": "elevator_row(10)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(10)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(10)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(10),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(9)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(9)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(9)",
                                            "key": "grid_row",
                                            "value": "2",
                                        },
                                        {
                                            "id": "elevator_row(9)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(9)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(9)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(9)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(9)",
                                            "type": "label",
                                            "parent": "elevator_row(9)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(9)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(9)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(9),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(8)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(8)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(8)",
                                            "key": "grid_row",
                                            "value": "3",
                                        },
                                        {
                                            "id": "elevator_row(8)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(8)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(8)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(8)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(8)",
                                            "type": "label",
                                            "parent": "elevator_row(8)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(8)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(8)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(8),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(7)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(7)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(7)",
                                            "key": "grid_row",
                                            "value": "4",
                                        },
                                        {
                                            "id": "elevator_row(7)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(7)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(7)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(7)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(7)",
                                            "type": "label",
                                            "parent": "elevator_row(7)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(7)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(7)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(7),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(5)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(5)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(5)",
                                            "key": "grid_row",
                                            "value": "6",
                                        },
                                        {
                                            "id": "elevator_row(5)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(5)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(5)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(5)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(5)",
                                            "type": "label",
                                            "parent": "elevator_row(5)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(5)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(5)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(5),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(4)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(4)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(4)",
                                            "key": "grid_row",
                                            "value": "7",
                                        },
                                        {
                                            "id": "elevator_row(4)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(4)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(4)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(4)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(4)",
                                            "type": "label",
                                            "parent": "elevator_row(4)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(4)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(4)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(4),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(3)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(3)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(3)",
                                            "key": "grid_row",
                                            "value": "8",
                                        },
                                        {
                                            "id": "elevator_row(3)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(3)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(3)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(3)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(3)",
                                            "type": "label",
                                            "parent": "elevator_row(3)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(3)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(3)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(3),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(2)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(2)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(2)",
                                            "key": "grid_row",
                                            "value": "9",
                                        },
                                        {
                                            "id": "elevator_row(2)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(2)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(2)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(2)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(2)",
                                            "type": "label",
                                            "parent": "elevator_row(2)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(2)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(2)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(2),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(1)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(1)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(1)",
                                            "key": "grid_row",
                                            "value": "10",
                                        },
                                        {
                                            "id": "elevator_row(1)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(1)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(1)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(1)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(1)",
                                            "type": "label",
                                            "parent": "elevator_row(1)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(1)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(1)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(1),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                                {
                                    "id": "elevator_row(0)",
                                    "type": "container",
                                    "parent": "elevator",
                                    "attributes": [
                                        {
                                            "id": "elevator_row(0)",
                                            "key": "child_layout",
                                            "value": "grid",
                                        },
                                        {
                                            "id": "elevator_row(0)",
                                            "key": "grid_row",
                                            "value": "11",
                                        },
                                        {
                                            "id": "elevator_row(0)",
                                            "key": "grid_column",
                                            "value": "0",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [
                                        {
                                            "id": "elevator_floor(0)",
                                            "type": "dropdown_menu",
                                            "parent": "elevator_row(0)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "grid_column",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_floor(0)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [],
                                            "children": [],
                                        },
                                        {
                                            "id": "elevator_call(0)",
                                            "type": "label",
                                            "parent": "elevator_row(0)",
                                            "attributes": [
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "label",
                                                    "value": '"⬆︎⬇︎"',
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "grid_row",
                                                    "value": "0",
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "grid_column",
                                                    "value": "1",
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "width",
                                                    "value": "70",
                                                },
                                                {
                                                    "id": "elevator_call(0)",
                                                    "key": "height",
                                                    "value": "70",
                                                },
                                            ],
                                            "callbacks": [
                                                {
                                                    "id": "elevator_call(0)",
                                                    "action": "click",
                                                    "policy": "add_atom(holds(called(0),5))",
                                                }
                                            ],
                                            "children": [],
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "info",
                            "type": "container",
                            "parent": "window",
                            "attributes": [
                                {"id": "info", "key": "pos_x", "value": "140"},
                                {"id": "info", "key": "pos_y", "value": "0"},
                                {"id": "info", "key": "child_layout", "value": "grid"},
                            ],
                            "callbacks": [],
                            "children": [
                                {
                                    "id": "info_step_c(6)",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_step_c(6)",
                                            "key": "label",
                                            "value": "serve",
                                        },
                                        {
                                            "id": "info_step_c(6)",
                                            "key": "width",
                                            "value": "200",
                                        },
                                        {
                                            "id": "info_step_c(6)",
                                            "key": "height",
                                            "value": "30",
                                        },
                                        {
                                            "id": "info_step_c(6)",
                                            "key": "grid_row",
                                            "value": "10",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_step_c(5)",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_step_c(5)",
                                            "key": "label",
                                            "value": "up",
                                        },
                                        {
                                            "id": "info_step_c(5)",
                                            "key": "width",
                                            "value": "200",
                                        },
                                        {
                                            "id": "info_step_c(5)",
                                            "key": "height",
                                            "value": "30",
                                        },
                                        {
                                            "id": "info_step_c(5)",
                                            "key": "grid_row",
                                            "value": "9",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_step_c(4)",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_step_c(4)",
                                            "key": "label",
                                            "value": "up",
                                        },
                                        {
                                            "id": "info_step_c(4)",
                                            "key": "width",
                                            "value": "200",
                                        },
                                        {
                                            "id": "info_step_c(4)",
                                            "key": "height",
                                            "value": "30",
                                        },
                                        {
                                            "id": "info_step_c(4)",
                                            "key": "grid_row",
                                            "value": "8",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_step_c(3)",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_step_c(3)",
                                            "key": "label",
                                            "value": "up",
                                        },
                                        {
                                            "id": "info_step_c(3)",
                                            "key": "width",
                                            "value": "200",
                                        },
                                        {
                                            "id": "info_step_c(3)",
                                            "key": "height",
                                            "value": "30",
                                        },
                                        {
                                            "id": "info_step_c(3)",
                                            "key": "grid_row",
                                            "value": "7",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_step_c(2)",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_step_c(2)",
                                            "key": "label",
                                            "value": "up",
                                        },
                                        {
                                            "id": "info_step_c(2)",
                                            "key": "width",
                                            "value": "200",
                                        },
                                        {
                                            "id": "info_step_c(2)",
                                            "key": "height",
                                            "value": "30",
                                        },
                                        {
                                            "id": "info_step_c(2)",
                                            "key": "grid_row",
                                            "value": "6",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_step_c(1)",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_step_c(1)",
                                            "key": "label",
                                            "value": "up",
                                        },
                                        {
                                            "id": "info_step_c(1)",
                                            "key": "width",
                                            "value": "200",
                                        },
                                        {
                                            "id": "info_step_c(1)",
                                            "key": "height",
                                            "value": "30",
                                        },
                                        {
                                            "id": "info_step_c(1)",
                                            "key": "grid_row",
                                            "value": "5",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_steps_l",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_steps_l",
                                            "key": "grid_row",
                                            "value": "4",
                                        },
                                        {
                                            "id": "info_steps_l",
                                            "key": "label",
                                            "value": '"History:"',
                                        },
                                        {
                                            "id": "info_steps_l",
                                            "key": "font_size",
                                            "value": "18",
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                                {
                                    "id": "info_find_goal",
                                    "type": "label",
                                    "parent": "info",
                                    "attributes": [
                                        {
                                            "id": "info_find_goal",
                                            "key": "grid_row",
                                            "value": "0",
                                        },
                                        {
                                            "id": "info_find_goal",
                                            "key": "font_size",
                                            "value": "20",
                                        },
                                        {
                                            "id": "info_find_goal",
                                            "key": "foreground_color",
                                            "value": "green",
                                        },
                                        {
                                            "id": "info_find_goal",
                                            "key": "label",
                                            "value": '"✓"',
                                        },
                                    ],
                                    "callbacks": [],
                                    "children": [],
                                },
                            ],
                        },
                    ],
                }
            ],
        }

        return json.loads(json.dumps(json_dict))
