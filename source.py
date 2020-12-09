class estimate:

    def _init_(self, OfficeSpacesqFt,    NumberofEmployeesperSqFt ):
        self.OfficeSpacesqFt=df['Office Space (Sq.Ft.)']
        self.NumberofEmployeesperSqFt=df['Number of Employees per 1,000 Sq.Ft.']



    def avg_office_building_space():

        """ Returns the average of office the office building space 
        """
        return df['Office Space (Sq.Ft.)'].mean()
    
    
    def num_employees_per_building():

        """ Returns number of employees per building  
        """
        return df['Office Space (Sq.Ft.)']*df['Number of Employees per 1,000 Sq.Ft.']/1000
    
    
    
    def avg_num_employees_per_building():
        a=num_employees_per_building().mean()
        """ Returns the Average number of employees per building.
        """
        return math.ceil(a)


    def num_persontrip_automode():
        b=num_employees_per_building()*0.2
        """ Returns the Number of person-trips which use auto mode 
        """
        return round(b)


    def tot_num_persontrip_automode():
        """ Returns the Total number of person-trips that use auto mode  
        """
        return num_persontrip_automode().sum()
    
    
    
    def num_persontrip_busmode():
        c=num_employees_per_building()*0.3
        """ Returns the Number of person-trips bus mode 
        """
        return round(c)

    
    
    def tot_num_persontrip_busmode():
        """ Returns the Total number of person-trips bus mode   
        """
        return num_persontrip_busmode().sum()


    def num_persontrip_subwaymode():
        d=num_employees_per_building()*1.3
        """ Returns the Number of person-trips subway mode 
        """
        return round(d)


    
    def tot_num_persontrip_subwaymode():
        """ Returns the Total number of person-trips subway mode   
        """
        return num_persontrip_subwaymode().sum()


    
    
    def num_persontrip_railmode():
        e=num_employees_per_building()*0.2
        """ Returns the Number of person-trips subway mode 
        """
        return round(e)


    def tot_num_persontrip_railmode():
        """ Returns the Total number of person-trips rail mode  
        """
        return num_persontrip_railmode().sum()
    
    
    
    
    
    def num_vehicletrip_per_building_autobus_mode():
    
        f=num_persontrip_automode()/1.48
    
        g=num_persontrip_busmode()/48
    
        """ Returns the Number vehicle-trips per building (auto + bus)
        """
        return round(f+g)
    
    
    def vehicletrip_per_building_autobus_mode():
    
        h=tot_num_persontrip_automode()/1.48
    
        i=tot_num_persontrip_busmode()/48
    
        """ Returns the Vehicle-trips per building (auto + bus)
        """
        return round(h+i)
    
