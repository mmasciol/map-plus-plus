import sys
from ctypes import *
import os

class Map(object):
    #lib = cdll.LoadLibrary('map.so') # class level loading lib
    lib = cdll.LoadLibrary('/media/sf_Dropbox/cemats/src/map.so')

    '''
    these are the fortran derived types created by the FAST registry.
    '''
    f_type_init = None
    f_type_initout = None
    f_type_d = None
    f_type_u = None
    f_type_x = None
    f_type_y = None
    f_type_z = None
    f_type_p = None


    ierr = c_int(0)
    status = create_string_buffer(1024)
    summary_file = c_char_p
    val = c_double

    class ModelData_Type(Structure):
        _fields_ = []


    '''
    void * object ;
    double gravity ;
    double seaDensity ;
    double depth ;
    char fileName[255] ;
    char summaryFileName[255] ;
    char libraryInputLine[255] ;
    char nodeInputLine[255] ;
    char elementInputLine[255] ;
    char optionInputLine[255] ;
    '''
    class InitializationData_Type(Structure):
        _fields_= [("object",c_void_p),
                   ("gravity",c_double),
                   ("seaDensity",c_double),
                   ("depth",c_double),
                   ("fileName",c_char*255),
                   ("summaryFileName",c_char*255),
                   ("libraryInputLine",c_char*255),
                   ("nodeInputLine",c_char*255),
                   ("elementInputLine",c_char*255),
                   ("optionInputLine",c_char*255)]

        
    class InitializationOutputData_Type(Structure):
        _fields_ = []


    class InputData_Type(Structure):
        _fields_ = []


    class OutputData_Type(Structure):
        _fields_ = []

        
    '''
    void * object ;
    double g ;
    double depth ;
    double rhoSea ;
    '''
    class ParameterData_Type(Structure):
        _fields_ = [("object",c_void_p),
                    ("g",c_double),
                    ("depth",c_double), 
                    ("rhoSea", c_double)]


    class ConstraintData_Type(Structure):
        _fields_ = []


    class ContinuousData_Type(Structure):
        _fields_ = []


    '''
    fields for the fortran types

    MAP_EXTERNCALL MAP_InitInputType_t* py_create_init_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_InitOutputType_t* py_create_initout_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_InputType_t* py_create_input_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_ParameterType_t* py_create_parameter_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_ConstraintStateType_t* py_create_constraint_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_OtherStateType_t* py_create_model_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_OutputType_t* py_create_output_data( char* msg, MAP_ERROR_CODE* status );
    MAP_EXTERNCALL MAP_ContinuousStateType_t* py_create_continuous_data( char* msg, MAP_ERROR_CODE* status );
    '''
    MapData_Type       = POINTER(ModelData_Type)
    MapInit_Type       = POINTER(InitializationData_Type)
    MapInitOut_Type    = POINTER(InitializationOutputData_Type)
    MapInput_Type      = POINTER(InputData_Type)
    MapOutput_Type     = POINTER(OutputData_Type)
    MapParameter_Type  = POINTER(ParameterData_Type)
    MapConstraint_Type = POINTER(ConstraintData_Type)
    MapContinuous_Type = POINTER(ContinuousData_Type)

    # read file stuff
    lib.set_init_to_null.argtype=[MapInit_Type, c_char_p, POINTER(c_int) ]
    lib.set_summary_file_name.argtype=[MapInit_Type, c_char_p, POINTER(c_int) ]
    lib.set_cable_library_data.argtype=[MapInit_Type]
    lib.set_node_data.argtype=[MapInit_Type]
    lib.set_element_data.argtype=[MapInit_Type]
    lib.set_solver_options.argtype=[MapInit_Type]

    lib.py_create_init_data.argtype       = [ c_char_p, POINTER(c_int) ]
    lib.py_create_initout_data.argtype    = [ c_char_p, POINTER(c_int) ]
    lib.py_create_input_data.argtype      = [ c_char_p, POINTER(c_int) ]
    lib.py_create_parameter_data.argtype  = [ c_char_p, POINTER(c_int) ]
    lib.py_create_constraint_data.argtype = [ c_char_p, POINTER(c_int) ]
    lib.py_create_model_data.argtype      = [ c_char_p, POINTER(c_int) ]
    lib.py_create_output_data.argtype     = [ c_char_p, POINTER(c_int) ]
    lib.py_create_continuous_data.argtype = [ c_char_p, POINTER(c_int) ]
    lib.py_create_continuous_data.argtype = [ MapData_Type ]
    
    lib.py_create_init_data.restype       = MapInit_Type
    lib.py_create_initout_data.restype    = MapInitOut_Type
    lib.py_create_input_data.restype      = MapInput_Type
    lib.py_create_parameter_data.restype  = MapParameter_Type
    lib.py_create_constraint_data.restype = MapConstraint_Type
    lib.py_create_model_data.restype      = MapData_Type
    lib.py_create_output_data.restype     = MapOutput_Type
    lib.py_create_continuous_data.restype = MapContinuous_Type

    lib.fcall_set_sea_depth.argtypes   = [ MapParameter_Type, c_double ]
    lib.fcall_set_gravity.argtypes     = [ MapParameter_Type, c_double ]
    lib.fcall_set_sea_density.argtypes = [ MapParameter_Type, c_double ]
    
    # numeric routines
    lib.pyget_residual_function_length.restype = c_double
    lib.pyget_residual_function_height.restype = c_double
    lib.pyget_jacobian_dxdh.restype            = c_double
    lib.pyget_jacobian_dxdv.restype            = c_double
    lib.pyget_jacobian_dzdh.restype            = c_double
    lib.pyget_jacobian_dzdv.restype            = c_double

    lib.pyget_residual_function_length.argtypes = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_residual_function_height.argtypes = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_jacobian_dxdh.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_jacobian_dxdv.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_jacobian_dzdh.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_jacobian_dzdv.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
    
    # plot routines
    lib.pyget_plot_x.argtypes = [ MapData_Type, c_int, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_plot_x.restype  = POINTER(c_double)
    lib.pyget_plot_y.argtypes = [ MapData_Type, c_int, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_plot_y.restype  = POINTER(c_double)
    lib.pyget_plot_z.argtypes = [ MapData_Type, c_int, c_int, c_char_p, POINTER(c_int) ]
    lib.pyget_plot_z.restype  = POINTER(c_double)
    lib.pyget_plot_array_free.argtypes = [ POINTER(c_double) ]


    # modifyers
    lib.py_offset_vessel.argtypes = [MapData_Type, MapInput_Type, c_double, c_double, c_double, c_double, c_double, c_double, c_char_p, POINTER(c_int)]        
    lib.py_linearize_matrix.argtypes = [MapInput_Type, MapData_Type, MapOutput_Type, MapConstraint_Type, c_double, c_char_p, POINTER(c_int)]        
    lib.py_linearize_matrix.restype  = POINTER(POINTER(c_double))
    lib.py_free_linearize_matrix.argtypes = [POINTER(POINTER(c_double))]

    '''
    MAP_EXTERNCALL void mapcall_msqs_init ( MAP_InitInputType_t* initFortType, 
                                            MAP_InputType_t* inputFortType,
                                            MAP_ParameterType_t* paramFortType,
                                            MAP_ContinuousStateType_t* contFortType,
                                            void* none,
                                            MAP_ConstraintStateType_t* constrFortType,
                                            MAP_OtherStateType_t* otherFortType,
                                            MAP_OutputType_t* outFortType,
                                            MAP_InitOutputType_t* initoutFortType,
                                            MAP_ERROR_CODE *ierr,
                                            char *map_msg )
    '''
    lib.mapcall_msqs_init.argtypes = [ MapInit_Type,
                                       MapInput_Type,
                                       MapParameter_Type,
                                       MapContinuous_Type,
                                       c_void_p,
                                       MapConstraint_Type,
                                       MapData_Type,
                                       MapOutput_Type,
                                       MapInitOut_Type,
                                       POINTER(c_int),
                                       c_char_p]


    lib.mapcall_msqs_update_states.argtypes = [ c_double,
                                                c_int,
                                                MapInput_Type,
                                                MapParameter_Type,
                                                MapContinuous_Type,
                                                c_void_p,
                                                MapConstraint_Type,
                                                MapData_Type,
                                                POINTER(c_int),
                                                c_char_p]

    lib.mapcall_msqs_end.argtypes = [ MapInput_Type,
                                      MapParameter_Type,
                                      MapContinuous_Type,
                                      c_void_p,
                                      MapConstraint_Type,
                                      MapData_Type,
                                      MapOutput_Type,
                                      POINTER(c_int),
                                      c_char_p]


    def __init__( self ) :
        self.f_type_d       = self.CreateDataState()
        self.f_type_u       = self.CreateInputState( )
        self.f_type_x       = self.CreateContinuousState( )
        self.f_type_p       = self.CreateParameterState( )
        self.f_type_y       = self.CreateOutputState( )
        self.f_type_z       = self.CreateConstraintState( )
        self.f_type_init    = self.CreateInitState( )
        self.f_type_initout = self.CreateInitoutState( )
        Map.lib.set_init_to_null(self.f_type_init, self.status, pointer(self.ierr) )
        self.summary_file("outlist.map.sum")


    def Init( self ):
        Map.lib.mapcall_msqs_init( self.f_type_init, self.f_type_u, self.f_type_p, self.f_type_x, None, self.f_type_z, self.f_type_d, self.f_type_y, self.f_type_initout, pointer(self.ierr), self.status )
        if self.ierr.value != 0 :
            print self.status.value        


    def UpdateStates(self, t, interval):
        Map.lib.mapcall_msqs_update_states(t, interval, self.f_type_u, self.f_type_p, self.f_type_x, None, self.f_type_z, self.f_type_d, pointer(self.ierr), self.status )
        if self.ierr.value != 0 :
            print self.status.value        


    """
    Calls function in main.c and fordatamanager.c to delete insteads of c structs. First, the malloc'ed arrays need to vanish
    gracefully; we accomplish this by calling MAP_End(...) routine. Then, the structs themself are deleted. Order is important.

    MAP_EXTERNCALL int MAP_End ( InputData *u, ParameterData *p, ContinuousData *x, ConstraintData *z, ModelData *data, OutputData *y, char *map_msg, MAP_ERROR_CODE *ierr )
    MAP_EXTERNCALL void MAP_Input_Delete( InputData* u )
    MAP_EXTERNCALL void MAP_Param_Delete( ParameterData* p )
    MAP_EXTERNCALL void MAP_ContState_Delete( InputData* x )
    MAP_EXTERNCALL void MAP_ConstrState_Delete( InputData* z )
    MAP_EXTERNCALL void MAP_Output_Delete( InputData* y )
    MAP_EXTERNCALL void MAP_OtherState_Delete( ModelData* data )
    """
    def MAP_End( self ):
        Map.lib.mapcall_msqs_end( self.f_type_u, self.f_type_p, self.f_type_x, None, self.f_type_z, self.f_type_d, self.f_type_y, pointer(self.ierr), self.status )

    """
    Set a name for the MAP summary file. Does not need to be called. If not called, the default name is 'outlist.sum.map'
    """
    def summary_file( self, echo_file ):
        self.f_type_init.contents.summaryFileName = echo_file
        Map.lib.set_summary_file_name(self.f_type_init, self.status, pointer(self.ierr) )


    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL InitializationData* MAP_InitInput_Create( char* map_msg, MAP_ERROR_CODE* ierr )
    """
    def CreateInitState( self ) :
        obj = Map.lib.py_create_init_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL void MAP_InitOutput_Delete( InputData* io )
    """
    def CreateInitoutState( self ) :
        obj = Map.lib.py_create_initout_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL ModelData *MAP_OtherState_Create( char *map_msg, MAP_ERROR_CODE *ierr )
    """
    def CreateDataState( self ) :
        obj = Map.lib.py_create_model_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL InputData* MAP_Input_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    """
    def CreateInputState( self ) :
        obj = Map.lib.py_create_input_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL ContinuousData* MAP_ContState_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    """
    def CreateContinuousState( self ) :
        obj = Map.lib.py_create_continuous_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL OutputData *MAP_Output_Create( char *map_msg, MAP_ERROR_CODE *ierr )
    """
    def CreateOutputState( self ) :
        obj = Map.lib.py_create_output_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL ConstraintData* MAP_ConstrState_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    """
    def CreateConstraintState( self ) :
        obj = Map.lib.py_create_constraint_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    """
    Calls function in fortdatamanager.c to create instance of c structs
    MAP_EXTERNCALL ParameterData* MAP_Param_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    """
    def CreateParameterState( self ) :
        obj = Map.lib.py_create_parameter_data( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
        return obj

    def set_sea_depth( self, depth ):
        Map.lib.fcall_set_sea_depth( self.f_type_p, depth )

    def set_gravity( self, g ):
        Map.lib.fcall_set_gravity( self.f_type_p, g )

    def set_sea_density( self, rho ):
        Map.lib.fcall_set_sea_density( self.f_type_p, rho )

    def funcl( self, i ) :
        self.val = Map.lib.pyget_residual_function_length( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        return self.val

    def funch( self, i ) :
        self.val = Map.lib.pyget_residual_function_height( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        return self.val

    def dxdh( self, i ) :
        self.val = Map.lib.pyget_jacobian_dxdh( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        return self.val


    def dxdv( self, i ) :
        self.val = Map.lib.pyget_jacobian_dxdv( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        return self.val

    def dzdh( self, i ) :
        self.val = Map.lib.pyget_jacobian_dzdh( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        return self.val

    def dzdv( self, i ) :
        self.val = Map.lib.pyget_jacobian_dzdv( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        return self.val


    def plot_x( self, elementNum, length ) :
        arr = [None]*length
        array = POINTER(c_double)
        array = Map.lib.pyget_plot_x( self.f_type_d, elementNum, length, self.status, pointer(self.ierr) )        
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            Map.lib.pyget_plot_array_free( array )        
            sys.exit('MAP terminated premature.')
        arr = [array[j] for j in range(length)]        
        Map.lib.pyget_plot_array_free( array )        
        return arr 


    def linear( self, epsilon ) :
        array = POINTER(POINTER(c_double))
        array = Map.lib.py_linearize_matrix( self.f_type_u, self.f_type_d, self.f_type_y, self.f_type_z, epsilon, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')
        arr = [[array[j][i] for i in range(6)] for j in range(6)]
        Map.lib.py_free_linearize_matrix(array)        
        return arr
    

    def displace_vessel(self,x,y,z,phi,the,psi) :
        Map.lib.py_offset_vessel(self.f_type_d, self.f_type_u, x,y,z,phi,the,psi, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            sys.exit('MAP terminated premature.')

    
    def plot_y( self, elementNum, length ) :
        arr = [None]*length
        array = POINTER(c_double)
        array = Map.lib.pyget_plot_y( self.f_type_d, elementNum, length, self.status, pointer(self.ierr) )        
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            Map.lib.pyget_plot_array_free( array )        
            sys.exit('MAP terminated premature.')
        arr = [array[j] for j in range(length)]        
        Map.lib.pyget_plot_array_free( array )        
        return arr 


    def plot_z( self, elementNum, length ) :
        arr = [None]*length
        array = POINTER(c_double)
        array = Map.lib.pyget_plot_z( self.f_type_d, elementNum, length, self.status, pointer(self.ierr) )        
        if self.ierr.value != 0 :
            print self.status.value        
            self.MAP_End( )
            Map.lib.pyget_plot_array_free( array )        
            sys.exit('MAP terminated premature.')
        arr = [array[j] for j in range(length)]        
        Map.lib.pyget_plot_array_free( array )        
        return arr 
    

    def read_file( self, fileName ):
        f           = open(fileName, 'r')
        charptr     = POINTER(c_char)
        line_offset = []
        offset      = 0
        temp_str    = []
    
        for line in f:
            line_offset.append(offset)
            offset += len(line)
    
        f.seek(0)
    
        i = 0
        for line in f:
            words = line.split()
            if words[0] == "LineType":
                next(f)
                LineType_ref = i
            elif words[0] == "Node":
                next(f)
                Node_ref = i
            elif words[0] == "Element":
                next(f)
                Element_ref = i 
            elif words[0] == "Option":
                next(f)
                Option_ref = i 
    
            i+=1
        
        f.seek(line_offset[LineType_ref+2])
         
        for line in f:
            if line[0] == "-":
                break
            else:
                self.f_type_init.contents.libraryInputLine=line
                Map.lib.set_cable_library_data(self.f_type_init)
   
        f.seek(line_offset[Node_ref+3])

        for line in f:
            if line[0] == "-":
                break
            else:
                self.f_type_init.contents.nodeInputLine=line
                Map.lib.set_node_data(self.f_type_init)

        f.seek(line_offset[Element_ref+4])

        for line in f:
            if line[0] == "-":
                break
            else:
                self.f_type_init.contents.elementInputLine=line
                Map.lib.set_element_data(self.f_type_init)
                 
        f.seek(line_offset[Option_ref+5])

        for line in f:
            if line[0]=="-":
                break
            elif line[0]=="!":
                None
            else:
                self.f_type_init.contents.optionInputLine=line
                Map.lib.set_solver_options(self.f_type_init)            
