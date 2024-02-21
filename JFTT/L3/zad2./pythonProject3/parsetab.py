
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVrightUMINUSPOWCOM DIV LPAREN MINUS NUMBER PLUS POW RPAREN TIMESSTAR : EXPRSTAR : COMEXPR : EXPR PLUS EXPREXPR : EXPR MINUS EXPREXPR : MINUS EXPR %prec UMINUSEXPR : EXPR TIMES EXPREXPR : EXPR DIV EXPREXPR : EXPR POW EXPEXPONUMR : NUMBEREXP : MINUS EXP %prec UMINUSEXP : EXP PLUS EXPEXP : EXP MINUS EXPEXP : EXP TIMES EXPEXP : EXP DIV EXPEXP : LPAREN EXP RPARENEXP : EXPONUMREXPR : NUMBEREXPR : LPAREN EXPR RPAREN'
    
_lr_action_items = {'COM':([0,],[3,]),'MINUS':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[4,8,4,-17,4,4,4,4,4,19,-5,8,-3,-4,-6,-7,-8,19,19,-16,-9,-18,19,19,19,19,-10,25,-11,-12,-13,-14,-15,]),'NUMBER':([0,4,6,7,8,9,10,11,19,20,24,25,26,27,],[5,5,5,5,5,5,5,22,22,22,22,22,22,22,]),'LPAREN':([0,4,6,7,8,9,10,11,19,20,24,25,26,27,],[6,6,6,6,6,6,6,20,20,20,20,20,20,20,]),'$end':([1,2,3,5,12,14,15,16,17,18,21,22,23,28,30,31,32,33,34,],[0,-1,-2,-17,-5,-3,-4,-6,-7,-8,-16,-9,-18,-10,-11,-12,-13,-14,-15,]),'PLUS':([2,5,12,13,14,15,16,17,18,21,22,23,28,29,30,31,32,33,34,],[7,-17,-5,7,-3,-4,-6,-7,-8,-16,-9,-18,-10,24,-11,-12,-13,-14,-15,]),'TIMES':([2,5,12,13,14,15,16,17,18,21,22,23,28,29,30,31,32,33,34,],[9,-17,-5,9,9,9,-6,-7,-8,-16,-9,-18,-10,26,26,26,-13,-14,-15,]),'DIV':([2,5,12,13,14,15,16,17,18,21,22,23,28,29,30,31,32,33,34,],[10,-17,-5,10,10,10,-6,-7,-8,-16,-9,-18,-10,27,27,27,-13,-14,-15,]),'POW':([2,5,12,13,14,15,16,17,18,21,22,23,28,30,31,32,33,34,],[11,-17,11,11,11,11,11,11,-8,-16,-9,-18,-10,-11,-12,-13,-14,-15,]),'RPAREN':([5,12,13,14,15,16,17,18,21,22,23,28,29,30,31,32,33,34,],[-17,-5,23,-3,-4,-6,-7,-8,-16,-9,-18,-10,34,-11,-12,-13,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'STAR':([0,],[1,]),'EXPR':([0,4,6,7,8,9,10,],[2,12,13,14,15,16,17,]),'EXP':([11,19,20,24,25,26,27,],[18,28,29,30,31,32,33,]),'EXPONUMR':([11,19,20,24,25,26,27,],[21,21,21,21,21,21,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> STAR","S'",1,None,None,None),
  ('STAR -> EXPR','STAR',1,'p_STAR_EXPR','zad2.py',122),
  ('STAR -> COM','STAR',1,'p_STAR_COM','zad2.py',131),
  ('EXPR -> EXPR PLUS EXPR','EXPR',3,'p_add','zad2.py',136),
  ('EXPR -> EXPR MINUS EXPR','EXPR',3,'p_sub','zad2.py',142),
  ('EXPR -> MINUS EXPR','EXPR',2,'p_expr2uminus','zad2.py',148),
  ('EXPR -> EXPR TIMES EXPR','EXPR',3,'p_mult','zad2.py',154),
  ('EXPR -> EXPR DIV EXPR','EXPR',3,'p_div','zad2.py',160),
  ('EXPR -> EXPR POW EXP','EXPR',3,'p_pow','zad2.py',171),
  ('EXPONUMR -> NUMBER','EXPONUMR',1,'p_expnumr_neg','zad2.py',177),
  ('EXP -> MINUS EXP','EXP',2,'p_exp_neg','zad2.py',182),
  ('EXP -> EXP PLUS EXP','EXP',3,'p_exp_add','zad2.py',188),
  ('EXP -> EXP MINUS EXP','EXP',3,'p_exp_sub','zad2.py',194),
  ('EXP -> EXP TIMES EXP','EXP',3,'p_exp_mult','zad2.py',200),
  ('EXP -> EXP DIV EXP','EXP',3,'p_exp_div','zad2.py',206),
  ('EXP -> LPAREN EXP RPAREN','EXP',3,'p_exp_parens','zad2.py',221),
  ('EXP -> EXPONUMR','EXP',1,'p_EXPO_NUM','zad2.py',226),
  ('EXPR -> NUMBER','EXPR',1,'p_expr2NUM','zad2.py',231),
  ('EXPR -> LPAREN EXPR RPAREN','EXPR',3,'p_parens','zad2.py',236),
]
