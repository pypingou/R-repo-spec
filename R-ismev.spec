%global packname  ismev
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.37
Release:          1%{dist}
Summary:          An Introduction to Statistical Modeling of Extreme Values

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions to support the computations carried out in `An Introduction to
Statistical Modeling of Extreme Values' by Stuart Coles. The functions may
be divided into the following groups; maxima/minima, order statistics,
peaks over thresholds and point processes.

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
%doc %{rlibdir}/ismev/DESCRIPTION
%doc %{rlibdir}/ismev/html
%{rlibdir}/ismev/README
%{rlibdir}/ismev/help
%{rlibdir}/ismev/Meta
%{rlibdir}/ismev/data
%{rlibdir}/ismev/demo
%{rlibdir}/ismev/R
%{rlibdir}/ismev/CHANGES
%{rlibdir}/ismev/RCHANGES
%{rlibdir}/ismev/NAMESPACE
%{rlibdir}/ismev/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.37-1
- Update to version 1.37

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.36-1
- initial package for Fedora