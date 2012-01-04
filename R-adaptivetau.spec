%global packname  adaptivetau
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.902
Release:          1%{?dist}
Summary:          Tau-leaping stochastic simulation

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implements adaptive tau leaping to approximate the trajectory of a
continuous-time stochastic process as described by Cao et al. (2007) The
Journal of Chemical Physics.  This package is based upon work supported by
the National Science Foundation under Award No. DBI-0906041.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.902-1
- initial package for Fedora