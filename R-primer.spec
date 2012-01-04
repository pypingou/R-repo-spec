%global packname  primer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Functions and data for the forthcoming, A Primer of Ecology with R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-deSolve R-lattice 

BuildRequires:    R-devel tex(latex) R-deSolve R-lattice 

%description
Functions are primarily functions for systems of ordinary differential
equations, difference equations, and eigenanalysis and projection of
demographic matrices; data are for examples.

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
%doc %{rlibdir}/primer/DESCRIPTION
%doc %{rlibdir}/primer/html
%{rlibdir}/primer/Meta
%{rlibdir}/primer/R
%{rlibdir}/primer/INDEX
%{rlibdir}/primer/data
%{rlibdir}/primer/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora