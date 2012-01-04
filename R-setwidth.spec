%global packname  setwidth
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Set the value of options("width") on terminal emulators

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Automatically sets the value of options("width") when the terminal
emulator is resized. The functions of this package only work if R is
compiled for Unix systems and it is running interactively in a terminal

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
%doc %{rlibdir}/setwidth/NEWS
%doc %{rlibdir}/setwidth/html
%doc %{rlibdir}/setwidth/DESCRIPTION
%{rlibdir}/setwidth/help
%{rlibdir}/setwidth/Meta
%{rlibdir}/setwidth/libs
%{rlibdir}/setwidth/NAMESPACE
%{rlibdir}/setwidth/INDEX
%{rlibdir}/setwidth/R

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3-1
- initial package for Fedora