%global packname  colorout
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          Colorize R output on terminal emulators

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Colorize R output when it is running on a terminal emulator. There is no
support for Graphical User Interfaces, such as Windows RGui, RStudio,
RKward, JGR etc. The functions of this package only work if R is compiled
for Unix systems and it is running interactively in a terminal emulator.
The terminal must support Select Graphic Rendition (SGR, also known as
ANSI escape codes or sequences). The package contains a C library with a
function that replaces the default Rstd_WriteConsoleEx which, when
enabled, is responsible for printing messages in the Console when R is
running in interactive mode. Screenshot:

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/colorout/NEWS
%doc %{rlibdir}/colorout/html
%doc %{rlibdir}/colorout/DESCRIPTION
%{rlibdir}/colorout/R
%{rlibdir}/colorout/libs
%{rlibdir}/colorout/NAMESPACE
%{rlibdir}/colorout/po
%{rlibdir}/colorout/LICENSE
%{rlibdir}/colorout/INDEX
%{rlibdir}/colorout/Meta
%{rlibdir}/colorout/help

%changelog
* Sun Dec 04 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.4-1
- initial package for Fedora