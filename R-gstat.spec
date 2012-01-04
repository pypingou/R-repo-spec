%global packname  gstat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.10
Release:          1%{?dist}
Summary:          spatial and spatio-temporal geostatistical modelling, prediction and simulation

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-sp R-spacetime 
Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-sp R-spacetime
BuildRequires:    R-lattice 


%description
variogram modelling; simple, ordinary and universal point or block
(co)kriging, sequential Gaussian or indicator (co)simulation; variogram
and variogram map plotting utility functions.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.10-1
- initial package for Fedora