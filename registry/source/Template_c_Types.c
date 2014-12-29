char *template_c_types[] = {
"MODULE ModName_C_Types",
"",
"  USE , INTRINSIC :: ISO_C_Binding",
"  IMPLICIT NONE",
"",
"  PRIVATE",
"",
"  !==========   ModName C++ Object Pointers   ===",
"  ! Fortran types that will be binded with C++. ",
"  ! These types are pointers to C++ objects.    ",
"  !                                             ",
"  ! Initialization Input States                 ",
"  TYPE , BIND(C) :: ModName_InitInput_C         ",
"     PRIVATE                                    ",
"     TYPE(C_ptr) :: object = C_NULL_ptr         ",
"  END TYPE ModName_InitInput_C                  ",
"                                                ",
"  ! Other States                                ",
"  TYPE , BIND(C) :: ModName_OtherState_C        ",
"     PRIVATE                                    ",
"     TYPE(C_ptr) :: object = C_NULL_ptr         ",
"  END TYPE ModName_OtherState_C                 ",
"  !==============================================",
"",
"",
"  !==========   ModName Object Constructor/Destructor   ==========",
"  !                                                               ",    
"  INTERFACE ! BEGIN: Interface to external C functions            ",    
"                                                                  ",    
"     !==========   ModName C++ Object Constructor/Destructor   ===",
"     !                                                            ",
"     ! Initalize Initialization Input object                      ",
"     FUNCTION C_Create_ModName_InitInput(msg,err) RESULT( this ) &", 
"          !NAME = the C function called inside ' extern \"C\" '   ", 
"          BIND( C , NAME=\"ModName_InitInput_Create\" )           ", 
"       IMPORT                                                     ",
"       TYPE(C_ptr) :: this                                        ",
"       CHARACTER(KIND=C_CHAR), DIMENSION(1024) :: msg             ",
"       INTEGER(KIND=C_INT) :: err                                 ",
"     END FUNCTION C_Create_ModName_InitInput                      ",
"                                                                  ",
"     ! Delete input object                                        ",
"     SUBROUTINE C_Delete_ModName_InitInput( this ) &              ",
"          !NAME = the C function called inside ' extern \"C\" '   ",
"          BIND( C , NAME=\"ModName_InitInput_Delete\" )           ",
"       IMPORT                                                     ",
"       TYPE(C_ptr), VALUE :: this                                 ",
"     END SUBROUTINE C_Delete_ModName_InitInput                    ",
"     !============================================================",
"                                                                  ",
"                                                                  ",
"     !==========   ModName C++ Object Constructor/Destructor   ===",
"     !                                                            ",
"     ! Initalize input object                                     ",
"     FUNCTION C_Create_ModName_Other(msg,err) RESULT( this ) &    ",
"          !NAME = the C function called inside ' extern \"C\" '   ",
"          BIND( C , NAME=\"ModName_OtherState_Create\" )          ",
"       IMPORT                                                     ",
"       TYPE(C_ptr) :: this                                        ",
"       CHARACTER(KIND=C_CHAR), DIMENSION(1024) :: msg             ",
"       INTEGER(KIND=C_INT) :: err                                 ",
"     END FUNCTION C_Create_ModName_Other                          ",
"                                                                  ",
"     ! Delete input object                                        ",
"     SUBROUTINE C_Delete_ModName_Other( this ) &                  ",
"          !NAME = the C function called inside ' extern \"C\" '   ",
"          BIND( C , NAME=\"ModName_OtherState_Delete\" )          ",
"       IMPORT                                                     ",
"       TYPE(C_ptr), VALUE :: this                                 ",
"     END SUBROUTINE C_Delete_ModName_Other                        ",
"     !============================================================",
"  END INTERFACE ! END: Interface to external C functions          ",
"  !===============================================================",
"",
"",
"  !==========   ModName C++ Object Interface   ========",
"  !",
"  ! Input initalize interface                         ",
"  INTERFACE ModName_InitInput_Initialize              ",
"     MODULE PROCEDURE ModName_InitInput_Create        ",
"  END INTERFACE ModName_InitInput_Initialize          ",
"                                                      ",
"  ! Input destructor interface                        ",
"  INTERFACE ModName_InitInput_Destroy                 ",
"     MODULE PROCEDURE ModName_InitInput_Delete        ",
"  END INTERFACE ModName_InitInput_Destroy             ",
"                                                      ",
"                                                      ",
"  ! Input initalize interface                         ",
"  INTERFACE ModName_Other_Initialize                  ",
"     MODULE PROCEDURE ModName_OtherState_Create       ",
"  END INTERFACE ModName_Other_Initialize              ",
"  ! Input Destructor interface                        ",
"  INTERFACE ModName_Other_Destroy                     ",
"     MODULE PROCEDURE ModName_Other_Delete            ",
"  END INTERFACE ModName_Other_Destroy                 ",
"  !====================================================",
"",
"",
"  PUBLIC :: ModName_InitInput_C    , &",
"       ModName_OtherState_C        , &",
"       ModName_InitInput_Initialize, & ",
"       ModName_Other_Initialize    , &",
"       ModName_InitInput_Destroy   , &",
"       ModName_Other_Destroy        ",
"",
"CONTAINS",
"",
"  !==========   ModName C++ Object Interface   ====== ",
"  !",
"  ! Initialization Input type construction",
"  SUBROUTINE ModName_InitInput_Create( this,msg,err )",
"    TYPE( ModName_InitInput_C ), INTENT( OUT ) :: this",
"    CHARACTER(KIND=C_CHAR), DIMENSION(1024) :: msg",
"    INTEGER(KIND=C_INT) :: err",
"    this%object = C_Create_ModName_InitInput(msg,err)",
"  END SUBROUTINE ModName_InitInput_Create",
"  ! Initlialization Input type destruction",
"  SUBROUTINE ModName_InitInput_Delete(this)",
"    TYPE( ModName_InitInput_C ), INTENT(INOUT) :: this",
"    CALL C_Delete_ModName_InitInput( this%object )",
"    this%object = C_NULL_ptr",
"  END SUBROUTINE ModName_InitInput_Delete",
"",
"  ! Other type initialization",
"  SUBROUTINE ModName_OtherState_Create( this,msg,err )",
"    TYPE( ModName_OtherState_C ), INTENT( OUT ) :: this",
"    CHARACTER(KIND=C_CHAR), DIMENSION(1024) :: msg",
"    INTEGER(KIND=C_INT) :: err",
"    this%object = C_Create_ModName_Other(msg,err)",
"  END SUBROUTINE ModName_OtherState_Create",
"  ! Other type destruction",
"  SUBROUTINE ModName_Other_Delete(this)",
"    TYPE( ModName_OtherState_C ), INTENT(INOUT) :: this",
"    CALL C_Delete_ModName_Other( this%object )",
"    this%object = C_NULL_ptr",
"  END SUBROUTINE ModName_Other_Delete",
"  !=======================================================",
"",
"END MODULE ModName_C_Types",
0L } ;
