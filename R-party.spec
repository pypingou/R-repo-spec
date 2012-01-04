%global packname  party
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.99995
Release:          1%{?dist}
Summary:          A Laboratory for Recursive Partytioning

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-99995.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-survival R-grid R-modeltools R-coin R-zoo R-sandwich R-strucchange R-vcd R-stats 


BuildRequires:    R-devel tex(latex) R-methods R-survival R-grid R-modeltools R-coin R-zoo R-sandwich R-strucchange R-vcd R-stats



%description
A computational toolbox for recursive partitioning. The core of the
package is ctree(), an implementation of conditional inference trees which
embed tree-structured regression models into a well defined theory of
conditional inference procedures. This non-parametric class of regression
trees is applicable to all kinds of regression problems, including
nominal, ordinal, numeric, censored as well as multivariate response
variables and arbitrary measurement scales of the covariates. Based on
conditional inference trees, cforest() provides an implementation of
Breiman's random forests. The function mob() implements an algorithm for
recursive partitioning based on parametric models (e.g. linear models,
GLMs or survival regression) employing parameter instability tests for
split selection. Extensible functionality for visualizing tree-structured
regression models is available.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.99995-1
- initial package for Fedora