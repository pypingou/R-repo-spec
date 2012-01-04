%global packname  pmg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.42
Release:          1%{?dist}
Summary:          Poor Man's GUI

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-42.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-MASS R-proto R-foreign R-gWidgets R-gWidgetsRGtk2 


BuildRequires:    R-devel tex(latex) R-lattice R-MASS R-proto R-foreign R-gWidgets R-gWidgetsRGtk2



%description
Simple GUI for R using gWidgets.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.42-1
- initial package for Fedora