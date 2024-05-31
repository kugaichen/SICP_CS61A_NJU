;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (cond
    ((= total 0)(list '()))
    ((or (= biggest 0)(< total 0)) '())
    (else
      (let ((with-biggest (make-change (- total biggest) biggest))
        (without-biggest (make-change total (- biggest 1)))
      )
      (append 
        (map (lambda (lst) (cons biggest lst)) with-biggest)
        without-biggest)
      )
    )
  )
)


(define (find n lst)
  (define (findest n lst x)
    (cond 
      ((= n (car lst)) x)
      (else (findest n (cdr lst) (+ x 1)))
    )  
  )

  (findest n lst 0)
)

(define (find-nest n sym)
  (define (helper lst expr)
    (if (pair? lst)
      (let 
        ((r1 
          (helper (car lst) (list 'car expr))
        ))
        (if (null? r1) (helper (cdr lst) (list 'cdr expr)) r1)
      )
      (if (and (number? lst) (= n lst)) expr nil)))
  (helper (eval sym) sym)
)


(define-macro (def func args body)
  `(define ,(cons func args) ,body)
)


(define-macro (k-curry fn args vals indices)
 
)


(define-macro (let* bindings expr)
  ''YOUR-CODE-HERE
)

;;; Just For Fun Problems

; Tree ADT
(define (tree label branches) (cons label branches))
(define (label t) (car t))
(define (branches t) (cdr t))
(define (is-leaf t) (null? (branches t)))

; A tree for test
(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 3 nil)
        (tree 7 (list
          (tree 7 nil)))))
    (tree 3 nil)
    (tree 6
      (list
        (tree 7 nil))))))

(define (find-in-tree t goal)
  'YOUR-CODE-HERE
)

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  ''YOUR-CODE-HERE
)
