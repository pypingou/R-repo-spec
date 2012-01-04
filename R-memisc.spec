%global packname  memisc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.95.35
Release:          1%{?dist}
Summary:          Tools for Management of Survey Data, Graphics, Programming, Statistics, and Simulation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.95-35.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-grid R-stats R-methods R-utils R-MASS 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-stats R-methods R-utils R-MASS 

%description
One of the aims of this package is to make life easier for useRs who deal
with survey data sets. It provides an infrastructure for the management of
survey data including value labels, definable missing values, recoding of
variables, production of code books, and import of (subsets of) SPSS and
Stata files. Further, it provides functionality to produce tables and data
frames of arbitrary descriptive statistics and (almost) publication-ready
tables of regression model estimates. Also some convenience tools for
graphics, programming, and simulation are provided.

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
%doc %{rlibdir}/memisc/NEWS
%doc %{rlibdir}/memisc/html
%doc %{rlibdir}/memisc/DESCRIPTION
%doc %{rlibdir}/memisc/doc
%{rlibdir}/memisc/anes
RPM build errors:
%{rlibdir}/memisc/INDEX
%{rlibdir}/memisc/help
%{rlibdir}/memisc/Meta
%{rlibdir}/memisc/demo
%{rlibdir}/memisc/libs
%{rlibdir}/memisc/NAMESPACE
%{rlibdir}/memisc/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.95.35-1
- initial package for Fedora