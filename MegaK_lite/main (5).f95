program MegaK_lite
implicit none

integer:: n, m
character:: op

read(*,*) n
read(*,*) op
read(*,*) m
select case(op)
	case('-')
    	write(*,*) n-m
	case("+")
    	write(*,*) n+m
	case("/")
    	write(*,*) n/m
	case("*")
    	write(*,*) n*m
	case default
    	write(*,*) "none"
end select

end program MegaK_lite