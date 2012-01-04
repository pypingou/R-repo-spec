%global packname  MIfuns
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.1
Release:          1%{?dist}
Summary:          Pharmacometric tools for data preparation, modeling, simulation, and reporting

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-reshape R-methods R-lattice R-grid R-XML R-MASS 


BuildRequires:    R-devel tex(latex) R-reshape R-methods R-lattice R-grid R-XML R-MASS



%description
Pharmacometric tools for common data preparation tasks, stratified
bootstrap resampling of data sets, NONMEM control stream creation/editing,
NONMEM model execution, creation of standard and user-defined diagnostic
plots, execution and summary of bootstrap and predictive check results,
implementation of simulations from posterior parameter distributions,
reporting of output tables and creation of detailed analysis logs. 
Deprecated.  Please see the replacement package: metrumrg.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.1-1
- initial package for Fedora