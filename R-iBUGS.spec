%global packname  iBUGS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          An Interface to R2WinBUGS by gWidgets

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R2WinBUGS R-gWidgetsRGtk2 


BuildRequires:    R-devel tex(latex) R-R2WinBUGS R-gWidgetsRGtk2



%description
This package has provided an interface to WinBUGS/OpenBUGS via R2WinBUGS.
Some options will be intelligently guessed, e.g. the path to
WinBUGS/OpenBUGS and the data/parameter list. Users can specify all the
options in a GUI.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora