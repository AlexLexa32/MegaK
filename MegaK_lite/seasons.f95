program a
implicit none

integer:: m

write(*,*) 'введите номер месяца'
read(*,*) m

select case(m)
	case(1,2,12)
    	write(*,*) 'зима'
	case(3:5)
    	write(*,*) 'весна'
	case(6:8)
    	write(*,*) 'лето'
	case(9:11)
    	write(*,*) 'осень'
	case default
    	write(*,*) 'некоректные данные'
end select

end program a