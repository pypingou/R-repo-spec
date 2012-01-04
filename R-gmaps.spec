%global packname  gmaps
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Wrapper and auxilliary functions for maps package to work with grid graphics system.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-maps R-grid 

BuildRequires:    R-devel tex(latex) R-maps R-grid 

%description
The gmaps package extends the functionality of the maps package for the
grid graphics system.  This enables more advanced plots and more
functionality.  It also makes use of the grid structure to fix problems
encountered with the traditional graphics system, such as resizing of

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
%doc %{rlibdir}/gmaps/html
%doc %{rlibdir}/gmaps/DESCRIPTION
%{rlibdir}/gmaps/NAMESPACE
%{rlibdir}/gmaps/R
%{rlibdir}/gmaps/help
%{rlibdir}/gmaps/INDEX
%{rlibdir}/gmaps/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora